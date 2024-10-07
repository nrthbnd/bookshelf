from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from crud import book_crud
from constants import NAME_DUPLICATE_EXCEPTION


async def check_name_duplicate(
    book_title: str,
    session: AsyncSession,
    book_in_id: int = None,
) -> None:
    """Проверить уникальность полученного названия книги."""
    book_id = await book_crud.get_book_id_by_name(
        book_title, session,
    )
    if book_id is not None and book_id != book_in_id:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=NAME_DUPLICATE_EXCEPTION,
        )


async def check_obj_exists(
    obj_id: int,
    model_crud,
    exception: str,
    session: AsyncSession,
):
    """Проверить, существует ли объект по id."""
    obj = await model_crud.get(
        obj_id=obj_id,
        session=session,
    )
    if obj is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=exception,
        )
    return obj
