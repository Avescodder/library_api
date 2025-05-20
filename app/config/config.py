from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
HOST = os.getenv("HOST")
PORT = os.getenv("PORT")