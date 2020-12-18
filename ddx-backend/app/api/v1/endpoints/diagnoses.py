from typing import List

from fastapi import APIRouter, HTTPException, Query


from app.engine.ddx import ddx_wmc_v3
from app.models.diagnoses import Diagnoses, Diagnosis, DiagnosisOut

router = APIRouter()


#definition of the get diagnoses-endpoint. This endpoint returns all diagnoses based on given symptoms
@router.get("/", response_model=Diagnoses)
def get_diagnoses(symptoms: List[str] = Query(None), model: str = 'wmc_v3', parameter_t:int=15):
    if not symptoms:
        return Diagnoses(diagnoses=[])
    ddx_result=ddx_wmc_v3(symptoms,parameter_t)
    

    diagnosis_list = list(
        map(lambda d: DiagnosisOut(name=d, probability=ddx_result[d]), ddx_result)
    )
    diagnoses = Diagnoses(diagnoses=diagnosis_list)
    return diagnoses
