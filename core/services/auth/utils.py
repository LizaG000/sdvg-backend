import datetime
import jwt
import bcrypt
from loguru import logger
from config import settings

def encode_jwt(
        payload: dict,
        key: str = settings.auth.private_key_path.read_text(encoding="utf-8"),
        algorithm: str= settings.auth.algorithm,
        expire_timedelta: datetime.timedelta | None = None,
        expire_minutes: int = settings.auth.access_token_expire_minutes):
    to_encode = payload.copy()
    now = datetime.datetime.now(datetime.timezone.utc)
    if expire_timedelta:
        expire = now + expire_timedelta
    else:
        expire = now + datetime.timedelta(minutes=expire_minutes)
    to_encode.update(
        exp=expire,
        iat=now
    )
    encoded = jwt.encode(
        to_encode,
        key, 
        algorithm=algorithm)
    return encoded

def hash_password(password: str) -> str:
    salt = bcrypt.gensalt()
    pwd_bytes = password.encode('utf-8')
    hashed_password = bcrypt.hashpw(pwd_bytes, salt)
    return hashed_password.decode('utf-8')


def validate_password(password: str, hashed_password: str) -> bool:
    hashed_password_bytes = hashed_password.encode('utf-8')
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password_bytes)
