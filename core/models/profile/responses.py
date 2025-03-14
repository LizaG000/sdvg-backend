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
    password: str
    email: EmailStr
    date_created: datetime
    date_modified: datetime
    balance: float
    del_: bool

class GetOneProfileRespons(BaseModel):
    phone: int
    username: str
    email: str
    date_modified: datetime
    balance: int
    del_: bool
