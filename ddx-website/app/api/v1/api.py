from fastapi import APIRouter

from app.api.v1.endpoints import symptoms
api_router = APIRouter()

api_router.include_router(symptoms.router, prefix="/symptoms", tags=["symptoms"])
