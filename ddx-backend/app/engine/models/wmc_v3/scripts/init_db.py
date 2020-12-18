import pathlib
print(pathlib.Path(__file__).absolute())
from app.engine.models.wmc_v3.db.session import Session, engine
from app.engine.models.wmc_v3.db.models import Base
from app.engine.models.wmc_v3.scripts.knowledge import Knowledge
from app.engine.models.wmc_v3.db.models import NodeData, WeightData
import app.engine.models.wmc_v3.models as schemas
import os
import app.engine.models.wmc_v3.crud as crud



knowledge=Knowledge()

#this function loads the knowledgebase from the .csv file into postgress
def init_db(db:Session)->None:
  
    indicator_names=knowledge.get_entry_list()
    node_datas=list(map(lambda k: schemas.NodeDataCreate(indicator_name=k), indicator_names))
    crud.node_data.create_all(db,objs_in=node_datas)
    weight_information=knowledge.get_weight_rows()
    weight_data=list(map(lambda w: schemas.WeightDataCreate(disease_name=w[0],symptom_name=w[1],parameter_weight=w[2]),weight_information))
    crud.weight_data.create_all(db,objs_in=weight_data)


if __name__=='__main__':
    db=Session()
    Base.metadata.create_all(engine)
    init_db(db)