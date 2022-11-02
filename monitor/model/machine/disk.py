import psutil
from logging import getLogger
from collections import namedtuple


class Disk:

    def __init__(self):
        self.logger = getLogger(__name__)

    def info(self) -> dict:
        disk_size = psutil.disk_usage("..")
        total = round(disk_size.total / 1000000000, 2)
        used = round(disk_size.used / 1000000000, 2)
        percent = disk_size.percent
        free = round(disk_size.free / 1000000000, 2)
        result = {"total": total,
                  "used": used,
                  "free": free,
                  "percent": percent}
        self.logger.debug(result)
        return result
