import json

import pytest
import requests
from starlette.testclient import TestClient

from app.core import config
from app.main import app
from app.models.diagnoses import Diagnoses, Diagnosis, DiagnosisOut

diagnosis1 = DiagnosisOut(name="abscess", probability=0.026)
diagnosis2 = DiagnosisOut(name="crohn's disease", probability=0.016)
diagnosis3 = DiagnosisOut(name="epididymitis", probability=0.013)
diagnosis4 = DiagnosisOut(name="irritable bowel syndrome", probability=0.023)
diagnosis5 = DiagnosisOut(name="parkinson's disease", probability=0.003)
diagnosis6 = DiagnosisOut(name="ulcerative colitis", probability=0.019)


existent_diagnoses = Diagnoses(
    diagnoses=[diagnosis1, diagnosis2, diagnosis3, diagnosis4, diagnosis5, diagnosis6]
)
nonexistent_diagnosis = Diagnoses(existent_diagnoses=[])

client = TestClient(app)


@pytest.mark.parametrize(
    "symptom, diagnoses",
    [("rectal pain", existent_diagnoses), ("XXX", nonexistent_diagnosis)],
)
def test_retrieve_diagnoses(server_url, symptom, diagnoses):
    full_url = f"{server_url}{config.API_V1_STR}/diagnoses/?symptoms={symptom}"
    r = client.get(full_url, headers={"content-type": "application/json"})
    assert 200 == r.status_code
    assert diagnoses.json() == json.dumps(r.json())


def test_no_symtoms_provided(server_url):
    full_url = f"{server_url}{config.API_V1_STR}/diagnoses/"
    response = client.get(full_url, headers={"content-type": "application/json"})
    assert 200 == response.status_code
    assert response.json() == {"diagnoses": []}
