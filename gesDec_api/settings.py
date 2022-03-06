"""SETTINGS
Settings loaders using Pydantic BaseSettings classes (load from environment variables / dotenv file)
"""

# # Installed # #
import pydantic

class BaseSettings(pydantic.BaseSettings):
    class Config:
        env_file = ".env"


class APISettings(BaseSettings):
    title: str = "GesDec API"
    host: str = "localhost"
    port: int = 8000

    class Config(BaseSettings.Config):
        env_prefix = "API_"


api_settings = APISettings()