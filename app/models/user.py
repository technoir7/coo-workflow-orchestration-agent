from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
import uuid

from .base import Base, UUIDMixin, TimestampMixin

class User(Base, UUIDMixin, TimestampMixin):
    __tablename__ = "users"

    org_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("organizations.id"), nullable=False)
    email: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)
    role: Mapped[str] = mapped_column(String(50), nullable=False)  # 'ADMIN', 'APPROVER', 'VIEWER'
    full_name: Mapped[str] = mapped_column(String(255), nullable=True)

    organization: Mapped["Organization"] = relationship(back_populates="users")
