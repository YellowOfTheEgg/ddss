from app.engine.models.wmc_v3.db.models import NodeData, WeightData
from sqlalchemy.orm import Session
from typing import Any, Dict, Optional, Union
from app.engine.models.wmc_v3.crud.base import CRUDBase
from sqlalchemy import desc, or_, func
from app.engine.models.wmc_v3.models.weight_data import WeightDataUpdate, WeightDataCreate
from fastapi.logger import logger as fastapi_logger


#this class summarizes all function which contain joins between node and weight data
class CRUDWmcVariable(CRUDBase[WeightData, WeightDataUpdate, WeightDataCreate]):
    #all diseases which have one or more of given symptoms (version before rework)
    #for the wmc-model
    def get_by_symptom_names(self, db: Session, symptom_names: [str]):
        qry= db.query(WeightData).with_entities(
                WeightData.symptom_name,
                WeightData.disease_name,
                WeightData.parameter_id,
                WeightData.auxiliary_id,
                NodeData.indicator_id,
                NodeData.indicator_name,
                WeightData.parameter_weight,
            ).join(
                NodeData,
                WeightData.disease_name == NodeData.indicator_name,
                isouter=True
            ).filter(
                or_(
                    WeightData.symptom_name == symptom_name
                    for symptom_name in symptom_names
                )
            )        
        return qry.all()


wmc_variable=CRUDWmcVariable(WeightData)