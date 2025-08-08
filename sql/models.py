import enum

class JobStatus(str, enum.Enum):
    applied = "applied"
    interviewing = "interviewing"
    offered = "offered"
    rejected = "rejected"

#Define Job ORM model:

from sqlalchemy import Column, Integer, String, DateTime, Enum, Text
from datetime import datetime
from sql.database import Base
from .models import JobStatus  # if enum is separated

class Job(Base):
    _tablename_ = "jobs"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    company = Column(String, nullable=False)
    status = Column(Enum(JobStatus), nullable=False, default="applied")
    applied_date = Column(DateTime, nullable=False)
    notes = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
