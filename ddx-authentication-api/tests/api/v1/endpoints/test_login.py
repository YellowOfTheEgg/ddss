import pytest
from fastapi.testclient import TestClient

from app.core.config import settings


@pytest.mark.skipif(
    not settings.INTEGRATION_TESTS, reason="run only in development envirnoment"
)
def test_get_access_token(client: TestClient) -> None:
    login_data = {
        "username": settings.FIRST_SUPERUSER,
        "password": settings.FIRST_SUPERUSER_PASSWORD,
    }
    r = client.post(f"{settings.API_V1_STR}/login/access-token", data=login_data)
    tokens = r.json()
    assert r.status_code == 200
    assert "access_token" in tokens
    assert tokens["access_token"]
