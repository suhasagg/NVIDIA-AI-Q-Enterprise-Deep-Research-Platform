from pydantic import BaseModel,Field
from typing import Any,Literal
class ResearchRequest(BaseModel):
 tenant_id:str="enterprise";principal_id:str="researcher@example";goal:str
 mode:Literal["auto","shallow","deep"]="auto";allowed_sources:list[str]=Field(default_factory=lambda:["enterprise","web"])
 context:dict[str,Any]=Field(default_factory=dict)
class ResearchTask(BaseModel):
 key:str;question:str;source_types:list[str]=Field(default_factory=list);depends_on:list[str]=Field(default_factory=list)
 priority:int=1
class ResearchPlan(BaseModel):
 objective:str;tasks:list[ResearchTask];success_criteria:list[str]=Field(default_factory=list)
class Evidence(BaseModel):
 id:str;source_type:str;uri:str;title:str;snippet:str;retrieved_at:str
 authority:float=0.5;freshness:float=0.5;relevance:float=0.5;access_scope:str="tenant"
 metadata:dict[str,Any]=Field(default_factory=dict)
class Claim(BaseModel):
 id:str;text:str;evidence_ids:list[str]=Field(default_factory=list);confidence:float=0.0
class ResearchReport(BaseModel):
 title:str;summary:str;claims:list[Claim];citations:dict[str,Evidence];limitations:list[str]=Field(default_factory=list)
