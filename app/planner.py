from app.domain import ResearchPlan,ResearchTask
class Planner:
 def plan(self,goal:str,mode:str)->ResearchPlan:
  if mode=="shallow":
   return ResearchPlan(objective=goal,tasks=[ResearchTask(key="lookup",question=goal,source_types=["enterprise","web"])],success_criteria=["answer is evidence-backed"])
  qs=[
   ("scope",f"Establish definitions, scope and key entities for: {goal}"),
   ("internal",f"Find relevant enterprise evidence for: {goal}"),
   ("external",f"Find authoritative public evidence for: {goal}"),
   ("analysis",f"Analyze quantitative or structured evidence relevant to: {goal}"),
  ]
  return ResearchPlan(objective=goal,tasks=[ResearchTask(key=k,question=q,source_types=["enterprise"] if k=="internal" else ["web"] if k=="external" else ["enterprise","web"]) for k,q in qs],success_criteria=["material claims have citations","contradictions are surfaced","limitations are explicit"])
