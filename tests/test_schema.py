from sql.schemas import JobCreate, JobStatus
from datetime import datetime

job = JobCreate(
    title="Backend Engineer",
    company="Stripe",
    status=JobStatus.applied,
    applied_date=datetime.utcnow()
)

print(job.json(indent=2))  # Pretty-print the JSON
