from datetime import datetime
from pydantic import BaseModel
from typing import Optional

from .requests import CreateTaskRequest

class TaskRespons(CreateTaskRequest):
    id: int
    profile_id: int
    title: str
    text: str
    till_dt: datetime
    completed_dt: Optional[datetime] = None
    date_modified: datetime