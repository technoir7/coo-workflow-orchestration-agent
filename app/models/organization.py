from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List

from .base import Base, UUIDMixin, TimestampMixin

class Organization(Base, UUIDMixin, TimestampMixin):
    __tablename__ = "organizations"

    name: Mapped[str] = mapped_column(String(255), nullable=False)
    
    users: Mapped[List["User"]] = relationship(back_populates="organization")
    integration_accounts: Mapped[List["IntegrationAccount"]] = relationship(back_populates="organization")
    policies: Mapped[List["Policy"]] = relationship(back_populates="organization")
    work_items: Mapped[List["WorkItem"]] = relationship(back_populates="organization")
