from fastapi import APIRouter, HTTPException, BackgroundTasks, Depends
from typing import List, Optional
from datetime import datetime
from pydantic import BaseModel, HttpUrl

from app.schemas.work_item import NormalizedWorkItem
from app.workflows.states import IngestionState

router = APIRouter()

# --- Schemas for API Requests ---
class ConnectIntegrationRequest(BaseModel):
    provider: str # 'LINEAR' or 'SLACK'
    auth_code: str
    
class MeetingNotesRequest(BaseModel):
    notes_text: str
    metadata: dict

# --- Endpoints ---

@router.post("/integrations/connect")
async def connect_integration(request: ConnectIntegrationRequest):
    """Authenticate and connect a third-party tool"""
    # Logic to exchange auth_code for token and store in IntegrationAccount
    return {"status": "connected", "provider": request.provider}

@router.get("/workitems", response_model=List[NormalizedWorkItem])
async def list_work_items(
    status: Optional[str] = None, 
    assignee_id: Optional[str] = None
):
    """List normalized work items with filtering"""
    # Logic to query DB
    return []

@router.get("/workitems/{id}", response_model=NormalizedWorkItem)
async def get_work_item(id: str):
    """Get details of a specific work item"""
    # Logic to get from DB
    raise HTTPException(status_code=404, detail="Item not found")

@router.get("/exceptions")
async def list_exceptions(status: str = "OPEN"):
    """List active policy violations"""
    return []

@router.post("/approvals/{draft_id}")
async def approve_action(draft_id: str, decision: str): # decision: APPROVED / REJECTED
    """Human approval for an automated action draft"""
    # Logic to update ActionDraft status and trigger execution workflow
    return {"draft_id": draft_id, "status": decision}

@router.post("/meetings/ingest")
async def ingest_meeting_notes(request: MeetingNotesRequest, background_tasks: BackgroundTasks):
    """Upload meeting notes for task extraction"""
    # Logic to queue extraction workflow
    return {"status": "queued", "job_id": "123"}

@router.get("/workflows/{id}")
async def get_workflow_status(id: str):
    """Get execution status of a background workflow"""
    return {"id": id, "status": "RUNNING"}
