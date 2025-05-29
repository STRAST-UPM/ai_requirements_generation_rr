from typing import List, Dict, Any, Optional, Callable
from langchain.chains.base import Chain
from langchain.chains.sequential import SequentialChain
from langchain.callbacks.manager import CallbackManagerForChainRun, AsyncCallbackManagerForChainRun

import random
import time

class EarlyStoppingSequentialChain(SequentialChain):
  """Sequential chain with early stopping conditions."""

  stop_conditions: List[Callable[[Dict[str, Any]], bool]]

  def _invoke_with_retries(self, chain: Chain, inputs: Dict[str, Any], callbacks: CallbackManagerForChainRun) -> Dict[str, Any]:
    error = True
    while error:
      try:
        result = chain(inputs, return_only_outputs=True, callbacks=callbacks)
        error = False
      except Exception as e:
        print(f"Error when trying to run chain: {e}")
        random_wait = random.randint(0, 10)
        print(f"Retrying in {random_wait} seconds...")
        time.sleep(random_wait)
    return result
  
  def _check_stop_conditions(self, outputs: Dict[str, Any]) -> bool:
    """Check if any stop condition is met."""
    return any(condition(outputs) for condition in self.stop_conditions)

  def _call(
    self,
    inputs: Dict[str, str],
    run_manager: Optional[CallbackManagerForChainRun] = None,
  ) -> Dict[str, str]:
    known_values = inputs.copy()
    _run_manager = run_manager or CallbackManagerForChainRun.get_noop_manager()
    
    for i, chain in enumerate(self.chains):
      callbacks = _run_manager.get_child()
      outputs = self._invoke_with_retries(chain, known_values, callbacks)
      known_values.update(outputs)
      
      if self._check_stop_conditions(known_values):
        break  # Stop execution if any stop condition is met
    
    return {k: known_values.get(k, None) for k in self.output_variables}

  async def _acall(
    self,
    inputs: Dict[str, Any],
    run_manager: Optional[AsyncCallbackManagerForChainRun] = None,
  ) -> Dict[str, Any]:
    known_values = inputs.copy()
    _run_manager = run_manager or AsyncCallbackManagerForChainRun.get_noop_manager()
    callbacks = _run_manager.get_child()
    
    for i, chain in enumerate(self.chains):
      outputs = await chain.acall(
        known_values, return_only_outputs=True, callbacks=callbacks
      )
      known_values.update(outputs)
      
      if self._check_stop_conditions(known_values):
        break  # Stop execution if any condition is met
      
    return {k: known_values.get(k, None) for k in self.output_variables}
