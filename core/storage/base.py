from contextlib import asynccontextmanager

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker


class BaseStorage:

    def __init__(self, session_maker: async_sessionmaker):
        self.__session_maker: async_sessionmaker = session_maker

    @asynccontextmanager
    async def get_session(self) -> AsyncSession:
        session = self.__session_maker()
        try:
            yield session
        finally:
            await session.aclose()
