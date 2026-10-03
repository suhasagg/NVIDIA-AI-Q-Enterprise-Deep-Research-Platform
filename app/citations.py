def citation_map(evidence):return {e.id:e for e in evidence}
def validate_claims(claims,evidence):
 ids={e.id for e in evidence};return [{"claim_id":c.id,"valid":bool(c.evidence_ids) and all(x in ids for x in c.evidence_ids)} for c in claims]
