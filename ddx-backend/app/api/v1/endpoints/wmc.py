from typing import List

from fastapi import APIRouter, HTTPException, Query

from app.engine.ddx import wmc_v3
from app.models.wmc import Wmc

router = APIRouter()

#definition of the get wmc-endpoint. This endpoint returns the WMC based on given symptoms
@router.get("/", response_model=Wmc)
def get_wmc(symptoms: List[str] = Query(None), parameter_t: int=15):
    if not symptoms:
        return Wmc(probability=-1)

    
    ddx_result=wmc_v3(symptoms,parameter_t)
   
    return Wmc(probability=ddx_result['probability'],runtime=ddx_result['runtime'])