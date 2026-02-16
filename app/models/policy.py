from sqlalchemy import String, ForeignKey, Boolean
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, mapped_column, relationship
import uuid

from .base import Base, UUIDMixin, TimestampMixin

class Policy(Base, UUIDMixin, TimestampMixin):
    __tablename__ = "policies"

    org_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("organizations.id"), nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    trigger_event: Mapped[str] = mapped_column(String(100), nullable=False)
    rules: Mapped[dict] = mapped_column(JSONB, nullable=False)
    actions: Mapped[dict] = mapped_column(JSONB, nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)

    organization: Mapped["Organization"] = relationship(back_populates="policies")
    exceptions: Mapped[list["Exception"]] = relationship(back_populates="policy")
