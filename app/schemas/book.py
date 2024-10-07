from datetime import date
from typing import Optional

from pydantic import BaseModel


class BookBase(BaseModel):
    """Базовая схема книги."""
    title: Optional[str]
    author: Optional[str]
    publication_date: Optional[date]


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

    class Config:
        from_attributes = True
