from fastapi import FastAPI
from contextlib import asynccontextmanager

from core.config import settings
from core.init_db import create_first_superuser
from api.routers import main_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_first_superuser()
    yield


app = FastAPI(title=settings.app_title, lifespan=lifespan)

app.include_router(main_router)
