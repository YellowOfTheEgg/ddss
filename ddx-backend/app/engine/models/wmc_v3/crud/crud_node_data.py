from app.engine.models.wmc_v3.models.node_data import NodeDataUpdate, NodeDataCreate
from app.engine.models.wmc_v3.db.models import NodeData,WeightData
from sqlalchemy.orm import Session
from typing import Any, Dict, Optional, Union
from app.engine.models.wmc_v3.crud.base import CRUDBase
from app.engine.models.wmc_v3.crud.utils import get_max_id
from sqlalchemy import desc


# CRUDNodeData  summarizes sql-queries for the table node_data of the database
class CRUDNodeData(CRUDBase[NodeData, NodeDataCreate,NodeDataUpdate]):
    
    def get_by_indicator_name(self, db: Session, *, indicator_name: str) -> Optional[NodeData]:
        qry=db.query(NodeData).filter(NodeData.indicator_name == indicator_name)       
        return qry.first()


    

    def create(self, db:Session, *, obj_in:NodeDataCreate)->NodeData:
        db_obj = NodeData(indicator_name=obj_in.indicator_name, indicator_id=obj_in.indicator_id)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj


    def create_one(self, db:Session, *, obj_in:NodeDataCreate)->NodeData:
        id_count=get_max_id(db)+1
        obj_in.indicator_id= id_count
        db_obj=self.create(db=db,obj_in=obj_in)        
        return db_obj


    def create_all(self, db:Session, *, objs_in:[NodeDataCreate])->[NodeData]:
        id_count=get_max_id(db)+1
        db_objs=[]
        for obj_in in objs_in:
            obj_in.indicator_id=id_count
            db_obj=self.create(db=db,obj_in=obj_in)
            db_objs.append(db_obj)
            id_count+=1
        return db_objs
        

node_data=CRUDNodeData(NodeData)