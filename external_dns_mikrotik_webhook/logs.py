import logging

import uvicorn.config
import uvicorn.logging

import external_dns_mikrotik_webhook


def configure_logging(log_level: int | None = None):
    """
    Configures logging for the application.
    """
    # configure the logger for the application
    log_level = log_level or logging.INFO
    logger = logging.getLogger(external_dns_mikrotik_webhook.__name__)
    handler = logging.StreamHandler()
    default_formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(name)s - %(message)s"
    )
    handler.setFormatter(default_formatter)
    logger.addHandler(handler)
    logger.setLevel(log_level)

    # configure pykrotik logging
    logger = logging.getLogger("pykrotik")
    handler = logging.StreamHandler()
    handler.setFormatter(default_formatter)
    logger.addHandler(handler)
    logger.setLevel(log_level)

    # configure uvicorn logging
    # NOTE: reference: uvicorn.config.LOGGING_CONFIG
    # NOTE: reference: uvicorn.logging.AccessFormatter
    logger = logging.getLogger("uvicorn.access")
    handler = logging.StreamHandler()
    access_formatter = uvicorn.logging.AccessFormatter(
        '%(asctime)s - %(levelname)s - %(name)s - "%(request_line)s" %(status_code)s'
    )
    handler.setFormatter(access_formatter)
    logger.addHandler(handler)
    logger.propagate = False
    logger.setLevel(log_level)
    logger = logging.getLogger("uvicorn")
    handler = logging.StreamHandler()
    handler.setFormatter(default_formatter)
    logger.addHandler(handler)
    logger.setLevel(log_level)
