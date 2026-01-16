from fastapi import APIRouter, HTTPException, Query

router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"]
)

# In-memory task list (temporary)
tasks = [
    {
        "id": 1,
        "title": "Setup project structure",
        "status": "todo",
        "priority": "high",
        "is_deleted": False,
        "created_by": "system"
    },
    {
        "id": 2,
        "title": "Create health endpoint",
        "status": "done",
        "priority": "medium",
        "is_deleted": False,
        "created_by": "system"
    }
]


@router.get("/")
def get_all_tasks(
    status: str | None = Query(default=None),
    priority: str | None = Query(default=None)
):
    """
    Get all tasks with optional filtering
    """
    result = tasks

    if status:
        result = [t for t in result if t["status"] == status]

    if priority:
        result = [t for t in result if t["priority"] == priority]

    return result


@router.get("/{task_id}")
def get_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id and not task["is_deleted"]:
            return task
    raise HTTPException(status_code=404, detail="Task not found")


@router.post("/")
def create_task(task: dict):
    new_id = max(t["id"] for t in tasks) + 1 if tasks else 1

    new_task = {
        "id": new_id,
        "title": task.get("title"),
        "status": task.get("status", "todo"),
        "priority": task.get("priority", "low"),
        "is_deleted": False,
        "created_by": "system"
    }

    tasks.append(new_task)
    return new_task


@router.put("/{task_id}")
def update_task(task_id: int, updated_task: dict):
    for task in tasks:
        if task["id"] == task_id and not task["is_deleted"]:
            task["title"] = updated_task.get("title", task["title"])
            task["status"] = updated_task.get("status", task["status"])
            task["priority"] = updated_task.get("priority", task["priority"])
            return task

    raise HTTPException(status_code=404, detail="Task not found")


@router.delete("/{task_id}")
def delete_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id and not task["is_deleted"]:
            task["is_deleted"] = True
            return {"message": "Task deleted successfully"}

    raise HTTPException(status_code=404, detail="Task not found")
