from sqlalchemy.orm import declarative_base
import datetime
import uuid
from sqlalchemy import Date, ForeignKey
from sqlalchemy import Integer, String
from sqlalchemy.orm import (
    mapped_column,
    Mapped,
    relationship,
)

from sqlalchemy.dialects.postgresql import UUID, DATE
from .base import Base

class Objective(Base):
    __tablename__ = "objectives"
    objectiveId: Mapped[UUID] = mapped_column(UUID, primary_key=True, default=uuid.uuid4)
    objectiveName: Mapped[str] = mapped_column(nullable=False)
    objectiveDescription: Mapped[str] = mapped_column(nullable=True)