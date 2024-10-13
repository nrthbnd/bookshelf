import aio_pika
import json
import logging

from logging_config import setup_logging

from broker.config import settings

setup_logging()
logger = logging.getLogger("rabbitmq_service")


async def produce_message(action: str, book):
    connection_url = settings.RMQ_CONNECTION_URL
    connection = await aio_pika.connect_robust(connection_url)

    async with connection:
        channel = await connection.channel()
        queue = await channel.declare_queue(settings.RMQ_QUEUE_NAME, durable=True)

        message = json.dumps({
            "action": action,
            "book": {
                "id": book.id,
                "title": book.title,
                "author": book.author,
                "publication_date": book.publication_date.isoformat(),
            },
        })

        await channel.default_exchange.publish(
            aio_pika.Message(body=message.encode()),
            routing_key=queue.name
        )
        logger.debug(f"Message published, queuename: {queue.name}.")
