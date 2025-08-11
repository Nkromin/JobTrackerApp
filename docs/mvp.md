# MVP – Job Tracker API

## Job Model
- id: int
- title: str
- company: str
- status: enum (applied, interviewing, offered, rejected)
- applied_date: date
- notes: Optional[str]

## API Endpoints
- GET /jobs
- GET /jobs/{id}
- POST /jobs
- PUT /jobs/{id}
- DELETE /jobs/{id}

[ ] Optional future features: user auth, reminders, resume parsing
