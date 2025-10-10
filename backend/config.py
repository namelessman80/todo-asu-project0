from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    mongodb_url: str = "mongodb://localhost:27017"
    database_name: str = "todo_app"
    secret_key: str = "your-secret-key-change-this-in-production-09876543210"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30
    
    class Config:
        env_file = ".env"
        case_sensitive = False


settings = Settings()




