import os
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


class Settings(BaseSettings):
    # Application Settings
    app_name: str = os.getenv("APP_NAME", "FastAPI App")
    app_version: str = os.getenv("APP_VERSION", "0.1.0")
    debug: bool = os.getenv("DEBUG", "False") == "True"

    # Server Settings
    host: str = os.getenv("HOST", "127.0.0.1")
    port: int = int(os.getenv("PORT", "8000"))

    # Database Settings
    database_url: str = os.getenv("DATABASE_URL", "sqlite:///./test.db")
    atlas_connection_string: str = os.getenv("ATLAS_CONNECTION_STRING", "") # MongoDB Atlas connection string

    # API Settings
    api_prefix: str = os.getenv("API_PREFIX", "/api/v1")

    # Secret Keys
    secret_key: str = os.getenv("SECRET_KEY", "your-super-secret-key")
    hugging_face_access_token: str = os.getenv("HUGGING_FACE_ACCESS_TOKEN", "") # Hugging Face API access token

    class Config:
        env_file = ".env"


# Create global settings object
settings = Settings()
