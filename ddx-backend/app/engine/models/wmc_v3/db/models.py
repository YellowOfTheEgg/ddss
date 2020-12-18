from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DECIMAL

Base=declarative_base()

#these classes define the tables in the database
class NodeData(Base):
    __tablename__='node_data'
    indicator_id=Column(Integer, primary_key=True)
    indicator_name=Column(String(255), index=True,unique=True)
    anamnesis_weight=Column(DECIMAL,nullable=True)


class WeightData(Base):
    __tablename__='weight_data'
    disease_name=Column(String(255), primary_key=True)
    symptom_name=Column(String(255), primary_key=True)
    parameter_weight=Column(DECIMAL,nullable=False)
    parameter_id=Column(Integer, index=True)
    auxiliary_id=Column(Integer, index=True)

