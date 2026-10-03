def detect(evidence):
 groups={}
 for e in evidence:
  groups.setdefault(e.title.lower(),[]).append(e)
 return [{"topic":k,"evidence_ids":[x.id for x in v],"status":"REVIEW"} for k,v in groups.items() if len(v)>1 and len({x.snippet for x in v})>1]
