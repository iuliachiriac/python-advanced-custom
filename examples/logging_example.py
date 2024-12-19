import logging
import logging_other_module

logger = logging.getLogger("my_app")
logging.basicConfig(filename='example.log',
                    encoding='utf-8',
                    level=logging.DEBUG,
                    filemode="w",
                    format='%(asctime)s %(levelname)s %(message)s',
                    datefmt='%m/%d/%Y %H:%M:%S',
                    )

logger.debug('This message should go to the log file')
logger.info('So should this')
logger.warning('And this, too')
logger.error('And non-ASCII stuff, too, like Øresund and Malmö')
logger.critical("Critical error!")

logging_other_module.my_func("test", 20)
