from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from fastapi import HTTPException

class CreateTaskRequest(BaseModel):
    profile_id: int
    title: str
    text: str
    till_dt: datetime
    completed_dt: Optional[datetime] = None

class UpdateTaskRequest(BaseModel):
    id: int
    profile_id: int
    title: str
    text: str
    till_dt: datetime
    completed_dt: Optional[datetime] = None
