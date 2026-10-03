from app.planner import Planner
from app.compiler import compile_plan
from app.retrieval import HybridRetriever
from app.evidence_graph import EvidenceGraph
from app.agents import ResearchAgent,DataAnalysisAgent,CriticAgent
from app.contradictions import detect
from app.citations import validate_claims
from app.report import Writer
from app.evaluator import evaluate
from app.budget import Budget
class ResearchRuntime:
 async def run(self,r):
  mode="deep" if r.mode=="auto" else r.mode
  plan=Planner().plan(r.goal,mode);compile_plan(plan);budget=Budget(tasks=len(plan.tasks));graph=EvidenceGraph()
  retriever=HybridRetriever();researcher=ResearchAgent();claims=[];all_ev=[]
  for t in plan.tasks:
   ev=await retriever.search(t.question,t.source_types,r.tenant_id,r.allowed_sources);budget.tool_calls+=1;budget.sources+=len(ev)
   for e in ev:graph.add_evidence(e)
   all_ev.extend(ev);c=await researcher.synthesize_task(t,ev);claims.append(c);graph.add_claim(c)
   if not budget.allow():break
  contradictions=detect(all_ev);validations=validate_claims(claims,all_ev);critique=await CriticAgent().critique(claims,contradictions,validations)
  report=Writer().write(r.goal,claims,all_ev,contradictions,critique);score=evaluate(report,validations,contradictions,budget)
  return {"mode":mode,"plan":plan.model_dump(),"evidence_graph":graph.context(),"analysis":await DataAnalysisAgent().analyze(all_ev),"contradictions":contradictions,"critique":critique,"evaluation":score,"report":report.model_dump()}
