from fastapi import FastAPI

from app.routers import health

app = FastAPI(title="TaskFlow Backend")

# include routers
app.include_router(health.router)
