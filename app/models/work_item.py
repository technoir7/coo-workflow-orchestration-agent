from sqlalchemy import String, ForeignKey, DateTime, UniqueConstraint
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
import uuid

from .base import Base, UUIDMixin, TimestampMixin

class WorkItem(Base, UUIDMixin, TimestampMixin):
    __tablename__ = "work_items"

    org_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("organizations.id"), nullable=False)
    source_system: Mapped[str] = mapped_column(String(50), nullable=False)
    source_id: Mapped[str] = mapped_column(String(255), nullable=False)
    title: Mapped[str] = mapped_column(String, nullable=False) # Changed to Text -> String
    status: Mapped[str] = mapped_column(String(100), nullable=False)
    assignee_id: Mapped[str] = mapped_column(String(255), nullable=True)
    priority: Mapped[str] = mapped_column(String(50), nullable=True)
    due_date: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=True)
    sla_deadline: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=True)
    last_activity_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=True)
    tags: Mapped[list] = mapped_column(JSONB, default=[], nullable=True)
    raw_data: Mapped[dict] = mapped_column(JSONB, nullable=True)
    hash: Mapped[str] = mapped_column(String(64), nullable=True)

    organization: Mapped["Organization"] = relationship(back_populates="work_items")
    exceptions: Mapped[list["Exception"]] = relationship(back_populates="work_item")

    __table_args__ = (
        UniqueConstraint('org_id', 'source_system', 'source_id', name='uq_work_item_source'),
    )
