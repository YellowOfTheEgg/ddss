from typing import List

from pydantic import BaseModel

class Symptom(BaseModel):
    symptom: str

class Symptoms(BaseModel):
    symptoms: List[str]
