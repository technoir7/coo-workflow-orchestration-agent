from fastapi import FastAPI
from app.api.router import router as api_router

app = FastAPI(
    title="COO Workflow Agent",
    version="0.1.0", 
    description="Bounded, semi-autonomous workflow control tower"
)

app.include_router(api_router, prefix="/api/v1")

@app.get("/health")
async def health_check():
    return {"status": "ok", "version": "0.1.0"}
