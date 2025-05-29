from typing import List, Dict, Any, Optional, Callable
from langchain.chains.base import Chain
from langchain.chains.sequential import SequentialChain
from langchain.callbacks.manager import CallbackManagerForChainRun, AsyncCallbackManagerForChainRun

import random
import time

class RetryingSequentialChain(SequentialChain):
  """Sequential chain with early stopping conditions."""

  @property
  def output_keys(self) -> List[str]:
    """Generate a list of output keys based on all chains' outputs.

    :meta private:
    """
    output_keys = []
    for chain in self.chains:
      output_keys.extend(chain.output_keys)
    return output_keys

  def _invoke_with_retries(self, chain: Chain, inputs: Dict[str, Any], callbacks: CallbackManagerForChainRun) -> Dict[str, Any]:
    error = True
    while error:
      try:
        result = chain(inputs, return_only_outputs=True, callbacks=callbacks)
        error = False
      except Exception as e:
        print(f"Error when trying to run chain: {e}")
        random_wait = random.randint(20, 60)
        print(f"Retrying in {random_wait} seconds...")
        time.sleep(random_wait)
    return result
  
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
    
    return {k: known_values.get(k, None) for k in self.output_keys}

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
            
    return {k: known_values.get(k, None) for k in self.output_keys}
