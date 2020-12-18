import pytest
from app.core import config
from app.main import app
from starlette.testclient import TestClient
import json

client = TestClient(app)

existent_icd_codes = {
    "icd_codes": [
        {"name": "Atrial septal defect", "icd_code": "ICD-10:Q21.1"},
        {"name": "Coronary sinus atrial septal defect", "icd_code": "ICD-10:Q21.1"},
        {"name": "Secundum atrial septal defect", "icd_code": "ICD-10:Q21.1"},
        {"name": "Sinus venosus atrial septal defect", "icd_code": "ICD-10:Q21.1"},
    ]
}

nonexistent_icd_codes = {"icd_codes": []}


@pytest.mark.parametrize(
    "term, icd_codes",
    [("Atrial septal defect", existent_icd_codes), ("XXX", nonexistent_icd_codes)],
)
def test_retrieve_icd_codes(server_url, term, icd_codes):
    full_url = f"{server_url}{config.API_V1_STR}/icd_codes/?search_term={term}"
    r = client.get(full_url, headers={"content-type": "application/json"})
    assert 200 == r.status_code
    assert json.dumps(icd_codes) == json.dumps(r.json())
