import pytest
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app import crud
from app import models as schemas
from app.core.config import settings
from app.core.security import verify_password
from app.models import db as models
from app.models.user import UserCreate, UserUpdate
from tests.utils.utils import random_email, random_lower_string


@pytest.mark.skipif(
    not settings.INTEGRATION_TESTS, reason="run only in development envirnoment"
)
def test_create_user(db: Session) -> None:
    email = random_email()
    password = random_lower_string()
    user_in = UserCreate(email=email, password=password)
    user = crud.user.create(db, obj_in=user_in)
    assert user.email == email
    assert hasattr(user, "hashed_password")


@pytest.mark.skipif(
    not settings.INTEGRATION_TESTS, reason="run only in development envirnoment"
)
def test_authenticate_user(db: Session) -> None:
    email = random_email()
    password = random_lower_string()
    user_in = UserCreate(email=email, password=password)
    user = crud.user.create(db, obj_in=user_in)
    authenticated_user = crud.user.authenticate(db, email=email, password=password)
    assert authenticated_user
    assert user.email == authenticated_user.email


@pytest.mark.skipif(
    not settings.INTEGRATION_TESTS, reason="run only in development envirnoment"
)
def test_not_authenticate_user(db: Session) -> None:
    email = random_email()
    password = random_lower_string()
    user = crud.user.authenticate(db, email=email, password=password)
    assert user is None


@pytest.mark.skipif(
    not settings.INTEGRATION_TESTS, reason="run only in development envirnoment"
)
def test_check_if_user_is_active(db: Session) -> None:
    email = random_email()
    password = random_lower_string()
    user_in = UserCreate(email=email, password=password)
    user = crud.user.create(db, obj_in=user_in)
    is_active = crud.user.is_active(user)
    assert is_active is True


@pytest.mark.skipif(
    not settings.INTEGRATION_TESTS, reason="run only in development envirnoment"
)
def test_check_if_user_is_active_inactive(db: Session) -> None:
    email = random_email()
    password = random_lower_string()
    user_in = UserCreate(email=email, password=password, disabled=True)
    user = crud.user.create(db, obj_in=user_in)
    is_active = crud.user.is_active(user)
    assert is_active


@pytest.mark.skipif(
    not settings.INTEGRATION_TESTS, reason="run only in development envirnoment"
)
def test_check_if_user_is_superuser(db: Session) -> None:
    email = random_email()
    password = random_lower_string()
    user_in = UserCreate(email=email, password=password, is_superuser=True)
    user = crud.user.create(db, obj_in=user_in)
    is_superuser = crud.user.is_superuser(user)
    assert is_superuser is True


@pytest.mark.skipif(
    not settings.INTEGRATION_TESTS, reason="run only in development envirnoment"
)
def test_check_if_user_is_superuser_normal_user(db: Session) -> None:
    username = random_email()
    password = random_lower_string()
    user_in = UserCreate(email=username, password=password)
    user = crud.user.create(db, obj_in=user_in)
    is_superuser = crud.user.is_superuser(user)
    assert is_superuser is False


@pytest.mark.skipif(
    not settings.INTEGRATION_TESTS, reason="run only in development envirnoment"
)
def test_get_user(db: Session) -> None:
    password = random_lower_string()
    username = random_email()
    user_in = UserCreate(email=username, password=password, is_superuser=True)
    user = crud.user.create(db, obj_in=user_in)
    user_2 = crud.user.get(db, id=user.id)
    assert user_2
    assert user.email == user_2.email
    assert jsonable_encoder(user) == jsonable_encoder(user_2)


@pytest.mark.skipif(
    not settings.INTEGRATION_TESTS, reason="run only in development envirnoment"
)
def test_update_user(db: Session) -> None:
    password = random_lower_string()
    email = random_email()
    user_in = UserCreate(email=email, password=password, is_superuser=True)
    user = crud.user.create(db, obj_in=user_in)
    new_password = random_lower_string()
    user_in_update = UserUpdate(password=new_password, is_superuser=True)
    crud.user.update(db, db_obj=user, obj_in=user_in_update)
    user_2 = crud.user.get(db, id=user.id)
    assert user_2
    assert user.email == user_2.email
    assert verify_password(new_password, user_2.hashed_password)
