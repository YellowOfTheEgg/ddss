import pytest
from app.core import config
from app.main import app
from starlette.testclient import TestClient
import json

client = TestClient(app)

existent_descriptions = {
    "descriptions": [
        {
            "name": "Cold paresis",
            "description": "Increased muscle weakness upon exposure to cold temperatures.",
        },
        {
            "name": "Cold urticaria",
            "description": "Urticaria may be caused by cold temperatures.",
        },
        {
            "name": "Cold-induced hemolysis",
            "description": "A form of hemolytic anemia that can be triggered by cold temperatures.",
        },
        {
            "name": "Cold-induced muscle cramps",
            "description": "Sudden and involuntary contractions of one or more muscles brought on by exposure to cold temperatures.",
        },
        {
            "name": "Cold-induced sweating",
            "description": "Sweating provoked by cold temperature rather than by heat.",
        },
        {
            "name": "Cold-sensitive myotonia",
            "description": "An involuntary and painless delay in the relaxation of skeletal muscle following contraction or electrical stimulation that is induced by exposure to cold.",
        },
        {
            "name": "Triggered by cold",
            "description": "Applies to a sign or symptom that is provoked or brought about by exposure to cold surroundings.",
        },
    ]
}

nonexistent_descriptions = {"descriptions": []}


@pytest.mark.parametrize(
    "term, descriptions",
    [("cold", existent_descriptions), ("XXX", nonexistent_descriptions)],
)
def test_retrieve_descriptions(server_url, term, descriptions):
    full_url = f"{server_url}{config.API_V1_STR}/descriptions/?search_term={term}"
    r = client.get(full_url, headers={"content-type": "application/json"})
    assert 200 == r.status_code
    assert json.dumps(descriptions) == json.dumps(r.json())
