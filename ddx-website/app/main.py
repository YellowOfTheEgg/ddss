import os

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.api.v1.api import api_router
from app.core import config

app = FastAPI(title="ddx-website")
app.include_router(api_router, prefix=config.API_V1_STR)

origins = os.environ.get("ORIGINS", "*").split(" ")
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
