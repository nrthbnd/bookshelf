import logging
import logging.config
import os


LOG_LEVEL_APP = os.getenv("LOG_LEVEL_APP", "INFO")
LOG_LEVEL_GRPC = os.getenv("LOG_LEVEL_GRPC", "INFO")
LOG_LEVEL_RMQ = os.getenv("LOG_LEVEL_RMQ", "INFO")


LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "simple": {
            "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "simple",
            "level": "DEBUG",
        },
    },
    "loggers": {
        "app": {
            "handlers": ["console"],
            "level": LOG_LEVEL_APP,
            "propagate": False,
        },
        "grpc": {
            "handlers": ["console"],
            "level": LOG_LEVEL_GRPC,
            "propagate": False,
        },
        "rabbitmq_service": {
            "handlers": ["console"],
            "level": LOG_LEVEL_RMQ,
            "propagate": False,
        },
    },
}


def setup_logging():
    logging.config.dictConfig(LOGGING_CONFIG)
