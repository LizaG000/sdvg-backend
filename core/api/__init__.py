# api/__init__.py
from fastapi import APIRouter
from .profile import router as profile_router 
from .task import router as task_router

# Создаем главный роутер с префиксом '/api/v1'
router = APIRouter(prefix="/api")

# Подключаем роутер профиля к главному роутеру
router.include_router(profile_router)
router.include_router(task_router)
