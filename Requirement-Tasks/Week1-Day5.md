Week 1 – Day 5: Implement GET /jobs Endpoint (Fetch All Jobs)
🎯 Objective
Implement a public GET /jobs API to retrieve all job applications from the database, using service and CRUD layers. Response should return clean Pydantic objects, sorted by applied_date (descending).

📌 Task 1: Create get_all_jobs() in crud.py
Type: Database Logic
Priority: High
Time Estimate: 15 min

✅ To-Do:
 Open sql/crud.py

 Add:

python
Copy
Edit
def get_all_jobs(db: Session):
    return db.query(models.Job).order_by(models.Job.applied_date.desc()).all()
 Commit:

bash
Copy
Edit
git add sql/crud.py
git commit -m "Add get_all_jobs function to fetch all jobs from DB"
📌 Task 2: Create get_jobs_service() in job_service.py
Type: Business Logic
Priority: High
Time Estimate: 10 min

✅ To-Do:
 Open services/job_service.py

 Add:

python
Copy
Edit
def get_jobs_service(db: Session):
    return get_all_jobs(db)
 Commit:

bash
Copy
Edit
git add services/job_service.py
git commit -m "Add service function to get all jobs"
📌 Task 3: Build GET /jobs in Routes
Type: API Endpoint
Priority: Highest
Time Estimate: 20 min

✅ To-Do:
 Open routes/job_routes.py

 Add:

python
Copy
Edit
from typing import List

@router.get("/", response_model=List[JobOut])
def get_jobs(db: Session = Depends(get_db)):
    return get_jobs_service(db)
 Commit:

bash
Copy
Edit
git add routes/job_routes.py
git commit -m "Implement GET /jobs route to fetch all job entries"
📌 Task 4: Manually Test in Swagger or Postman
Type: Manual Testing
Priority: High
Time Estimate: 15–20 min

✅ To-Do:
 Open Swagger UI: http://localhost:8000/docs

 Call GET /jobs with no parameters

 Confirm:

HTTP 200 OK

Response is a list of job objects

Objects are sorted by applied_date (latest first)

 Also test in Postman or CURL (optional)

📌 Task 5 (Optional): Add Pagination Placeholder (Prep for Future)
Type: Architecture Improvement
Priority: Optional
Time Estimate: 10 min

✅ To-Do:
 Add placeholder comment in get_jobs_service():

python
Copy
Edit
# TODO: Add pagination (limit, offset) in Week 2
 Also mention it in README.md or docs/mvp.md under “Future Enhancements”

 Commit:

bash
Copy
Edit
git commit -am "Add TODO for pagination support"
✅ Day 5 Summary Checklist
Task	Description	Status
📦 CRUD logic added	get_all_jobs() in crud.py	[ ]
🧩 Service layer wired	get_jobs_service() in job_service.py	[ ]
🔌 Route built	GET /jobs endpoint in job_routes.py	[ ]
🧪 Tested manually	Swagger confirms response with job list	[ ]
🧠 Pagination note added	# TODO for future paging support	[ ]
📘 Git commits	All commits done in modular steps	[ ]

