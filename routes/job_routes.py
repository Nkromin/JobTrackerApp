from fastapi import APIRouter

job_routes = APIRouter()

@job_routes.get("/jobs")
def get_jobs():
    return {"message": "Jobs route working!"}
