from fastapi import APIRouter, Request, Response
from app.api.proxy import _proxy
from app.core.config import settings
from fastapi.logger import logger

router = APIRouter()

#endpoint for user-login which contains the forwarding to the auth-service
@router.post("/login/access-token")
async def login_access_token(request: Request, response: Response):
    """OAuth2 compatible token login, get an access token for future requests

    Arguments:
        request {Request} -- [request object containing credentials]

    Returns:
        [Token] -- [Token object containing the JWT token]
    """
    
    login_response = await _proxy(
        request, f"{settings.DDX_AUTHENTICATION_API}/login/access-token"
    )
   
    if login_response["status_code"] == 200:
        response.set_cookie(
            key="Authorization",
            value=login_response["body"]["access_token"],
            httponly=True,
        )

    return login_response
