from app.config import settings
class ModelRouter:
 def route(self,role,complexity="normal"):
  if role in {"intent","shallow"}:return {"provider":"nvidia","model":"nemotron-fast-profile"}
  if role in {"planner","researcher","writer","critic"}:return {"provider":"nvidia","model":"nemotron-reasoning-profile"}
  return {"provider":"frontier" if settings.frontier_model_base_url else "nvidia","model":"orchestrator-profile"}
