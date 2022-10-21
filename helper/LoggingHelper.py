# https://blog.csdn.net/claroja/article/details/102601920
import logging
from logging import Formatter, Handler, handlers as logging_handlers
from typing import List, Optional

from helper.FileHelper import create_dir_of_path


def get_logger1(
        level=logging.INFO,
        formatter: Formatter = logging.Formatter(
            '%(asctime)s %(filename)s %(funcName)s [line:%(lineno)d] %(levelname)s %(message)s'
        ),
        handlers: List[Optional[Handler]] = None,
):
    if handlers is None:
        handlers = [logging.StreamHandler()]
    logger = logging.getLogger()
    logger.setLevel(level)
    for i in handlers:
        i.setFormatter(formatter)
        logger.addHandler(i)
    return logger


def get_logger2(
        level=logging.INFO,
        formatter: Formatter = logging.Formatter(
            '%(asctime)s %(filename)s %(funcName)s [line:%(lineno)d] %(levelname)s %(message)s'
        ),
        handlers: List[Optional[Handler]] = None,
):
    if handlers is None:
        file_name = 'logs/log'
        create_dir_of_path(file_name)
        handlers = [logging_handlers.TimedRotatingFileHandler(file_name, when='D', encoding="utf-8")]
        logger = logging.getLogger()
        logger.setLevel(level)
        for i in handlers:
            i.setFormatter(formatter)
            logger.addHandler(i)
        return logger
