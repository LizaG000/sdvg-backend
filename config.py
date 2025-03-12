from pydantic import IPvAnyAddress, PostgresDsn, EmailStr, AnyUrl
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    host: IPvAnyAddress
    port: int = 8000
    secret: str  # openssl rand -hex 32
    postgres_url: PostgresDsn
    token_lifetime: int = 15
    system_username: str = 'admin'
    system_pwd: str = 'admin'
    system_email: EmailStr = 'ernest@elitvinenko.tech'
    domain: str
    static_url: str = ""

    class Config:
        env_file = '.env'



Config = Settings()
