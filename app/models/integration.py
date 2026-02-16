from sqlalchemy import String, ForeignKey
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, mapped_column, relationship
import uuid

from .base import Base, UUIDMixin, TimestampMixin

class IntegrationAccount(Base, UUIDMixin, TimestampMixin):
    __tablename__ = "integration_accounts"

    org_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("organizations.id"), nullable=False)
    provider: Mapped[str] = mapped_column(String(50), nullable=False)  # 'LINEAR', 'SLACK'
    config: Mapped[dict] = mapped_column(JSONB, default={}, nullable=False)
    status: Mapped[str] = mapped_column(String(50), default='ACTIVE', nullable=False)

    organization: Mapped["Organization"] = relationship(back_populates="integration_accounts")
