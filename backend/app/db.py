from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie
from app.models.user import User
import os

async def init_db():
    """Инициализация подключения к MongoDB и Beanie ODM"""
    mongo_uri = os.getenv("MONGO_URI", "mongodb://localhost:27017")
    client = AsyncIOMotorClient(mongo_uri)
    database = client.get_database("transcriber")
    await init_beanie(database=database, document_models=[User])  # type: ignore
    
 