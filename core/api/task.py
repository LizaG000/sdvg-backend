from fastapi import APIRouter
from core.storage import task_storage
from src.core.models.task.requests import CreateTaskRequest
from src.core.models.task.responses import TaskRespons
from src.core.models.task.requests import UpdateTaskRequest

router = APIRouter()

@router.post("/task")
async def create_task(task: CreateTaskRequest) -> list[TaskRespons]:
    return await task_storage.create_task(task)

@router.get("/task")
async def get_task(profile_id: int) -> list[TaskRespons]:
    return await task_storage.get_task_by_id(profile_id)

@router.patch("/task")
async def update_task(task: UpdateTaskRequest) -> list[TaskRespons]:
    return await task_storage.update_task(task)

@router.delete("/task")
async def delete_task(id: int, profile_id: int) -> list[TaskRespons]:
    return await task_storage.delete_task(id, profile_id)