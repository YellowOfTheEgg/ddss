from pydantic import BaseModel
from typing import Optional
from decimal import Decimal
#this are classes for structuring information about a literal. Objects of these classes are used for creating the WMC1-Encoding
class WmcVariableBase(BaseModel):    
    id:Optional[int]=None
    negation:Optional[bool]=None
    type:Optional[str]=None    
    weight:Optional[Decimal]=None
    indicator_name:Optional[str]=None
    disease_name:Optional[str]=None
    symptom_name:Optional[str]=None


class WmcVariable(WmcVariableBase):
    def __lt__(self, other):
        return self.id<other.id
    
    def __eq__(self, other):
        return (self.id==other.id and self.__class__==other.__class__)
    def __hash__(self):
        return hash(self.id)   
    
    def __str__(self):
        if self.negation:
            return str(-1*self.id)
        else:
            return str(self.id)
    pass
