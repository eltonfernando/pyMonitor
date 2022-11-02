import json
import psutil

from .disk import Disk
from .ram import Ram
from .cpu import Cpu
from .network import Network


class Machine():

    def __init__(self):
        self.__started = False
        self.__disk = Disk()
        self.__ram = Ram()
        self.__cpu = Cpu()
        self.__net = Network()

    def info(self) -> json:
        data_info = {"cpu": self.__cpu.info(),
                     "ram": self.__ram.info(),
                     "disck": self.__disk.info(),
                     "network": self.__net.info(),
                     "temperature": self.temperature(),
                     "sbattery": {}}
        return data_info

    def temperature(self):
        return psutil.sensors_temperatures()
