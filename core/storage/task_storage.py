from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException
from datetime import datetime

from .base import BaseStorage
from ..models.task.requests import CreateTaskRequest
from ..models.task.requests import UpdateTaskRequest
from ..models.task.responses import TaskRespons

class TaskStorage(BaseStorage):
    async def create_task(self, task: CreateTaskRequest) -> list[TaskRespons]:
        stmt = text("""
            insert into task (profile_id, title, text, till_dt, completed_dt)
            values (:profile_id, :title, :text, :till_dt, :completed_dt)
        """)

        stmt_select = text("""
            select * from task where profile_id = :profile_id
        """)

        async with self.get_session() as session:
            session: AsyncSession
            task_data = task.model_dump(mode="python")
            if isinstance(task_data['till_dt'], datetime) and task_data['till_dt'].tzinfo is not None:
                task_data['till_dt'] = task_data['till_dt'].replace(tzinfo=None)
            if task_data["completed_dt"] is None:
                task_data["completed_dt"] = task_data["till_dt"]
            await session.execute(stmt, task_data)
            await session.commit()

            d = (await session.execute(stmt_select, task_data)).fetchall()
            return list(TaskRespons(
                id = i.id,
                profile_id = i.profile_id,
                title = i.title,
                text = i.text,
                till_dt = i.till_dt,
                completed_dt = i.completed_dt,
                date_modified = i.date_modified
            ) for i in d)
        

    async def get_task_by_id(self, id: int) -> list[TaskRespons]:
        stmt = text("""
            select * from task where profile_id = :profile_id
        """)

        params = {"profile_id": id}

        async with self.get_session() as session:
            session: AsyncSession
            d = (await session.execute(stmt, params)).fetchall()
            return list(TaskRespons(
                id = i.id,
                profile_id = i.profile_id,
                title = i.title,
                text = i.text,
                till_dt = i.till_dt,
                completed_dt = i.completed_dt,
                date_modified = i.date_modified
                ) for i in d)
    
    async def update_task(self, task: UpdateTaskRequest):
        stmt = text("""
            update task set title = :title, text = :text, till_dt = :till_dt, completed_dt = :completed_dt
            where id = :id
        """)

        stmt_select = text("""
            select * from task where profile_id = :profile_id
        """)

        async with self.get_session() as session:
            session: AsyncSession
            task_data = task.model_dump(mode="python")
            print(task_data)
            if isinstance(task_data['till_dt'], datetime) and task_data['till_dt'].tzinfo is not None:
                task_data['till_dt'] = task_data['till_dt'].replace(tzinfo=None)
            if isinstance(task_data['completed_dt'], datetime) and task_data['completed_dt'].tzinfo is not None:
                task_data['completed_dt'] = task_data['completed_dt'].replace(tzinfo=None)

            await session.execute(stmt, task_data)
            await session.commit()

            d = (await session.execute(stmt_select, task_data)).fetchall()
            return list(TaskRespons(
                id = i.id,
                profile_id = i.profile_id,
                title = i.title,
                text = i.text,
                till_dt = i.till_dt,
                completed_dt = i.completed_dt,
                date_modified = i.date_modified
                ) for i in d)

    async def delete_task(self, id: int, profile_id: int) -> list[TaskRespons]:
        stmt = text("""
            delete from task where id = :id
        """)

        stmt_select = text("""
            select * from task where profile_id = :profile_id
        """)

        params = {
            "id" : id,
            "profile_id" : profile_id
        }

        async with self.get_session() as session:
            session: AsyncSession

            await session.execute(stmt, params)
            await session.commit()

            d = (await session.execute(stmt_select, params)).fetchall()

            return list(TaskRespons(
                id = i.id,
                profile_id = i.profile_id,
                title = i.title,
                text = i.text,
                till_dt = i.till_dt,
                completed_dt = i.completed_dt,
                date_modified = i.date_modified
                ) for i in d)
