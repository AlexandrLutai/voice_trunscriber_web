from beanie import Document
from datetime import datetime, timezone

class User(Document):
    username:str
    password:str
    created_at:datetime = datetime.now(timezone.utc)
    class Settings:
        name = "users"
        validate_on_save = True