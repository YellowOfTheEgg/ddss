from fastapi import APIRouter, Request, Response
from app.api.proxy import _proxy
from app.core.config import settings


router = APIRouter()

#endpoint for symptoms which contains the forwarding to the website-service
@router.get("/symptoms")
async def symptoms(request: Request, response: Response):

    symptom_response = await _proxy(request, f"{settings.DDX_WEBSITE_API}/symptoms/")

    return symptom_response