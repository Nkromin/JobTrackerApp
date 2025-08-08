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