from fastapi import APIRouter, Request, Response
from app.api.proxy import _proxy
from app.core.config import settings


router = APIRouter()

#endpoint for user-logout which contains the forwarding to the auth-service
@router.post("/logout")
async def login_access_token(request: Request, response: Response):

    logout_response = await _proxy(
        request, f"{settings.DDX_AUTHENTICATION_API}/logout/"
    )

    if logout_response["status_code"] == 200:
        response.set_cookie(
            key="Authorization",
            value=logout_response["body"]["access_token"],
            httponly=True,
        )

    return logout_response
