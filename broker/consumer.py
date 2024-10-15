import aio_pika
import asyncio
import json
import logging

from aio_pika import IncomingMessage
from logging_config import setup_logging

from broker.config import settings


async def consume():
    try:
        logger.info("Attempting to connect to RabbitMQ...")
        connection_url = settings.RMQ_CONNECTION_URL
        connection = await aio_pika.connect_robust(connection_url)

        async with connection:
            logger.info("Connection established. Setting up channel and queue...")
            channel = await connection.channel()
            queue = await channel.declare_queue(settings.RMQ_QUEUE_NAME, durable=True)

            async with queue.iterator() as queue_iter:
                async for message in queue_iter:  # type: IncomingMessage
                    async with message.process():
                        logger.info(f"Received message: {json.loads(message.body.decode())}")

    except Exception as e:
        logger.exception(f"Error in consumer: {e}")
        raise


if __name__ == "__main__":
    setup_logging()
    logger = logging.getLogger("rabbitmq_service")
    asyncio.run(consume())
