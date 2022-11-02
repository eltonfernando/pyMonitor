import asyncio
import os
from logging import getLogger
from tornado.web import Application
from typing import Optional, Awaitable
from tornado.web import RequestHandler
from tornado.ioloop import IOLoop
from .. import Machine
logger = getLogger(__name__)


class BaseHandler(RequestHandler):

    def data_received(self, chunk: bytes) -> Optional[Awaitable[None]]:
        print(chunk)

    def set_default_headers(self):
        print("setting headers!!!")
        self.set_header("Content-Type", "application/json")
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "*")
        self.set_header(
            "Access-Control-Allow-Methods", "POST, GET, OPTIONS, PATCH, PUT"
        )

    def options(self):
        self.set_status(204)
        self.finish()

    def get(self):
        maq = Machine()
        resul = maq.info()
        print("GET")
        self.write(resul)

    def post(self):
        print(self.request.body)
        self.write(f"{self.request.body}")


def make_app():
    return Application([(r"/", BaseHandler)])


async def start_server():
    port = os.environ.get("PORT", "8888")
    host = os.environ.get("HOST", "localhost")
    logger.debug(f"host: {host}:{port}")
    app = make_app()
    app.listen(int(port))
    app.default_host = host
    await asyncio.Event().wait()
