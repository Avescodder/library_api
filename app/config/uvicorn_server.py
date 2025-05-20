import uvicorn
import asyncio
from config.config import HOST, PORT
from config.logger import get_logger

logger = get_logger()


class UvicornServer:
    def __init__(self, app, host=HOST, port=PORT):
        self.app = app
        self.host = host
        self.port = port
        self.server = None

    async def start(self):
        config = uvicorn.Config(
            self.app, host=self.host, port=self.port, log_level="info"
        )
        server = uvicorn.Server(config)

        self.task = asyncio.create_task(server.serve())

    async def stop(self):
        if self.task:
            self.task.cancel()
            try:
                await self.task
            except asyncio.CancelledError:
                logger.info("FastAPI сервер остановлен")