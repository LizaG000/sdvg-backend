import json
import asyncio
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.asyncio import AsyncAttrs, create_async_engine, async_sessionmaker
from config import settings
from loguru import logger


# Базовый класс для моделей??
class Base(AsyncAttrs, DeclarativeBase):
    pass


engine = create_async_engine(
    settings.database.postgres_url,
    pool_size=20,
    max_overflow=0,
    pool_pre_ping=True)


Session = async_sessionmaker(bind=engine, expire_on_commit=False)
