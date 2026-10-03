from dataclasses import dataclass
from app.config import settings
@dataclass
class Budget:
 loops:int=0;tasks:int=0;sources:int=0;model_calls:int=0;tool_calls:int=0;cost_usd:float=0
 def allow(self):
  return self.loops<settings.max_research_loops and self.tasks<=settings.max_tasks and self.sources<=settings.max_sources and self.model_calls<=settings.max_model_calls and self.tool_calls<=settings.max_tool_calls and self.cost_usd<=settings.max_budget_usd
 def snapshot(self): return self.__dict__.copy()
