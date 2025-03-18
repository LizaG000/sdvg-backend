from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException
from core.services.auth.utils import hash_password, validate_password

from .base import BaseStorage
from ..models.profile.requests import CreateProfileRequest
from ..models.profile.responses import GetProfilesResponse
from ..models.profile.requests import GetOneProfileRequest
from ..models.profile.responses import GetProfilesResponse

class ProfileStorage(BaseStorage):
    async def create_profile(self, profile: CreateProfileRequest) -> GetProfilesResponse:
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
            profile_query = profile.model_dump(mode="python")
            profile_query["password"] = hash_password(profile.password)
            profile_query["balance"] = 0

            await session.execute(stmt, profile_query)
            await session.commit()

            result = (await session.execute(stmt_select)).fetchone()
            return GetProfilesResponse(
                    id = result.id,
                    username = result.username,
                    phone = result.phone,
                    email = result.email,
                    date_modified = result.date_modified,
                    balance = result.balance,
                    is_del = result.is_del
                    )
    
    async def get_one_profile(self, profile: GetOneProfileRequest) -> GetProfilesResponse:
        stmt_select = text("""
                SELECT id, phone, username, email, date_modified, password, balance, is_del
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
            result = (await session.execute(stmt_select, params)).fetchone()
            if result is None:
                raise HTTPException(status_code=422, detail="Неверно введен логин")
            if validate_password(profile.password, result.password):
                return GetProfilesResponse(
                    id = result.id,
                    username = result.username,
                    phone = result.phone,
                    email = result.email,
                    date_modified = result.date_modified,
                    balance = result.balance,
                    is_del = result.is_del
                    )
            else:
                raise HTTPException(status_code=422, detail="Неверно введен пароль")
