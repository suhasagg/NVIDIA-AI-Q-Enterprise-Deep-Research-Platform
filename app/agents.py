import hashlib
from app.domain import Claim
class ResearchAgent:
 async def synthesize_task(self,task,evidence):
  eid=[e.id for e in evidence]
  cid=hashlib.sha256(task.key.encode()).hexdigest()[:10]
  return Claim(id=cid,text=f"Evidence-backed synthesis for research task: {task.question}",evidence_ids=eid,confidence=.75 if eid else .1)
class DataAnalysisAgent:
 async def analyze(self,evidence):return {"evidence_count":len(evidence),"source_types":sorted({e.source_type for e in evidence})}
class CriticAgent:
 async def critique(self,claims,contradictions,validations):
  gaps=[v["claim_id"] for v in validations if not v["valid"]]
  return {"decision":"RERESEARCH" if gaps else "PASS","unsupported_claims":gaps,"contradictions":contradictions}
