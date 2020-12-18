from fastapi import APIRouter, Request, Response
from app.api.proxy import _proxy
from app.core.config import settings


router = APIRouter()

#endpoint for diagnoses which contains the forwarding to the ml-service (called backend)
@router.get("/diagnoses/")
async def diagnoses(request: Request, response: Response):

    diagnoses_response = await _proxy(request, f"{settings.DDX_BACKEND_API}/diagnoses/")

    return diagnoses_response
