import pytest

from app import crud
from app.core import config


@pytest.fixture(scope="module")
def server_url():
    return f"http://{config.SERVER_NAME}:8000"

@pytest.fixture(scope="module")
def feedback_url():
    return f"http://{config.SERVER_NAME}:8000{config.API_V1_STR}/feedback/"

@pytest.fixture(scope="module")
def knowledge_base():
    return crud.knowledge_base.get()
