from sqlalchemy.orm import Session

from app import crud
from app import models as schemas
from app.core.config import settings
from app.db import base  # noqa: F401
from app.models import db as models

# make sure all SQL Alchemy models are imported (app.db.base) before initializing DB
# otherwise, SQL Alchemy might fail to initialize relationships properly
# for more details: https://github.com/tiangolo/full-stack-fastapi-postgresql/issues/28

#db-initialization
def init_db(db: Session) -> None:
    """Initializes the database by creating the first super user.
    Notice that the tables should be created with Alembic migrations before.
    """
    user = crud.user.get_by_email(db, email=settings.FIRST_SUPERUSER)
    if not user:
        user_in = schemas.UserCreate(
            email=settings.FIRST_SUPERUSER,
            password=settings.FIRST_SUPERUSER_PASSWORD,
            is_superuser=True,
        )
        user = crud.user.create(db, obj_in=user_in)  # noqa: F841
