# sql/schemas.py

from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from enum import Enum


class JobStatus(str, Enum):
    """
    Enum representing the status of a job application.
    """
    applied = "applied"
    interviewing = "interviewing"
    offered = "offered"
    rejected = "rejected"


class JobBase(BaseModel):
    """
    Base schema for a job application, shared across creation and output.
    """
    title: str
    company: str
    status: JobStatus = JobStatus.applied
    applied_date: datetime
    notes: Optional[str] = None


class JobCreate(JobBase):
    """
    Schema for creating a new job application.
    Inherits all fields from JobBase.
    """
    pass


class JobUpdate(BaseModel):
    """
    Schema for updating a job application (PATCH-style update).
    All fields are optional.
    """
    title: Optional[str]
    company: Optional[str]
    status: Optional[JobStatus]
    applied_date: Optional[datetime]
    notes: Optional[str]


class JobOut(JobBase):
    """
    Schema for job data returned from the API.
    Includes additional read-only fields.
    """
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True  # Enables ORM compatibility with SQLAlchemy models
