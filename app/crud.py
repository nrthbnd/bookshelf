from typing import Optional
from fastapi.encoders import jsonable_encoder
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from models import Book


class CRUDBook:
    """Базовые CRUD методы."""

    def __init__(self, model):
        self.model = model

    async def get(
        self,
        obj_id: int,
        session: AsyncSession,
    ):
        """Получить книгу по id."""
        db_obj = await session.execute(
            select(self.model).where(self.model.id == obj_id))
        return db_obj.scalars().first()

    async def get_multi(
        self,
        session: AsyncSession,
    ):
        """Получить все книги."""
        db_objs = await session.execute(select(self.model))
        return db_objs.scalars().all()

    async def create(
        self,
        obj_in,
        session: AsyncSession,
    ):
        """Создать новую книгу."""
        obj_in_data = obj_in.dict()
        db_obj = self.model(**obj_in_data)
        session.add(db_obj)
        await session.commit()
        await session.refresh(db_obj)
        return db_obj

    async def update(
        self,
        db_obj,
        obj_in,
        session: AsyncSession,
    ):
        """Обновить книгу."""
        obj_data = jsonable_encoder(db_obj)
        update_data = obj_in.dict(exclude_unset=True)

        for field in obj_data:
            if field in update_data:
                setattr(db_obj, field, update_data[field])
        session.add(db_obj)
        await session.commit()
        await session.refresh(db_obj)
        return db_obj

    async def remove(
        self,
        db_obj,
        session: AsyncSession,
    ):
        """Удалить книгу."""
        await session.delete(db_obj)
        await session.commit()
        return db_obj

    async def get_book_id_by_name(
        self,
        book_title: str,
        session: AsyncSession,
    ) -> Optional[int]:
        """Получить id книги по ее названию."""
        db_book_id = await session.execute(
            select(Book.id).where(
                Book.title == book_title
            )
        )
        return db_book_id.scalars().first()


book_crud = CRUDBook(Book)
