from pydantic import BaseModel
from typing import Optional
from decimal import Decimal

#this are classes for structuring information about a literal. Objects of these classes are used for creating the WMC1-Encoding
class NodeDataBase(BaseModel):
    indicator_name: Optional[str]=None
    indicator_id: Optional[int]=None
    anamnesis_weight:Optional[Decimal]=None


class NodeDataCreate(NodeDataBase):
    indicator_name:str
    

class NodeDataUpdate(NodeDataBase):
    indicator_name:Optional[str]
    anamnesis_weight:Optional[Decimal]

class NodeData(NodeDataBase):
    pass