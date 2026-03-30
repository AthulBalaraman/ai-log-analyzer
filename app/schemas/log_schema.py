from pydantic import BaseModel

class LogRequest(BaseModel):
    logs: str

class LogResponse(BaseModel):
    summary: str
    suspicious_activity: str
    risk_level: str
    suggested_action: str