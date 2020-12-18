from app import crud
from app.autocomplete.autocompleter import Autocompleter

symptoms = crud.symptoms.get()
autocompleter = Autocompleter(symptoms)


def test_get_matching_symptoms():
    matches = autocompleter.complete("headache")
    assert matches == [
        "headache",
        "severe headache",
        "persistent headache",
        "throbbing headache",
    ]


def test_none_matching_symptoms():
    matches = autocompleter.complete("forehead pain")
    assert matches == []
