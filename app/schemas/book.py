from datetime import date

from pydantic import BaseModel


class BookBase(BaseModel):
    """Базовая схема книги."""
    title: str | None
    author: str | None
    publication_date: date | None


class BookCreate(BookBase):
    """Схема для создания книги."""
    title: str
    author: str
    publication_date: date


class BookUpdate(BookBase):
    """Схема для обновления полей книги."""


class BookDB(BookCreate):
    """Схема книги в БД."""
    id: int

    model_config = {
        "from_attributes": True,
    }
