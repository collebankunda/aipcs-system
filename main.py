
from fastapi import FastAPI
from routes import project_routes

app = FastAPI()
app.include_router(project_routes.router, prefix="/api/projects")

@app.get("/")
def root():
    return {"message": "Welcome to AIPCS API"}
