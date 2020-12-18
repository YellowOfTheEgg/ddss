from fastapi import APIRouter

from app.api.v1.endpoints.authentication import login, users,logout
from app.api.v1.endpoints.backend import diagnoses
from app.api.v1.endpoints.website import symptoms

api_router = APIRouter()

api_router.include_router(login.router, tags=["login"])
api_router.include_router(logout.router, tags=["logout"])
api_router.include_router(users.router, prefix="/users", tags=["users"])


api_router.include_router(symptoms.router, tags=['symptoms'])
api_router.include_router(diagnoses.router, tags=['diagnoses'])


