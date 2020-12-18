from datetime import timedelta
from typing import Any

from fastapi import APIRouter, Body, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app import crud
from app import models as schemas
from app.api import deps
from app.core import security
from app.core.config import settings
from app.core.security import get_password_hash
from app.models import db as models

router = APIRouter()

# endpoint for user-logout
@router.post("/logout/", response_model=schemas.Token)
def logout() -> Any:
  
    return {
        "access_token": '',
        "token_type": "bearer",
    }
