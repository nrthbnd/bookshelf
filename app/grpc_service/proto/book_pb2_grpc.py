# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import book_pb2 as book__pb2


class BookServiceStub(object):
    """Сервис для работы с книгами."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetBookById = channel.unary_unary(
                '/books.BookService/GetBookById',
                request_serializer=book__pb2.GetBookByIdRequest.SerializeToString,
                response_deserializer=book__pb2.Book.FromString,
                )
        self.ListBooks = channel.unary_unary(
                '/books.BookService/ListBooks',
                request_serializer=book__pb2.ListBooksRequest.SerializeToString,
                response_deserializer=book__pb2.ListBooksResponse.FromString,
                )


class BookServiceServicer(object):
    """Сервис для работы с книгами."""

    def GetBookById(self, request, context):
        """Получение информации о книге по ID."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListBooks(self, request, context):
        """Получение списка всех книг."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_BookServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetBookById': grpc.unary_unary_rpc_method_handler(
                    servicer.GetBookById,
                    request_deserializer=book__pb2.GetBookByIdRequest.FromString,
                    response_serializer=book__pb2.Book.SerializeToString,
            ),
            'ListBooks': grpc.unary_unary_rpc_method_handler(
                    servicer.ListBooks,
                    request_deserializer=book__pb2.ListBooksRequest.FromString,
                    response_serializer=book__pb2.ListBooksResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'books.BookService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class BookService(object):
    """Сервис для работы с книгами."""

    @staticmethod
    def GetBookById(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/books.BookService/GetBookById',
            book__pb2.GetBookByIdRequest.SerializeToString,
            book__pb2.Book.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListBooks(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/books.BookService/ListBooks',
            book__pb2.ListBooksRequest.SerializeToString,
            book__pb2.ListBooksResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
