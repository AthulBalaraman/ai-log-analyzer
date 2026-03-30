from fastapi import APIRouter
from app.schemas.log_schema import LogRequest
from app.services.ai_service import analyze_logs

router = APIRouter()

@router.post("/analyze")
async def analyze(req: LogRequest):
    result = await analyze_logs(req.logs)
    return {"result": result}