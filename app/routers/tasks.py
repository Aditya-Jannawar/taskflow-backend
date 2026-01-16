from fastapi import APIRouter, HTTPException


router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"]
)

# temporary in-memory storage
tasks = [
    {
        "id": 1,
        "title": "Setup project structure",
        "status": "todo"
    }
]


@router.get("/")
def get_all_tasks():
    return tasks


@router.get("/{task_id}")
def get_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            return task
    raise HTTPException(status_code=404, detail="Task not found")

