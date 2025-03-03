from fastapi import APIRouter, HTTPException
from core.models.profile.requests import CreateProfileRequest
from core.models.profile.requests import GetOneProfileRequest
from core.storage import profile_storage

router = APIRouter()


@router.get("/profiles")
async def get_profiles():
    return await profile_storage.get_profiles()

@router.get("/profile")
async def get_profile(password: str, email = None, phone = None):
    if email == None and phone == None:
        raise HTTPException(status_code=422, detail="Не введен логин")
    elif email != None:
        phone = 80000000000
    else:
        email = "base@exemple.ru"
    return await profile_storage.get_one_profile(GetOneProfileRequest(
        email = email,
        phone = phone,
        password = password
    ))

@router.patch("/profile")
async def update_del_profile(password: str, email = None, phone = None):
    await profile_storage.update_del_profile(GetOneProfileRequest(
        email = email,
        phone = phone,
        password = password
    ))

@router.delete("/prifile")
async def delete_profile(password: str, email = None, phone = None):
    await profile_storage.delete_profile(GetOneProfileRequest(
        email = email,
        phone = phone,
        password = password
    ))


@router.post("/profile")
async def create_profile(profile: CreateProfileRequest):
    return await profile_storage.create_profile(profile)
    # TODO Какие-нибудь токены сюда вставить надо
