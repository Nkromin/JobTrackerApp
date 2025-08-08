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

