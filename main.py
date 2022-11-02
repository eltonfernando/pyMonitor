import asyncio
from logger import LoggerConfig
from logging import DEBUG, INFO
LoggerConfig(console_level=DEBUG, file_level=INFO,path_logger="log/logger.log")
from monitor.controller.sever import start_server

if __name__ == "__main__":
   asyncio.run(start_server())