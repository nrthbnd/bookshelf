import asyncio
import grpc

from proto import book_pb2_grpc, book_pb2


async def run():
    async with grpc.aio.insecure_channel('localhost:50051') as channel:
        stub = book_pb2_grpc.BookServiceStub(channel)

        # Получение книги по ID
        try:
            response = await stub.GetBookById(book_pb2.GetBookByIdRequest(id=5))
            print("Book received: ", response)
        except grpc.RpcError as e:
            print(f"Error: {e.code()} - {e.details()}")


        # Получение списка всех книг
        response = await stub.ListBooks(book_pb2.ListBooksRequest())
        print("Books received: ", response.books)


if __name__ == '__main__':
    asyncio.run(run())
