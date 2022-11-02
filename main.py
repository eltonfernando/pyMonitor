from logger import LoggerConfig
from logging import DEBUG, INFO
LoggerConfig(console_level=DEBUG, file_level=INFO,path_logger="log/logger.log")
from hardware_monitor import Machine

if __name__ == "__main__":
    pc =Machine()
    print(pc.ram())
    print(pc.disk())