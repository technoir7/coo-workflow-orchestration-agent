from sqlalchemy import String, ForeignKey
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, mapped_column
import uuid

from .base import Base, UUIDMixin, TimestampMixin

class AuditLog(Base, UUIDMixin, TimestampMixin):
    __tablename__ = "audit_logs"

    trace_id: Mapped[uuid.UUID] = mapped_column(uuid.UUID(as_uuid=True), nullable=False)
    actor_id: Mapped[uuid.UUID] = mapped_column(uuid.UUID(as_uuid=True), nullable=True)
    event_type: Mapped[str] = mapped_column(String(100), nullable=False)
    resource_type: Mapped[str] = mapped_column(String(50), nullable=True)
    resource_id: Mapped[uuid.UUID] = mapped_column(uuid.UUID(as_uuid=True), nullable=True)
    before_state: Mapped[dict] = mapped_column(JSONB, nullable=True)
    after_state: Mapped[dict] = mapped_column(JSONB, nullable=True)
    metadata_: Mapped[dict] = mapped_column("metadata", JSONB, nullable=True) # metadata is a reserved keyword in some contexts, explicit name
