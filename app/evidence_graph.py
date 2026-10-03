class EvidenceGraph:
 def __init__(self):self.evidence={};self.claims={};self.edges=[]
 def add_evidence(self,e):self.evidence[e.id]=e
 def add_claim(self,c):
  self.claims[c.id]=c
  for e in c.evidence_ids:self.edges.append((c.id,e,"SUPPORTED_BY"))
 def context(self):return {"evidence":[e.model_dump() for e in self.evidence.values()],"claims":[c.model_dump() for c in self.claims.values()],"edges":self.edges}
