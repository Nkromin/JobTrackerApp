Week 1 – Day 2: PostgreSQL DB Setup & Job Table Creation

🎯 Objective

Connect FastAPI to a PostgreSQL database using SQLAlchemy. Define the Job model as the first table in your app. Tables will be created automatically on server start (Alembic migrations will come later).


---

📌 Task 1: Install DB Dependencies

Type: Development
Priority: Highest
Time Estimate: 10 min

✅ To-Do:

[ ] Install PostgreSQL DB adapter:

pip install psycopg2-binary
pip freeze > requirements.txt

[ ] Commit:

git add requirements.txt
git commit -m "Add psycopg2-binary for PostgreSQL support"



---

📌 Task 2: Prepare PostgreSQL Database

Type: Environment Setup
Priority: Highest
Time Estimate: 15–20 min

✅ To-Do:

[ ] Ensure PostgreSQL is running locally OR use Docker:

docker run --name jobtracker-postgres -e POSTGRES_PASSWORD=postgres -p 5432:5432 -d postgres

[ ] Create a new database:

DB name: jobtracker

Username: postgres

Password: postgres

Port: 5432 (default)


[ ] Optional tool: Use pgAdmin or TablePlus to verify DB creation



---

📌 Task 3: Configure SQLAlchemy DB Connection

Type: Development
Priority: High
Time Estimate: 15 min

✅ To-Do:

[ ] Create or update sql/database.py with:


from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:postgres@localhost/jobtracker"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

[ ] Add comment: "TODO: Move DB credentials to environment variables later"

[ ] Commit:

git add sql/database.py
git commit -m "Configure PostgreSQL database connection using SQLAlchemy"



---

📌 Task 4: Create the Job Table in models.py

Type: Development
Priority: Highest
Time Estimate: 20 min

✅ To-Do:

[ ] Create file: sql/models.py

[ ] Define JobStatus Enum:

import enum

class JobStatus(str, enum.Enum):
    applied = "applied"
    interviewing = "interviewing"
    offered = "offered"
    rejected = "rejected"

[ ] Define Job ORM model:

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

[ ] Commit:

git add sql/models.py
git commit -m "Define Job model with status enum"



---

📌 Task 5: Auto-Create Tables on Server Boot

Type: Development
Priority: High
Time Estimate: 15 min

✅ To-Do:

[ ] Edit main.py:


from fastapi import FastAPI
from sql.database import Base, engine
from sql import models  # Required so models are loaded
from routes import job_routes  # Will be plugged later

app = FastAPI(title="Job Tracker API")

# Create all tables
Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"message": "Welcome to the Job Tracker API"}

[ ] Run the app:

uvicorn app.main:app --reload

[ ] Verify table creation inside PostgreSQL:

\c jobtracker;
\dt

[ ] Commit:

git add app/main.py
git commit -m "Trigger table creation for Job model on server start"



---

📌 Task 6 (Optional): DB Verification via pgAdmin or TablePlus

Type: Debug/Verification
Priority: Optional
Time Estimate: 10 min

✅ To-Do:

[ ] Open your DB client (pgAdmin, DBeaver, or TablePlus)

[ ] Connect to jobtracker database

[ ] Browse tables → Confirm:

jobs exists

All fields match ORM model

status is stored as enum




---

✅ Day 2 Summary Checklist

Task	Description	Status

🧱 psycopg2-binary installed	DB driver installed	[ ]
🧰 PostgreSQL running	Via local or Docker	[ ]
🔗 Connection configured	sql/database.py written	[ ]
📄 Job model created	With enum + timestamps	[ ]
🧪 Tables created	Verified using client or psql	[ ]
📘 Git commits	DB setup committed in steps	[ ]