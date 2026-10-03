from fastapi import FastAPI
from app.api import router
from app.db import Base,engine
app=FastAPI(title="NVIDIA AI-Q Enterprise Deep Research Platform Reference")
app.include_router(router)
@app.on_event("startup")
async def start():
 async with engine.begin() as c:await c.run_sync(Base.metadata.create_all)
@app.get("/health")
async def health():return {"status":"ok"}
