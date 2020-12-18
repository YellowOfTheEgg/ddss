from app.engine.models.wmc_v3.models.weight_data import WeightDataUpdate, WeightDataCreate
from sqlalchemy.orm import Session,aliased
from typing import Any, Dict, Optional, Union
from app.engine.models.wmc_v3.crud.base import CRUDBase
from sqlalchemy import desc, or_, func, and_
from app.engine.models.wmc_v3.db.models import WeightData
from app.engine.models.wmc_v3.crud.utils import get_max_id


# CRUDNodeData  summarizes sql-queries for the table weight_data of the database
class CRUDWeightData(CRUDBase[WeightData,WeightDataCreate,WeightDataUpdate]):
    #for symptom_requester
    def get_intersection_by_symptom_names(self, db:Session,*,symptom_names:[str]):        
        res = db.query(WeightData).\
                filter(or_(WeightData.symptom_name==symptom_name for symptom_name in symptom_names)).\
                with_entities(WeightData.disease_name, func.count(WeightData.disease_name)).\
                group_by(WeightData.disease_name).\
                having(func.count(WeightData.disease_name)==len(symptom_names)).\
                all()        
        return res

    #for symptom_requester
    def get_most_likely_symptom_by_disease_names(self, db:Session,*,disease_names:[str],ignore_symptom_names:[str]):        
        res = db.query(WeightData).\
            filter(or_(WeightData.disease_name==disease_name for disease_name in disease_names)).\
                filter(and_(WeightData.symptom_name!=symptom_name for symptom_name in ignore_symptom_names)).\
                    with_entities(WeightData.symptom_name, WeightData.parameter_weight).\
                    group_by(WeightData.symptom_name, WeightData.parameter_weight).\
                        order_by(WeightData.parameter_weight.desc()).first()        
        return res



    def get_weight_data_by_symptom_names(self, db:Session,*,symptom_names:[str])->[WeightData]:
        return db.query(WeightData).filter(
            or_(WeightData.symptom_name==symptom_name for symptom_name in symptom_names)).all()

   
    def get_indifferent_symptoms(self, db:Session,*,true_symptoms:[str]):        
        #weight_data_b = aliased(WeightData)        
        #qry = db.query(WeightData).join(weight_data_b, WeightData.disease_name==weight_data_b.disease_name).with_entities(weight_data_b.symptom_name).filter(or_(WeightData.symptom_name==true_symptom for true_symptom in true_symptoms)).filter(and_(weight_data_b.symptom_name!=true_symptom for true_symptom in true_symptoms))
        qry = db.query(WeightData).filter(and_(WeightData.symptom_name!=true_symptom for true_symptom in true_symptoms)).with_entities(WeightData.symptom_name)
        #print(qry)
        res=qry.all()

        return [r[0] for r in res]        

 
    def create(self, db:Session, *, obj_in:WeightData)->WeightData:
        db_obj = WeightData(
                        disease_name=obj_in.disease_name, 
                        symptom_name=obj_in.symptom_name,
                        parameter_weight=obj_in.parameter_weight,
                        parameter_id=obj_in.parameter_id,
                        auxiliary_id=obj_in.auxiliary_id
                        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def create_one(self, db:Session,*,obj_in:WeightData)->WeightData:
        current_parameter_id=get_max_id(db)+1
        current_auxiliary_id = current_parameter_id+1
        obj_in.parameter_id=current_parameter_id
        obj_in.auxiliary_id=current_auxiliary_id
        db_obj=self.create(db=db,obj_in=obj_in)
        return db_obj

    def create_all(self, db:Session,*,objs_in:[WeightDataCreate])->[WeightData]:
        current_parameter_id=get_max_id(db)+1
        current_auxiliary_id=len(objs_in)+current_parameter_id
       

        db_objs=[]
        for obj_in in objs_in:
            obj_in.parameter_id=current_parameter_id
            obj_in.auxiliary_id=current_auxiliary_id
            db_obj=self.create(db=db, obj_in=obj_in)
            db_objs.append(db_obj)
            current_parameter_id+=1
            current_auxiliary_id+=1
        return db_objs

weight_data=CRUDWeightData(WeightData)
