from typing import Union
from database.database import init_db
from config.config import DATABASE_URL
import asyncio 
from config.uvicorn_server import UvicornServer

from fastapi import FastAPI



async def create_app():
    app = FastAPI()

    @app.get("/")
    async def read_root():
        return {"Hello": "World"}
    
    engine, session_factory = await init_db(DATABASE_URL)
    app.state.session_factory = session_factory

    server = UvicornServer(app)
    await server.start()

    
if __name__ == "__main__":
    asyncio.run(create_app())

