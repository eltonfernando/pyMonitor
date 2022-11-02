import logging

from .logger import LoggerConfig


def test_logger():
    LoggerConfig(file_level=logging.DEBUG)
    log = logging.getLogger()
    log.error("erro")
    log.debug("teste loger")
    log.info("loger info")
    log.critical("loger critical")

