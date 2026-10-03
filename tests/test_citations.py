from app.domain import Evidence,Claim
from app.citations import validate_claims
def test_citation():
 e=Evidence(id="e",source_type="web",uri="u",title="t",snippet="s",retrieved_at="now")
 assert validate_claims([Claim(id="c",text="x",evidence_ids=["e"])],[e])[0]["valid"]
