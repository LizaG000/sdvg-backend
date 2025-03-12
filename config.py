import toml  # или tomllib в Python 3.11+
from pydantic import BaseModel

class BackendSettings(BaseModel):
    host: str
    port: int

class DatabaseSettings(BaseModel):
    postgres_url: str

class AuthSettings(BaseModel):
    private_key_path: str
    public_key_path: str
    algorithm: str
    access_token_expire_minutes: int

class Settings(BaseModel):
    backend: BackendSettings
    database: DatabaseSettings
    auth: AuthSettings

with open("config.toml", "r", encoding="utf-8") as f:
    config_data = toml.load(f)

settings = Settings(**config_data)
