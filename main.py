import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from loguru import logger

from config import settings
# from config import Config
# from config import AuthCOnfig

from core.api import router as api_router

app = FastAPI()

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Including routers

app.include_router(api_router)


@app.get("/")
def root():
    return {"message": "Hello World"}


if __name__ == '__main__':
    uvicorn.run('main:app', host=str(settings.backend.host), port=settings.backend.port, reload=True)
