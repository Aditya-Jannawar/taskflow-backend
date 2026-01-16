from fastapi import FastAPI
from app.routers import health, tasks

app = FastAPI(title="TaskFlow Backend")

app.include_router(health.router)
app.include_router(tasks.router)
