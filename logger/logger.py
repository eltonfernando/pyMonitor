import logging
from logging import handlers
from os import path, mkdir


class LoggerConfig:
    """
    configure logs for output in terminal and save to file
        :param console_level: logging.DEBUG
        :param file_level: logging.ERROR
        :param path_logger: log/log.log
    """

    def __init__(
        self,
        console_level: logging = logging.DEBUG,
        file_level: logging = logging.DEBUG,
        path_logger: str = "log/log.log",
    ):
        self.console_level = console_level
        self.file_level = file_level
        self.path_logger = path_logger
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
        self.formatter = logging.Formatter(
            "%(asctime)s:%(levelname)s:%(filename)s:%(lineno)d:%(message)s"
        )
        self.logger.handlers.clear()
        self.__configure_console()
        self.__configure_file()

    def __configure_file(self):
        self.__check_path()
        fh = handlers.RotatingFileHandler(
            filename=self.path_logger,
            mode="a",
            maxBytes=5000000,  # 5MB
            backupCount=4,
            encoding="utf-8",
        )
        fh.setLevel(self.file_level)
        fh.setFormatter(self.formatter)
        self.logger.addHandler(fh)

    def __configure_console(self):
        ch = logging.StreamHandler()
        ch.setLevel(self.console_level)
        ch.setFormatter(self.formatter)
        self.logger.addHandler(ch)

    def __check_path(self):
        dir_logger = path.dirname(self.path_logger)
        if not path.isdir(dir_logger):
            mkdir(dir_logger)
