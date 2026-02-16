from sqlalchemy import String, ForeignKey, DateTime, Float
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
import uuid

from .base import Base, UUIDMixin, TimestampMixin

class Exception(Base, UUIDMixin, TimestampMixin):
    __tablename__ = "exceptions"

    work_item_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("work_items.id"), nullable=False)
    policy_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("policies.id"), nullable=False)
    type: Mapped[str] = mapped_column(String(100), nullable=False)  # 'STALL', 'SLA_RISK'
    severity: Mapped[str] = mapped_column(String(50), nullable=False)
    status: Mapped[str] = mapped_column(String(50), default='OPEN')  # 'OPEN', 'RESOLVED', 'IGNORED'

    work_item: Mapped["WorkItem"] = relationship(back_populates="exceptions")
    policy: Mapped["Policy"] = relationship(back_populates="exceptions")
    action_drafts: Mapped[list["ActionDraft"]] = relationship(back_populates="exception")


class ActionDraft(Base, UUIDMixin, TimestampMixin):
    __tablename__ = "action_drafts"

    exception_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("exceptions.id"), nullable=False)
    proposed_action: Mapped[str] = mapped_column(String(100), nullable=False)  # 'SEND_SLACK_MSG'
    payload: Mapped[dict] = mapped_column(JSONB, nullable=False)
    status: Mapped[str] = mapped_column(String(50), default='PENDING_APPROVAL')  # 'PENDING_APPROVAL', 'APPROVED', 'REJECTED'
    generated_reason: Mapped[str] = mapped_column(String, nullable=True)
    confidence_score: Mapped[float] = mapped_column(Float, nullable=True)

    exception: Mapped["Exception"] = relationship(back_populates="action_drafts")
    executions: Mapped[list["ActionExecution"]] = relationship(back_populates="draft")


class ActionExecution(Base, UUIDMixin, TimestampMixin):
    __tablename__ = "action_executions"

    draft_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("action_drafts.id"), nullable=False)
    executed_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=datetime.now().isoformat())
    result_status: Mapped[str] = mapped_column(String(50))  # 'SUCCESS', 'FAILURE'
    external_reference_id: Mapped[str] = mapped_column(String(255), nullable=True)

    draft: Mapped["ActionDraft"] = relationship(back_populates="executions")
