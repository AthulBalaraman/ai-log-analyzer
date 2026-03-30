from pydantic import BaseModel

class LogRequest(BaseModel):
    logs: str

class LogResponse(BaseModel):
    log_type: str
    attack_type: str
    summary: str
    suspicious_activity: str
    risk_level: str
    confidence_score: int
    suggested_action: str