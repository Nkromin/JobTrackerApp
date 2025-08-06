Week 1 – Day 4: Implement POST /jobs Endpoint (Create Job)
🎯 Objective
Build the backend flow for creating a new Job entry via POST /jobs using FastAPI, SQLAlchemy, and your existing Pydantic schemas.

📌 Task 1: Implement create_job() in crud.py
Type: Database Logic
Priority: Highest
Time Estimate: 20 min

✅ To-Do:
 Open sql/crud.py

 Add:

python
Copy
Edit
from sqlalchemy.orm import Session
from sql import models, schemas
from datetime import datetime

def create_job(db: Session, job: schemas.JobCreate):
    db_job = models.Job(
        title=job.title,
        company=job.company,
        status=job.status,
        applied_date=job.applied_date,
        notes=job.notes,
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow(),
    )
    db.add(db_job)
    db.commit()
    db.refresh(db_job)
    return db_job
 Commit:

bash
Copy
Edit
git add sql/crud.py
git commit -m "Add create_job function in CRUD layer"
📌 Task 2: Implement create_job_service() in services Layer
Type: Business Logic
Priority: High
Time Estimate: 10 min

✅ To-Do:
 Create file: services/job_service.py (if not already created)

 Add:

python
Copy
Edit
from sqlalchemy.orm import Session
from sql import schemas
from sql.crud import create_job

def create_job_service(db: Session, job: schemas.JobCreate):
    return create_job(db, job)
 Commit:

bash
Copy
Edit
git add services/job_service.py
git commit -m "Add job creation service layer"
📌 Task 3: Build POST /jobs in Routes
Type: API Endpoint
Priority: Highest
Time Estimate: 25 min

✅ To-Do:
 Create file: routes/job_routes.py

 Add:

python
Copy
Edit
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from sql.schemas import JobCreate, JobOut
from services.job_service import create_job_service
from sql.database import SessionLocal

router = APIRouter(prefix="/jobs", tags=["Jobs"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=JobOut, status_code=status.HTTP_201_CREATED)
def create_job(job: JobCreate, db: Session = Depends(get_db)):
    return create_job_service(db, job)
 Commit:

bash
Copy
Edit
git add routes/job_routes.py
git commit -m "Create POST /jobs route for job creation"
📌 Task 4: Plug Route into FastAPI App
Type: Routing Integration
Priority: High
Time Estimate: 5 min

✅ To-Do:
 Open main.py

 Register router:

python
Copy
Edit
from routes import job_routes

app.include_router(job_routes.router)
 Restart server:

bash
Copy
Edit
uvicorn app.main:app --reload
 Visit Swagger: http://127.0.0.1:8000/docs

 Confirm POST /jobs is visible

 Commit:

bash
Copy
Edit
git add app/main.py
git commit -m "Register job routes in main app"
📌 Task 5: Test Endpoint in Swagger or Postman
Type: Manual Testing
Priority: High
Time Estimate: 20 min

✅ To-Do:
 Open Swagger UI: http://localhost:8000/docs

 Use the POST /jobs route with payload:

json
Copy
Edit
{
  "title": "Backend Developer",
  "company": "PayPal",
  "status": "applied",
  "applied_date": "2025-08-01T00:00:00Z",
  "notes": "Reached out to recruiter on LinkedIn"
}
 Confirm response:

HTTP 201 Created

Response body contains ID and timestamps

 Check DB (via pgAdmin or CLI) to confirm record was inserted

📌 Task 6 (Optional): Add Response Examples to Swagger
Type: Documentation
Priority: Optional
Time Estimate: 10 min

✅ To-Do:
 Add example to schema:

python
Copy
Edit
class JobCreate(BaseModel):
    title: str = Field(..., example="Software Engineer")
    company: str = Field(..., example="Meta")
    status: JobStatus = Field(default=JobStatus.applied, example="applied")
    applied_date: datetime = Field(..., example="2025-08-01T00:00:00Z")
    notes: Optional[str] = Field(None, example="Reached out via email")
 Swagger docs now show example payload auto-filled.

✅ Day 4 Summary Checklist
Task	Description	Status
🧱 CRUD function added	create_job() in crud.py	[ ]
🔄 Service layer ready	create_job_service() in job_service.py	[ ]
🚀 Route built	POST /jobs in job_routes.py	[ ]
🧩 Route plugged in	Registered in main.py	[ ]
🧪 Manual test done	Swagger or Postman tested	[ ]
📝 Swagger example (optional)	Field examples added	[ ]
📘 Git commits	Each layer committed separately	[ ]

