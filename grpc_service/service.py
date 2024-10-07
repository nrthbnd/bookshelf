import asyncio
import grpc
import logging
from concurrent import futures
from sqlalchemy.future import select

from app.crud import book_crud, Book
from app.core.db import get_async_session
from proto import book_pb2_grpc, book_pb2


class BookServiceServicer(book_pb2_grpc.BookServiceServicer):
    async def GetBookById(self, request, context):
        async for session in get_async_session():
            book_db = await session.execute(
                select(Book).where(
                    Book.id == request.id)
            )
            if book:=book_db.scalars().first():
                return book_pb2.Book(
                    id=book.id,
                    title=book.title,
                    author=book.author,
                    publication_date=book.publication_date.isoformat(),
                )
            else:
                context.set_details(f'Book with id {request.id} not found')
                context.set_code(grpc.StatusCode.NOT_FOUND)
                return book_pb2.Book()

    async def ListBooks(self, request, context):
        async for session in get_async_session():
            books = await book_crud.get_multi(session)

            return book_pb2.ListBooksResponse(
                books=[
                    book_pb2.Book(
                        id=book.id,
                        title=book.title,
                        author=book.author,
                        publication_date=book.publication_date.isoformat(),
                    ) for book in books
                ]
            )


async def serve() -> None:
    server = grpc.aio.server(futures.ThreadPoolExecutor(max_workers=10))
    book_pb2_grpc.add_BookServiceServicer_to_server(BookServiceServicer(), server)
    listen_port = '[::]:50051'
    server.add_insecure_port(listen_port)
    await server.start()
    logging.info(f'Server is running on {listen_port}')
    await server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(serve())
