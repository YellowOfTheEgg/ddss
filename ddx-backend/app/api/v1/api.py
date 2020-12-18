from fastapi import APIRouter

from app.api.v1.endpoints import diagnoses, wmc
#this file includes the endpoints definitions into the FastApi router
api_router = APIRouter()
api_router.include_router(diagnoses.router, prefix="/diagnoses", tags=["diagnoses"])
api_router.include_router(wmc.router, prefix='/wmc', tags=['wmc'])