from fastapi import FastAPI
from app.api.routes.analyze import router

app = FastAPI(title="AI Log Analyzer")

app.include_router(router)  