import os

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.api.v1.api import api_router
from app.core import config

#run fastAPI service with defined router
app = FastAPI(title="ddx-backend")
app.include_router(api_router, prefix=config.API_V1_STR)

#set origins which are allowed to connect to the service
origins = os.environ.get("ORIGINS", "*").split(" ")
#set allowed methods, headers etc.
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
