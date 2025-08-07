Week 1 – Day 1: Project Initialization & FastAPI Bootstrapping

🎯 Objective

Kickstart the Job Tracker API project with a working FastAPI server, Git version control, clean project structure, and clear MVP planning.


---

📌 Task 1: Set Up Project Environment

Type: Development
Priority: Highest
Time Estimate: 30 min

✅ To-Do:

[ ] Open terminal and navigate to workspace directory

[ ] Create project directory

mkdir job-tracker-api && cd job-tracker-api

[ ] Create virtual environment

python -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate

[ ] Install initial dependencies

pip install fastapi uvicorn
pip freeze > requirements.txt

[ ] Create .gitignore file with:

venv/
_pycache_/
.env
.DS_Store

[ ] Initialize Git repository

git init
git add .
git commit -m "Initialize FastAPI project environment"



---

📌 Task 2: Define Project Structure

Type: Development
Priority: High
Time Estimate: 20 min

✅ To-Do:

[ ] Create top-level folders:

routes/

services/

sql/


[ ] Inside sql/, create:

[ ] crud.py

[ ] database.py

[ ] models.py

[ ] schemas.py


[ ] Create main app entry point:

[ ] app/main.py


[ ] Optional: add placeholder files with # TODO: implement at top

[ ] Commit:

git add .
git commit -m "Create initial project structure with folders and empty modules"



---

📌 Task 3: Create and Run FastAPI App

Type: Development
Priority: High
Time Estimate: 20 min

✅ To-Do:

[ ] Open app/main.py

[ ] Add basic FastAPI server:

from fastapi import FastAPI

app = FastAPI(title="Job Tracker API")

@app.get("/")
def root():
    return {"message": "Welcome to the Job Tracker API"}

[ ] Run the app:

uvicorn app.main:app --reload

[ ] Visit in browser:

[ ] http://127.0.0.1:8000 → Should show welcome message

[ ] http://127.0.0.1:8000/docs → Swagger UI loads


[ ] Commit:

git add app/main.py
git commit -m "Add working FastAPI app with root route"



---

📌 Task 4: Document MVP Features & API Plan

Type: Planning / Documentation
Priority: Medium
Time Estimate: 30 min

✅ To-Do:

[ ] Create docs/ folder

[ ] Create docs/mvp.md

[ ] List MVP features:

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

[ ] Commit:

git add docs/mvp.md
git commit -m "Add MVP feature plan and initial API route outline"



---

📌 Task 5: Create and Write Project README

Type: Documentation
Priority: Medium
Time Estimate: 15 min

✅ To-Do:

[ ] Create README.md

[ ] Add:

# Job Tracker API

A FastAPI backend for tracking job applications.

## Tech Stack
- FastAPI
- SQLAlchemy
- PostgreSQL (or SQLite)
- Docker (later)

## Setup Instructions
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload

Routes

GET / → Welcome




[ ] Commit:

git add README.md
git commit -m "Add initial README with setup and project intro"



---

📌 Task 6: Learning Assignment – FastAPI Basics

Type: Learning
Priority: Medium
Time Estimate: 30–40 min

✅ To-Do:

[ ] Read: FastAPI Tutorial – First Steps

[ ] Watch: FastAPI Crash Course – Traversy Media

[ ] Create: docs/day1-learnings.md

[ ] Write at least 5 key takeaways about:

FastAPI design

Auto documentation

Path vs query params

Type hinting and validation


[ ] Commit:

git add docs/day1-learnings.md
git commit -m "Add Day 1 FastAPI learning notes"



---

✅ Day 1 Summary Checklist

Task	Description	Status

🛠️ Environment setup	Python, venv, packages installed	[ ]
📁 Folder structure	All required folders/files created	[ ]
🚀 FastAPI booted	Root / endpoint working in Swagger	[ ]
📋 MVP defined	docs/mvp.md written	[ ]
📘 README created	With project setup instructions	[ ]
🧠 FastAPI basics learned	Notes written + committed	[ ]