from app import crud
from app.metainformation.MetaInformation import MetaInformation
import pytest

descriptions = crud.descriptions.get()
icd_codes = crud.icd_codes.get()
metainformation = MetaInformation(
    description_list=descriptions, icd_code_list=icd_codes
)

existent_descriptions = [
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


nonexistent_descriptions = []

existent_icd_codes = [
    {"name": "Atrial septal defect", "icd_code": "ICD-10:Q21.1"},
    {"name": "Coronary sinus atrial septal defect", "icd_code": "ICD-10:Q21.1"},
    {"name": "Secundum atrial septal defect", "icd_code": "ICD-10:Q21.1"},
    {"name": "Sinus venosus atrial septal defect", "icd_code": "ICD-10:Q21.1"},
]

nonexistent_icd_codes = []


@pytest.mark.parametrize(
    "term, descriptions",
    [("cold", existent_descriptions), ("XXX", nonexistent_descriptions)],
)
def test_get_descriptions(term, descriptions):
    assert metainformation.get_descriptions(term) == descriptions


@pytest.mark.parametrize(
    "term, icd_codes",
    [("Atrial septal defect", existent_icd_codes), ("XXX", nonexistent_icd_codes)],
)
def test_get_icd_codes(term, icd_codes):
    assert metainformation.get_icd_codes(term) == icd_codes
