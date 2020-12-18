from fastapi import APIRouter, Request

from app.api.proxy import _proxy
from app.core.config import settings
from fastapi.logger import logger
router = APIRouter()

#endpoint for user information which contains the forwarding to the auth-service
@router.put("/me")
async def update_user_me(*, request: Request):
    """Update the current user.

    Arguments:
        request {Request} -- request object (contains all data and params)

    Returns:
        [User] -- [reponse of the authentication api]
    """
    return await _proxy(request, f"{settings.DDX_AUTHENTICATION_API}/users/me")


@router.get("/me")
async def read_user_me(request: Request):
    """Returns the current user.

    Arguments:
        request {Request} -- request object (contains all data and params)

    Returns:
        [User] -- [reponse of the authentication api]
    """
    return await _proxy(request, f"{settings.DDX_AUTHENTICATION_API}/users/me")


@router.post("/open")
async def create_user_open(*, request: Request):
    logger.info('CREATE USER OPEN WAS HOOKED')
    logger.info(request)
    """Create new user without the need to be logged in.

    Arguments:
        request {Request} -- request object (contains all data and params)

    Returns:
        [User] -- [reponse of the authentication api]
    """
    return await _proxy(request, f"{settings.DDX_AUTHENTICATION_API}/users/open")
