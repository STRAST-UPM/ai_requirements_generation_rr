from typing import List, Dict, Any, Optional
from pydantic import ConfigDict
from langchain.chains.base import Chain
from langchain.callbacks.manager import CallbackManagerForChainRun, AsyncCallbackManagerForChainRun

import threading
import random
import time

FORCE_SEQUENTIAL = False

class ParallelChain(Chain):
  """Chain that executes multiple chains in parallel and combines results."""

  chains: List[Chain]
  input_variables: List[str]
  model_config = ConfigDict(
    arbitrary_types_allowed=True,
    extra="forbid",
  )

  @property
  def input_keys(self) -> List[str]:
    """Return input keys expected by the chain.

    :meta private:
    """
    return self.input_variables

  @property
  def output_keys(self) -> List[str]:
    """Generate a list of output keys based on all chains' outputs.

    :meta private:
    """
    if len(self.chains) == 1:
      return self.chains[0].output_keys
    output_keys = []
    for chain_id in range(len(self.chains)):
      output_keys.extend([f"{k}_{chain_id}" for k in self.chains[0].output_keys])
    return output_keys

  def validate_chains(self) -> None:
    """Ensure each chain can accept the given input variables."""
    for chain in self.chains:
      if not all(key in self.input_variables for key in chain.input_keys):
        raise ValueError(
          f"Chain {chain} has input keys {chain.input_keys} "
          "not covered by input_variables."
        )
  
  def _invoke_with_retries(self, chain: Chain, inputs: Dict[str, Any]) -> Dict[str, Any]:
    error = True
    while error:
      try:
        result = chain.invoke(inputs)
        error = False
      except Exception as e:
        print(f"Error when trying to run chain: {e}")
        random_wait = random.randint(0, 10)
        print(f"Retrying in {random_wait} seconds...")
        time.sleep(random_wait)
    return result
      
  def _parallel_thread(self, chain_id: int, chain: Chain, inputs: Dict[str, Any], results: Dict[str, Any]) -> None:
    result = self._invoke_with_retries(chain, inputs)
    if chain_id is None:
      result = {k: v for k, v in result.items() if k not in self.input_variables}
    else:
      result = {f"{k}_{chain_id}": v for k, v in result.items() if k not in self.input_variables}
    results.update(result)

  def _call(
    self,
    inputs: Dict[str, Any],
    run_manager: Optional[CallbackManagerForChainRun] = None,
  ) -> Dict[str, Any]:
    results = {}
    if FORCE_SEQUENTIAL:
      for (chain_id, chain) in enumerate(self.chains):
        result = self._invoke_with_retries(chain, inputs)
        # Append _i to the output keys to avoid conflicts
        result = {f"{k}_{chain_id if len(self.chains) != 1 else None}": v for k, v in result.items() if k not in self.input_variables}
        results.update(result)
    else:
      threads = []
      for (chain_id, chain) in enumerate(self.chains):
        thread = threading.Thread(
          target=self._parallel_thread,
          args=(chain_id if len(self.chains) != 1 else None,
                chain, inputs, results)
        )
        threads.append(thread)
        thread.start()
      for thread in threads:
        thread.join()
    return results

  async def _acall(
    self,
    inputs: Dict[str, Any],
    run_manager: Optional[AsyncCallbackManagerForChainRun] = None,
  ) -> Dict[str, Any]:
    raise NotImplementedError("Async call is not implemented yet.")
