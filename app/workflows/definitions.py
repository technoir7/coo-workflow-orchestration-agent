from typing import Dict, List
from .states import (
    IngestionState,
    StallDetectionState,
    SLAMonitorState,
    ReportGeneratorState,
    MeetingExtractionState
)

class WorkflowStateMachine:
    """
    Defines allowed state transitions for each workflow type.
    Enforces the 'bounded autonomy' constraint by making transitions explicit.
    """
    
    INGESTION_TRANSITIONS: Dict[IngestionState, List[IngestionState]] = {
        IngestionState.FETCHING: [IngestionState.NORMALIZING, IngestionState.FAILED],
        IngestionState.NORMALIZING: [IngestionState.HASHING, IngestionState.FAILED],
        IngestionState.HASHING: [IngestionState.UPSERTING, IngestionState.FAILED],
        IngestionState.UPSERTING: [IngestionState.COMPLETED, IngestionState.FAILED],
        IngestionState.COMPLETED: [],
        IngestionState.FAILED: [IngestionState.FETCHING] # Retry
    }

    STALL_DETECTION_TRANSITIONS: Dict[StallDetectionState, List[StallDetectionState]] = {
        StallDetectionState.CHECKING_POLICIES: [StallDetectionState.DETECTED_STALL, StallDetectionState.SKIPPED],
        StallDetectionState.DETECTED_STALL: [StallDetectionState.CHECKING_COOLDOWN],
        StallDetectionState.CHECKING_COOLDOWN: [StallDetectionState.DRAFTING_NUDGE, StallDetectionState.SKIPPED],
        StallDetectionState.DRAFTING_NUDGE: [StallDetectionState.AWAITING_APPROVAL, StallDetectionState.AUTO_SENDING],
        StallDetectionState.AWAITING_APPROVAL: [StallDetectionState.SENT, StallDetectionState.SKIPPED],
        StallDetectionState.AUTO_SENDING: [StallDetectionState.SENT],
        StallDetectionState.SENT: [],
        StallDetectionState.SKIPPED: []
    }

    SLA_MONITOR_TRANSITIONS: Dict[SLAMonitorState, List[SLAMonitorState]] = {
        SLAMonitorState.CALCULATING_HEADROOM: [SLAMonitorState.RISK_DETECTED, SLAMonitorState.RESOLVED],
        SLAMonitorState.RISK_DETECTED: [SLAMonitorState.ESCALATING],
        SLAMonitorState.ESCALATING: [SLAMonitorState.AWAITING_APPROVAL],
        SLAMonitorState.AWAITING_APPROVAL: [SLAMonitorState.NOTIFYING_MANAGER, SLAMonitorState.RESOLVED],
        SLAMonitorState.NOTIFYING_MANAGER: [SLAMonitorState.RESOLVED],
        SLAMonitorState.RESOLVED: []
    }
    
    # ... mapped similarly for others
