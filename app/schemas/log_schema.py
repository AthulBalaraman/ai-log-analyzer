from pydantic import BaseModel, Field
from typing import List

class LogRequest(BaseModel):
    logs: List[str]

class LogResponse(BaseModel):
    log_type: str
    attack_type: str
    summary: str
    suspicious_activity: str
    risk_level: str
    confidence_score: int = Field(..., ge=0, le=100)
    suggested_action: str    

class BatchLogResponse(BaseModel):
    overall_risk: str
    average_confidence: float
    total_logs: int
    analysis: List[LogResponse]
    plan: List[dict] = []
    actions_taken: List[str] = []