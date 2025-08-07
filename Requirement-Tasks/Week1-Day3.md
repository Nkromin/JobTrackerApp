Week 1 – Day 3: Define Pydantic Schemas for Job Entity
🎯 Objective
Create all necessary Pydantic models in schemas.py to validate and structure request/response data for the Job entity. These schemas will be used in the API endpoints and service layer.

📌 Task 1: Install Pydantic (If Needed)
Type: Dependency Check
Priority: High
Time Estimate: 5 min

✅ To-Do:
 Confirm pydantic is installed:

bash
Copy
Edit
pip show pydantic
 If not installed:

bash
Copy
Edit
pip install pydantic
pip freeze > requirements.txt
git commit -am "Install pydantic for schema validation"
📌 Task 2: Create and Structure schemas.py
Type: Development
Priority: Highest
Time Estimate: 25–30 min

✅ To-Do:
 Open or create sql/schemas.py

 Import:

python
Copy
Edit
from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from enum import Enum
 Define enum (matching JobStatus from models.py):

python
Copy
Edit
class JobStatus(str, Enum):
    applied = "applied"
    interviewing = "interviewing"
    offered = "offered"
    rejected = "rejected"
 Create JobBase schema:

python
Copy
Edit
class JobBase(BaseModel):
    title: str
    company: str
    status: JobStatus = JobStatus.applied
    applied_date: datetime
    notes: Optional[str] = None
 Create JobCreate schema:

python
Copy
Edit
class JobCreate(JobBase):
    pass  # same as JobBase
 Create JobUpdate schema (all optional for PATCH-style update):

python
Copy
Edit
class JobUpdate(BaseModel):
    title: Optional[str]
    company: Optional[str]
    status: Optional[JobStatus]
    applied_date: Optional[datetime]
    notes: Optional[str]
 Create JobOut schema (what is returned from API):

python
Copy
Edit
class JobOut(JobBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True  # VERY important for SQLAlchemy → Pydantic conversion
 Add docstrings to each class (optional but professional)

 Commit:

bash
Copy
Edit
git add sql/schemas.py
git commit -m "Define Pydantic schemas for Job entity"
📌 Task 3: Verify Schema Functionality (Mini Manual Test)
Type: Testing / Learning
Priority: Medium
Time Estimate: 10 min

✅ To-Do:
 Open a scratch script or Python shell

 Import and try:

python
Copy
Edit
from sql.schemas import JobCreate, JobStatus
from datetime import datetime

job = JobCreate(
    title="Backend Engineer",
    company="Stripe",
    status=JobStatus.applied,
    applied_date=datetime.utcnow()
)

print(job.json())
 Confirm schema works and returns correct JSON

📌 Task 4: Add Example Payloads (Optional but Helpful)
Type: Documentation
Priority: Optional
Time Estimate: 10 min

✅ To-Do:
 Add sample job payload to README.md or new file docs/sample_payloads.md

json
Copy
Edit
{
  "title": "Software Developer",
  "company": "Google",
  "status": "interviewing",
  "applied_date": "2025-08-01T00:00:00Z",
  "notes": "Had recruiter call on 5th Aug"
}
 Commit:

bash
Copy
Edit
git add docs/sample_payloads.md
git commit -m "Add sample job payload for testing"
✅ Day 3 Summary Checklist
Task	Description	Status
🧩 Enum created	JobStatus enum in Pydantic	[ ]
📦 Request schemas	JobBase, JobCreate, JobUpdate	[ ]
📤 Response schema	JobOut with orm_mode = True	[ ]
🧪 Manual test done	Schema object tested in REPL/script	[ ]
📝 Payload doc (optional)	Example added to /docs	[ ]
📘 Git commits	All schema changes committed	[ ]
