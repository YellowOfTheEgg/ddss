from fastapi import APIRouter, Query
from fastapi.logger import logger as fastapi_logger
from app import crud
from app.autocomplete.autocompleter import Autocompleter
from app.models.symptoms import Symptoms

router = APIRouter()
symptoms = crud.symptoms.get()
completer = Autocompleter(symptoms)

#endpoint for getting symptoms based on given strings
@router.get("/", response_model=Symptoms)
def get_symptoms(search_term: str = None):
    
    if not search_term:
        return Symptoms(symptoms=symptoms)

    matches = completer.complete(search_term)

    return Symptoms(symptoms=matches)

