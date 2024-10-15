from contextlib import asynccontextmanager, suppress
from fastapi_users.exceptions import UserAlreadyExists
from pydantic import EmailStr

from core.config import settings
from core.db import get_async_session
from core.user import get_user_db, get_user_manager
from schemas.user import UserCreate

get_async_session_context = asynccontextmanager(get_async_session)
get_user_db_context = asynccontextmanager(get_user_db)
get_user_manager_context = asynccontextmanager(get_user_manager)


async def create_user(
    email: EmailStr,
    password: str,
    is_superuser: bool = False,
):
    async with get_async_session_context() as session:
        async with get_user_db_context(session) as user_db:
            async with get_user_manager_context(user_db) as user_manager:
                with suppress(UserAlreadyExists):
                    await user_manager.create(
                        UserCreate(
                            email=email,
                            password=password,
                            is_superuser=is_superuser,
                        ),
                    )

async def create_first_superuser():
    """Создаем суперпользователя, если он не существует."""
    if (settings.first_superuser_email is not None
            and settings.first_superuser_password is not None):
        await create_user(
            email=settings.first_superuser_email,
            password=settings.first_superuser_password,
            is_superuser=True,
        )
