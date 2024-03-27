import logging
from logging import FileHandler

def setup_logger(name=None, log_file='test_log.log', level=logging.INFO):
    if name is None:
        name = __name__
    logger = logging.getLogger(name)
    if not logger.handlers:
        logger.setLevel(level)
        # Include the function name with %(funcName)s and set the datetime format
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(funcName)s - %(message)s', '%d-%m-%Y %H:%M:%S')
        formatter_c = logging.Formatter('%(asctime)s  - %(levelname)s  - %(message)s', '%d-%m-%Y %H:%M:%S')
        file_handler = FileHandler(log_file, mode='w')
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter_c)
        logger.addHandler(console_handler)

    return logger
