from fastapi import APIRouter, HTTPException, Response, Form
from core.models.profile.requests import CreateProfileRequest
from core.models.profile.requests import GetOneProfileRequest
from ..models.profile.responses import GetProfilesResponse
from core.storage import profile_storage
from core.services.auth.utils import encode_jwt
from loguru import logger
router = APIRouter()


@router.get("/profiles")
async def get_profiles():
    return await profile_storage.get_profiles()

@router.get("/profile", response_model=GetProfilesResponse)
async def get_profile(response: Response, password: str, email = None, phone = None) -> GetProfilesResponse:
    if email == None and phone == None:
        raise HTTPException(status_code=422, detail="Не введен логин")
    elif email != None:
        phone = 80000000000
    else:
        email = "base@exemple.ru"
    person = await profile_storage.get_one_profile(GetOneProfileRequest(
        email = email,
        phone = phone,
        password = password
    ))
    token = encode_jwt({})
    logger.info(token)
    response.headers["Authorization"] = f"Bearer {encode_jwt({})}"
    return person

@router.post("/profile", response_model=GetProfilesResponse)
async def create_profile(response: Response, profile: CreateProfileRequest=Form) -> GetProfilesResponse:
    person = await profile_storage.create_profile(profile)
    response.headers["Authorization"] = f"Bearer {encode_jwt({})}"
    return person
