from app.engine.models.wmc_v3.db.models import NodeData,WeightData
from sqlalchemy.orm import Session
from sqlalchemy import desc

#get_max_id is a additional function, which returns the max of auxiliary_ids, parameter_ids and indicator_ids
#this function is needed for insertion of new data
def get_max_id(db:Session):
    indicator_res=db.query(NodeData).order_by(desc(NodeData.indicator_id)).first()
    parameter_res=db.query(WeightData).order_by(desc(WeightData.parameter_id)).first()
    auxiliary_res=db.query(WeightData).order_by(desc(WeightData.auxiliary_id)).first()
    max_id = 0
    if indicator_res is not None and parameter_res is not None:
        max_id=max([indicator_res.indicator_id, parameter_res.parameter_id, auxiliary_res.auxiliary_id])
    elif indicator_res is not None:
        max_id=indicator_res.indicator_id
    elif parameter_res is not None:
        max_id=max([parameter_res.parameter_id,auxiliary_res.auxiliary_id])
    return max_id