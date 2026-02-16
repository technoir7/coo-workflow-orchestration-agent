from typing import List, Optional, Dict, Literal
from datetime import datetime
from pydantic import HttpUrl, Field

from .base import BaseSchema

class NormalizedWorkItem(BaseSchema):
    source_system: Literal["LINEAR", "JIRA", "ASANA"] = Field(..., description="The source task system")
    source_id: str = Field(..., description="The ID in the source system")
    title: str = Field(..., description="Task title")
    status: str = Field(..., description="Normalized status")
    assignee: Optional[Dict[str, str]] = Field(None, description="Assignee details {id, name, email}")
    priority: str = Field("NO_PRIORITY", description="Normalized priority")
    due_date: Optional[datetime] = Field(None, description="Due date")
    sla_deadline: Optional[datetime] = Field(None, description="Calculated SLA deadline")
    last_activity_at: datetime = Field(..., description="Last activity timestamp")
    tags: List[str] = Field(default_factory=list, description="Tags or labels")
    blockers: List[str] = Field(default_factory=list, description="List of blocking item IDs")
    url: Optional[str] = Field(None, description="URL to the task in source system")
