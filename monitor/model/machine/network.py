from logging import getLogger
import requests
import psutil


class Network:
    def __init__(self):
        self.logger = getLogger(__name__)

    def info(self) -> dict:

        return psutil.net_if_addrs()

    def ip_externo(self):
        try:
            ip = requests.get('https://api.ipify.org').content.decode('utf8')
        except Exception as erro:
            self.logger.error(f'falha ip {erro}')
            ip = ""
        return ip


if __name__ == "__main__":
    net = Network()
    print(net.info())

