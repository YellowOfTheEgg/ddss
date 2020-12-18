import pytest
import requests
from app.main import app
from starlette.testclient import TestClient

client = TestClient(app)


def test_create_feedback(feedback_url):
    feedback = {"rating": 5, "comment": "Accurate diagnosis"}
    response = client.post(feedback_url, json=feedback,)
    assert response.status_code == 200
    assert response.json() == feedback


def test_missing_comment(feedback_url):
    feedback = {"rating": 5}
    response = client.post(feedback_url, json=feedback,)
    assert response.status_code == 200
    assert response.json() == {"rating": 5, "comment": None}


def test_missing_rating(feedback_url):
    feedback = {"comment": "Accurate diagnosis"}
    response = client.post(feedback_url, json=feedback,)
    assert response.status_code == 422


def test_rating_less_zero(feedback_url):
    feedback = {"rating": -1}
    response = client.post(feedback_url, json=feedback,)
    message = response.json()["detail"][0]["msg"]
    assert response.status_code == 422
    assert message == "Rating must be an integer between 0 and 5"


def test_rating_greater_five(feedback_url):
    feedback = {"rating": 6}
    response = client.post(feedback_url, json=feedback,)
    message = response.json()["detail"][0]["msg"]
    assert response.status_code == 422
    assert message == "Rating must be an integer between 0 and 5"


def test_float_rating(feedback_url):
    feedback = {"rating": 2.4}
    response = client.post(feedback_url, json=feedback,)
    message = response.json()["detail"][0]["msg"]
    assert response.status_code == 422
    assert message == "Rating must be an integer between 0 and 5"


def test_string_rating(feedback_url):
    feedback = {"rating": "2"}
    response = client.post(feedback_url, json=feedback,)
    message = response.json()["detail"][0]["msg"]
    assert response.status_code == 422
    assert message == "Rating must be an integer between 0 and 5"


def test_comment_size(feedback_url):
    feedback = {
        "rating": 4,
        "comment": "Natoque penatibus et magnis dis parturient montes. Ac turpis egestas maecenas pharetra convallis posuere morbi leo urna. Volutpat sed cras ornare arcu dui vivamus arcu felis bibendum. Accumsan sit amet nulla facilisi. Massa tincidunt nunc pulvinar sapien et ligula. Ac turpis egestas sed tempus urna et pharetra pharetra massa. Condimentum mattis pellentesque id nibh tortor id. Volutpat sed cras ornare arcu dui vivamus arcu felis bibendum. Dignissim suspendisse in est ante in. Ut diam quam nulla porttitor massa. Quis commodo odio aenean sed adipiscing diam donec adipiscing.",
    }
    response = client.post(feedback_url, json=feedback,)
    message = response.json()["detail"][0]["msg"]
    assert response.status_code == 422
    assert message == "Comment exceeds 400 characters limit"
