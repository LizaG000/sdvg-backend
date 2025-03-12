from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException
from datetime import datetime

from .base import BaseStorage
from ..models.profile.requests import CreateProfileRequest
from ..models.profile.responses import CreateProfileResponse
from ..models.profile.responses import GetProfilesResponse
from ..models.profile.requests import GetOneProfileRequest
from ..models.profile.responses import GetOneProfileRespons

class ProfileStorage(BaseStorage):
    async def create_profile(self, profile: CreateProfileRequest) -> CreateProfileResponse:
        stmt = text("""
        insert into profile (phone, username, password, email, balance) values  (
        :phone, :username, :password, :email, :balance
        )
        """)

        stmt_select = text(f"""
            select * from profile where phone ='{profile.phone}' limit 1
        """)

        async with self.get_session() as session:
            session: AsyncSession
            profile_data_query = profile.model_dump(mode="python")
            profile_data_query["balance"] = 400

            await session.execute(stmt, profile_data_query)
            await session.commit()

            d = (await session.execute(stmt_select)).fetchone()
            return CreateProfileResponse(id=d.id, phone=d.phone, username=d.username, password=d.password,
                                         email=d.email)
    
    async def get_profiles(self) -> list[GetProfilesResponse]:
        stmt_select = text("SELECT id, phone, username, password, email, date_created, date_modified, balance, is_del FROM profile")
        async with self.get_session() as session:
            session: AsyncSession
            result = await session.execute(stmt_select)
            rows = result.fetchall()
            profile = [
                GetProfilesResponse(
                    id = row.id,
                    phone = row.phone,
                    username = row.username,
                    password = row.password,
                    email = row.email,
                    date_created = row.date_created,
                    date_modified = row.date_modified,
                    balance = row.balance,
                    is_del = row.is_del
                )
                for row in rows
            ]
            return profile
    
    async def get_one_profile(self, profile: GetOneProfileRequest) -> GetOneProfileRespons:
        stmt_select = text("""
                SELECT phone, username, email, date_modified, password, balance, is_del
                FROM profile
                WHERE phone = :phone OR email = :email
                limit 1
            """)
        params = {
            "phone": profile.phone,
            "email": profile.email,
        }

        async with self.get_session() as session:
            session: AsyncSession
            result = (await session.execute(stmt_select, params)).fetchall()
            if result == []:
                raise HTTPException(status_code=422, detail="Неверно введен логин")
            result = result[0]
            if result.password == profile.password:
                return GetOneProfileRespons(
                    username = result.username,
                    phone = result.phone,
                    email = result.email,
                    date_modified = result.date_modified,
                    balance = result.balance,
                    is_del = result.is_del
                    )
            else:
                raise HTTPException(status_code=422, detail="Неверно введен пароль")

    async def update_del_profile(self, profile: GetOneProfileRequest) -> bool:
        stmt = text("""
            UPDATE profile
            SET is_deleted=True, date_modified = :date_modified
            WHERE (phone = :phone OR email = :email) and password = :password
        """)

        params = {
            "phone": profile.phone,
            "email": profile.email,
            "password": profile.password,
            "date_modified": datetime.now()
            }
        
        async with self.get_session() as session:
            session: AsyncSession
            try:
                await self.get_one_profile(profile)
                await session.execute(stmt, params)   
                await session.commit()
                return True
            except Exception as exc:
                raise HTTPException(status_code=422, detail="Аккаунт не найден") from exc


    async def delete_profile(self, profile: GetOneProfileRequest) -> bool:
        stmt = text("""
                DELETE from profile
                WHERE (phone = :phone OR email = :email) and password = :password
        """)

        params = {
            "phone": profile.phone,
            "email": profile.email,
            "password": profile.password
            }
        
        async with self.get_session() as session:
            session: AsyncSession
            try:
                await self.get_one_profile(profile)
                await session.execute(stmt, params)   
                await session.commit()
                return True
            except Exception as exc:
                raise HTTPException(status_code=422, detail="Аккаунт не найден") from exc
