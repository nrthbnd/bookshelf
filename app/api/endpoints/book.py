from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from broker.publisher import produce_message
from api.validators import check_obj_exists, check_name_duplicate
from crud import book_crud
from core.db import get_async_session
from core.user import current_user
from constants import CLEAR_ROUTE, BOOK_ID_ROUTE, BOOK_NOT_EXISTS_EXCEPTION
from schemas.book import BookCreate, BookDB, BookUpdate

router = APIRouter()


@router.post(
    CLEAR_ROUTE,
    response_model=BookDB,
    dependencies=[Depends(current_user)],
)
async def create_new_book(
    book: BookCreate,
    session: AsyncSession = Depends(get_async_session),
):
    """Создать новую книгу."""
    await check_name_duplicate(book_title=book.title, session=session)
    new_book = await book_crud.create(obj_in=book, session=session)
    await produce_message("create", new_book)
    return new_book


@router.get(
    CLEAR_ROUTE,
    response_model=list[BookDB],
    dependencies=[Depends(current_user)],
)
async def get_all_books(
    session: AsyncSession = Depends(get_async_session),
):
    """Получить все книги."""
    all_books = await book_crud.get_multi(session=session)
    return all_books


@router.get(
    BOOK_ID_ROUTE,
    response_model=BookDB,
    dependencies=[Depends(current_user)],
)
async def get_book(
    book_id: int,
    session: AsyncSession = Depends(get_async_session),
):
    """Получить книгу по id."""
    book = await book_crud.get(obj_id=book_id, session=session)
    return book


@router.patch(
    BOOK_ID_ROUTE,
    response_model=BookDB,
    dependencies=[Depends(current_user)],
)
async def partially_update_book(
    book_id: int,
    obj_in: BookUpdate,
    session: AsyncSession = Depends(get_async_session),
):
    """Редактировать существующую книгу."""
    book = await check_obj_exists(
        obj_id=book_id,
        model_crud=book_crud,
        exception=BOOK_NOT_EXISTS_EXCEPTION,
        session=session,
    )
    if obj_in.title is not None:
        await check_name_duplicate(book_title=obj_in.title, book_in_id=book_id, session=session)

    updated_book = await book_crud.update(db_obj=book, obj_in=obj_in, session=session)
    await produce_message("update", updated_book)
    return updated_book


@router.delete(
    BOOK_ID_ROUTE,
    response_model=BookDB,
    dependencies=[Depends(current_user)],
)
async def remove_book(
    book_id: int,
    session: AsyncSession = Depends(get_async_session),
):
    """Удалить книгу."""
    book = await check_obj_exists(
        obj_id=book_id,
        model_crud=book_crud,
        exception=BOOK_NOT_EXISTS_EXCEPTION,
        session=session,
    )
    removed_book = await book_crud.remove(db_obj=book, session=session)
    await produce_message("delete", removed_book)
    return removed_book
