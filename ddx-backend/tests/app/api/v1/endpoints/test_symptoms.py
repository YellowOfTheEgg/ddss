import pytest
import requests
from starlette.testclient import TestClient

from app.core import config
from app.main import app
from app.models.symptoms import Symptoms

client = TestClient(app)


def test_retrieve_symptoms(server_url):
    search_term = "toe"
    full_url = f"{server_url}{config.API_V1_STR}/symptoms/?search_term={search_term}"
    response = client.get(full_url, headers={"content-type": "application/json"})
    symptoms = response.json()["symptoms"]
    assert 200 == response.status_code
    assert symptoms[0] == "toe pain"
