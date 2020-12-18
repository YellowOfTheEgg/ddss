from pydantic import BaseModel

#definition of objects which will be returned by the api
class Wmc(BaseModel):
    probability: float
    runtime: float