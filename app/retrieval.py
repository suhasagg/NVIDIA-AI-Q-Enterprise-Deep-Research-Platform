from datetime import datetime,timezone
import hashlib
from app.domain import Evidence
class HybridRetriever:
 async def search(self,query:str,source_types:list[str],tenant_id:str,allowed:list[str]):
  out=[]
  for s in source_types:
   if s not in allowed:continue
   key=hashlib.sha256(f"{s}:{query}".encode()).hexdigest()[:12]
   if s=="enterprise":
    out.append(Evidence(id=key,source_type=s,uri=f"enterprise://authorized/{key}",title="Authorized enterprise evidence",snippet=f"Reference enterprise evidence for '{query}'. Replace mock mode with deployment-owned RAG/search connector.",retrieved_at=datetime.now(timezone.utc).isoformat(),authority=.8,freshness=.7,relevance=.8))
   elif s=="web":
    out.append(Evidence(id=key,source_type=s,uri=f"web://source/{key}",title="Public research evidence",snippet=f"Reference public evidence for '{query}'. Replace mock mode with approved web/paper search provider.",retrieved_at=datetime.now(timezone.utc).isoformat(),authority=.7,freshness=.8,relevance=.8))
  return out
