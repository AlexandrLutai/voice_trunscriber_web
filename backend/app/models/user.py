from beanie import Document
from datetime import datetime

class User(Document):
    username:str
    password:str
    class Settings:
        name = "users"
        validate_on_save = True