import logging


logger = logging.getLogger(__name__)


def my_func(x, y):
    logger.debug("Log from another module")
    logger.info("x and y values: %s %d", x, y)
    try:
        x / y
    except TypeError as ex:
        # print(ex, type(ex).__name__)
        # logging.error("Cannot divide: %s", ex)
        logger.error("Cannot divide", exc_info=True)
