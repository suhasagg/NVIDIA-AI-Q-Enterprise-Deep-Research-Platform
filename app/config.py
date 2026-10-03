from pydantic_settings import BaseSettings,SettingsConfigDict
class Settings(BaseSettings):
 database_url:str="postgresql+asyncpg://postgres:postgres@localhost:5432/aiq"
 redis_url:str="redis://localhost:6379/0";api_key:str="change-me"
 model_mode:str="mock";source_mode:str="mock"
 nvidia_nim_base_url:str="https://integrate.api.nvidia.com/v1";nvidia_api_key:str=""
 frontier_model_base_url:str="";frontier_model_api_key:str="";mcp_gateway_url:str="http://localhost:8100"
 vector_url:str="http://localhost:6333";opensearch_url:str="http://localhost:9200"
 max_research_loops:int=3;max_tasks:int=12;max_sources:int=40;max_model_calls:int=30;max_tool_calls:int=60;max_budget_usd:float=5.0
 model_config=SettingsConfigDict(env_file=".env",extra="ignore")
settings=Settings()
