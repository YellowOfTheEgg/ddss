from typing import List

from pydantic import BaseModel

#definition of objects which will be returned by the api
class Diagnosis(BaseModel):
    name: str


class DiagnosisOut(Diagnosis):
    probability: float


class Diagnoses(BaseModel):
    diagnoses: List[DiagnosisOut] = []
