from pydantic import BaseSettings
from pathlib import Path

class Settings(BaseSettings):
    OUT_DIR: Path = Path("../price_landscape_outputs").resolve()
    CACHE_SEC: int = 60
    ALLOW_ORIGINS: str = "*"

settings = Settings()
