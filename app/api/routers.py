from fastapi import APIRouter

from constants import BOOK_ROUTER_PREFIX, BOOK_ROUTER_TAG

from api.endpoints import book_router, user_router


main_router = APIRouter()

main_router.include_router(
    book_router,
    prefix=BOOK_ROUTER_PREFIX,
    tags=[BOOK_ROUTER_TAG],
)

main_router.include_router(user_router)
