from abc import ABC, abstractmethod
from typing import List, Optional
from pydantic import BaseModel, Field

class NudgeDraft(BaseModel):
    message: str = Field(..., description="The drafted slack message")
    tone: str = Field(..., description="The tone of the message")
    confidence: float = Field(..., description="Confidence score 0.0-1.0")

class MeetingTask(BaseModel):
    title: str
    assignee: str
    due_date: str

class LLMInterface(ABC):
    @abstractmethod
    def summarize_work_history(self, work_item_context: dict) -> str:
        """Summarize history efficiently"""
        pass
        
    @abstractmethod
    def draft_nudge(self, context: dict) -> NudgeDraft:
        """Draft a nudge message with confidence score"""
        pass
        
    @abstractmethod
    def extract_tasks(self, meeting_notes: str) -> List[MeetingTask]:
        """Extract tasks from unstructured notes"""
        pass

class GeminiLLMService(LLMInterface):
    def __init__(self, api_key: str):
        self.api_key = api_key
        # Initialize Gemini client here
        
    def summarize_work_history(self, work_item_context: dict) -> str:
        # Placeholder for actual implementation
        return "Summary placeholder"
        
    def draft_nudge(self, context: dict) -> NudgeDraft:
        # Placeholder
        # In real impl, use structured prompting
        return NudgeDraft(
            message="Hey, just checking in on this task.",
            tone="neutral",
            confidence=0.9
        )
        
    def extract_tasks(self, meeting_notes: str) -> List[MeetingTask]:
        # Placeholder
        return []
