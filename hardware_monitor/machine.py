import requests
import psutil
from logging import getLogger
from collections import namedtuple


class Disk:
    result = namedtuple("disk", ["total", "used", "free", "percent"])

    def __init__(self):
        self.logger = getLogger(__name__)

    def info(self) -> result:
        free = self.__free()
        return free

    def __free(self) -> result:
        disk_size = psutil.disk_usage("..")
        total = round(disk_size.total / 1000000000, 2)
        used = round(disk_size.used / 1000000000, 2)
        percent = disk_size.percent
        free = round(disk_size.free / 1000000000, 2)
        return self.result(total, used, free, percent)


class Machine():

    def __init__(self):
        self.__disk = Disk()
        self.__ram = Ram()

    def disk(self) -> Disk.result:
        return self.__disk.info()

    def ram(self):
        return self.__ram.info()


class Cpu():
    def __init__(self):
        pass

    def info(self):
        pass

    def get_cpu_percent(self):
        """
        deve se chamada dentro de uma thread (demora)
        """
        return psutil.cpu_percent(interval=1)


class Ram:
    result = namedtuple("ram", ["used", "free", "percent"])

    def __init__(self):
        pass

    def info(self):
        result = psutil.virtual_memory()
        return self.result(result.used, result.free, result.percent)


class Network:
    def __init__(self):
        self.logger = getLogger(__name__)

    def get_ip_public(self):
        try:
            ip = requests.get('https://api.ipify.org').content.decode('utf8')
        except Exception as erro:
            self.logger.error(f'falha ip {erro}')
            ip = ""
        return ip


print(Machine().disk())
