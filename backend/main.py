from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.core.config import settings
from backend.api import routes_agent
from backend.api import routes_voice
from backend.api import routes_vision
from backend.api import routes_auto

app = FastAPI(
    title=settings.PROJECT_NAME,
    version="1.0.0",
    description="Backend for the Nova Clinical Companion App"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Welcome to the Nova Clinical Companion API. Visit /docs to test endpoints."}

@app.get("/health")
async def health_check():
    return {"status": "ok", "message": "API is running smoothly."}

# Registering ALL API routes mapped to Hackathon categories
app.include_router(routes_agent.router, prefix="/api/agent", tags=["Agentic Reasoning (Nova Lite)"])
app.include_router(routes_voice.router, prefix="/api/voice", tags=["Voice AI (Nova Sonic)"])
app.include_router(routes_vision.router, prefix="/api/vision", tags=["Multimodal (Nova Vision)"])
app.include_router(routes_auto.router, prefix="/api/auto", tags=["UI Automation (Nova Act)"])