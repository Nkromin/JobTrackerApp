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