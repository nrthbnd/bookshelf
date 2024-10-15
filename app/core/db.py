from typing import AsyncGenerator
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine

from core.config import settings


Base = declarative_base()

engine = create_async_engine(settings.database_url)

AsyncSessionLocal = sessionmaker(bind=engine, class_=AsyncSession)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    """Асинхронный генератор сессий."""
    async with AsyncSessionLocal() as async_session:
        yield async_session
