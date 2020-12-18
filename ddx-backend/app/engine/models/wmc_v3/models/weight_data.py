from pydantic import BaseModel
from typing import Optional
from decimal import Decimal
#this are classes for structuring information about a literal. Objects of these classes are used for creating the WMC1-Encoding
class WeightDataBase(BaseModel):    
    disease_name:Optional[str]=None
    symptom_name:Optional[str]=None
    parameter_weight:Optional[Decimal]=None
    parameter_id:Optional[int]=None
    auxiliary_id:Optional[int]=None

class WeightData(WeightDataBase):
    pass

class WeightDataUpdate(WeightDataBase):
    disease_name:str
    symptom_name:str
    parameter_weight:Decimal

class WeightDataCreate(WeightDataBase):
    disease_name:str
    symptom_name:str
    parameter_weight:Decimal