from datetime import datetime
from pydantic import BaseModel, EmailStr, SecretStr
from .requests import CreateProfileRequest


class CreateProfileResponse(CreateProfileRequest):
    id: int
    password: SecretStr

class GetProfilesResponse(BaseModel):
    id: int
    phone: int
    username: str
    email: EmailStr
    date_modified: datetime
    balance: float
    is_del: bool

class GetOneProfileRespons(BaseModel):
    phone: int
    username: str
    email: str
    date_modified: datetime
    balance: int
    is_del: bool
