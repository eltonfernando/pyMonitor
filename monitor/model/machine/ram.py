from psutil import virtual_memory
from collections import namedtuple


class Ram:
    def __init__(self):
        pass

    def info(self):
        value = virtual_memory()
        result = {"used":value.used,
                  "free": value.free,
                  "percent":value.percent}
        return result

if __name__ == "__main__":
    ram = Ram()
    print(ram.info())