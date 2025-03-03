# Pylint ошибочно отмечает валидаторы полей. Отключаем предупреждение no-self-argument.
# pylint: disable=E0213
import re

from pydantic import BaseModel, field_validator, EmailStr, SecretStr, model_validator
from fastapi import HTTPException

def valid_phone(value: int):
    number_str = str(value)
    regex = r"^\d{10}$|^\d{11}$"
    if re.match(regex, number_str):
        return value
    raise HTTPException(status_code=422, detail="Неправильно набран номер телефона")
def valid_password(value: str):
    if isinstance(value, SecretStr):
        password = value.get_secret_value()
    else:
        password = value
    regex = r"^[a-zA-Zа-яА-Я0-9_+=-@.,/]{8,16}"
    if re.match(regex, password):
        return value
    raise HTTPException(status_code=422, detail="Пароль не соответствует требованиям безопасности")

class CreateProfileRequest(BaseModel):
    phone: int
    username: str
    password: str
    email: EmailStr

    @field_validator("phone")
    def validate_phone(cls, value: int) -> int:
        return valid_phone(value)

    @field_validator("username")
    def validate_username(cls, value):
        latyn_regex = r"^[a-zA-Z0-9_]*$"
        cyrilic_regex = r"^[а-яА-Я0-9_]*$"

        if re.match(latyn_regex, value) or re.match(cyrilic_regex, value):
            return value
        raise HTTPException(status_code=422, detail="Неправильно введено имя пользователя")

    @field_validator("password")
    def validate_password(cls, value):
        return valid_password(value)

class GetOneProfileRequest(BaseModel):
    email: EmailStr
    phone: int
    password: str

    @model_validator(mode="before")
    def validate_login(cls, values: dict):
        email = values.get("email")
        phone = values.get("phone")

        if not email and not phone:
            raise HTTPException(status_code=422, detail="Не введен логин")

        # Если email не задан, подставляем значение по умолчанию
        if not email:
            values["email"] = "base@exemple.ru"

        # Если phone не задан, подставляем значение по умолчанию
        if not phone:
            values["phone"] = 80000000000

        return values

    @field_validator("phone")
    def validate_phone(cls, value: int) -> int:
        return valid_phone(value)
    
    @field_validator("password")
    def validate_password(cls, value):
        return valid_password(value)