def evaluate(report,validations,contradictions,budget):
 coverage=sum(1 for v in validations if v["valid"])/max(1,len(validations))
 return {"decision":"PASS" if coverage==1 else "RERESEARCH","citation_coverage":coverage,"contradiction_count":len(contradictions),"budget":budget.snapshot()}
