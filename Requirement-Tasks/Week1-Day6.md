Here is your ✅ Week 1 – Day 6 breakdown — a professional, checklist-driven sprint focused on implementing full single-record CRUD for the Job Tracker API:

GET /jobs/{id}

PUT /jobs/{id}

DELETE /jobs/{id}

This completes the entire CRUD set for the Job entity.

✅ Week 1 – Day 6: Implement GET, PUT, DELETE /jobs/{id} (Single Record CRUD)
🎯 Objective
Enable single-record operations for Job entries:

Fetch a job by ID

Update job fields

Delete job entry

These endpoints should return proper status codes (200/404/204) and use service + CRUD layers.

📌 Task 1: Add Single-Record Methods in crud.py
Type: Database Logic
Priority: Highest
Time Estimate: 30 min

✅ To-Do:
 Open sql/crud.py

 Add:

python
Copy
Edit
# Get single job by ID
def get_job_by_id(db: Session, job_id: int):
    return db.query(models.Job).filter(models.Job.id == job_id).first()

# Update job by ID
def update_job(db: Session, job_id: int, job_data: schemas.JobUpdate):
    db_job = get_job_by_id(db, job_id)
    if not db_job:
        return None
    for key, value in job_data.dict(exclude_unset=True).items():
        setattr(db_job, key, value)
    db.commit()
    db.refresh(db_job)
    return db_job

# Delete job by ID
def delete_job(db: Session, job_id: int):
    db_job = get_job_by_id(db, job_id)
    if not db_job:
        return None
    db.delete(db_job)
    db.commit()
    return True
 Commit:

bash
Copy
Edit
git add sql/crud.py
git commit -m "Add get/update/delete job functions to CRUD"
📌 Task 2: Add Service Layer Functions
Type: Business Logic
Priority: High
Time Estimate: 15 min

✅ To-Do:
 Open services/job_service.py

 Add:

python
Copy
Edit
from sql.crud import get_job_by_id, update_job, delete_job

def get_job_service(db: Session, job_id: int):
    return get_job_by_id(db, job_id)

def update_job_service(db: Session, job_id: int, job_data: schemas.JobUpdate):
    return update_job(db, job_id, job_data)

def delete_job_service(db: Session, job_id: int):
    return delete_job(db, job_id)
 Commit:

bash
Copy
Edit
git add services/job_service.py
git commit -m "Add service functions for job fetch/update/delete"
📌 Task 3: Build Routes in job_routes.py
Type: API Endpoint
Priority: Highest
Time Estimate: 30 min

✅ To-Do:
 Open routes/job_routes.py

 Add:

python
Copy
Edit
@router.get("/{job_id}", response_model=JobOut)
def get_job(job_id: int, db: Session = Depends(get_db)):
    job = get_job_service(db, job_id)
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")
    return job

@router.put("/{job_id}", response_model=JobOut)
def update_job(job_id: int, job_data: JobUpdate, db: Session = Depends(get_db)):
    job = update_job_service(db, job_id, job_data)
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")
    return job

@router.delete("/{job_id}", status_code=204)
def delete_job(job_id: int, db: Session = Depends(get_db)):
    deleted = delete_job_service(db, job_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Job not found")
    return
 Commit:

bash
Copy
Edit
git add routes/job_routes.py
git commit -m "Add GET, PUT, DELETE routes for job by ID"
📌 Task 4: Manual Testing via Swagger
Type: QA / Debug
Priority: High
Time Estimate: 20 min

✅ To-Do:
 Open Swagger: http://localhost:8000/docs

 Test:

GET /jobs/{id} – Valid and invalid ID

PUT /jobs/{id} – Update title/status

DELETE /jobs/{id} – Delete job

 Check:

Correct status codes: 200, 204, 404

Empty 204 response for DELETE

404 if job doesn’t exist

 Check DB to confirm updates/deletes

📌 Task 5 (Optional): Improve Error Messages
Type: UX Improvement
Priority: Optional
Time Estimate: 10 min

✅ To-Do:
 Refactor error messages:

python
Copy
Edit
raise HTTPException(status_code=404, detail=f"Job with ID {job_id} not found")
 Optional: Add logging for update/delete failures

✅ Day 6 Summary Checklist
Task	Description	Status
🔎 CRUD added	get/update/delete job by ID	[ ]
🧠 Service layer built	fetch/update/delete wrappers	[ ]
🚀 Routes created	GET, PUT, DELETE /jobs/{id}	[ ]
🧪 Swagger tested	All 3 endpoints verified	[ ]
📘 Git commits	Modular commits for each layer	[ ]
💬 Error UX	404 messages are helpful	[ ]

