from fastapi import APIRouter,Depends
from app.security import auth
from app.domain import ResearchRequest
from app.runtime import ResearchRuntime
from app.model_router import ModelRouter
router=APIRouter(prefix="/v1",dependencies=[Depends(auth)])
@router.post("/research")
async def research(r:ResearchRequest):return await ResearchRuntime().run(r)
@router.get("/models/routes")
async def routes():return {r:ModelRouter().route(r) for r in ["intent","shallow","planner","researcher","writer","critic"]}
