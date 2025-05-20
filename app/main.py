from typing import Union
from database.database import init_db
from config.config import DATABASE_URL
import asyncio 
from config.uvicorn_server import UvicornServer

from config.logger import get_logger

from fastapi import FastAPI

logger = get_logger()

async def create_app():
    app = FastAPI()

    @app.get("/")
    async def read_root():
        return {"Hello": "World"}
    
    engine, session_factory = await init_db(DATABASE_URL)
    app.state.session_factory = session_factory

    server = UvicornServer(app)
    await server.start()
    
    try:
        while True:
            await asyncio.sleep(1)
    except KeyboardInterrupt:
        logger.info('Останавливаю сервис')
        await server.stop()





    
if __name__ == "__main__":
    asyncio.run(create_app())

