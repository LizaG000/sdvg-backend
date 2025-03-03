"""
Register our storages
"""
from .profile_storage import ProfileStorage
from .task_storage import TaskStorage
from .base import BaseStorage
from database import Session

base_storage = BaseStorage(Session)
profile_storage = ProfileStorage(Session)
task_storage = TaskStorage(Session)
