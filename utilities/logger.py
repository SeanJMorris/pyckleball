import logging
import coloredlogs

# logger = logging.getLogger(__name__)
# coloredlogs.install(level='DEBUG', logger=logger)

logger = logging.getLogger(__name__)
# log_format = '%(asctime)s [%(name)s:%(process)d] %(levelname)s %(message)s'
log_format = '%(asctime)s %(hostname)s [%(name)s:%(process)d] %(levelname)s %(message)s'
date_format = '%Y-%m-%dT%H:%M:%S%z'  # ISO-8601 format with timezone

coloredlogs.install(level='DEBUG', logger=logger, fmt=log_format, datefmt=date_format)

if __name__ == "__main__":
    logger.debug("This is a debug message.")
    logger.info("This is an info message.")
    logger.warning("This is a warning message.")
    logger.error("This is an error message.")
    logger.critical("This is a critical message.")
