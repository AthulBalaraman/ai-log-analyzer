from fastapi import APIRouter
from app.schemas.log_schema import LogRequest
from app.services.ai_service import analyze_logs_batch

router = APIRouter()

@router.post("/analyze")
async def analyze(req: LogRequest):
    result = await analyze_logs_batch(req.logs)
    return {"result": result}