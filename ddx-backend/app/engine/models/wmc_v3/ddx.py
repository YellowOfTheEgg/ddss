from app.engine.models.wmc_v3.core.wmc_solver import solve
import app.engine.models.wmc_v3.crud as crud
from app.engine.models.wmc_v3.db.session import Session


#definition of a kind of interface-functions. The API will access the WMC-Module via these functions

#ddx calculates probability for all diseases which are connected with given symptoms by running the wmc1-Zerlegung for symptoms and for symptoms with a given disase
def ddx(symptoms, parameter_t):    
    weight_data_rows=crud.weight_data.get_weight_data_by_symptom_names(db=Session(),symptom_names=symptoms)
    result={}   
    denominator_dict = solve(symptoms,parameter_t)
    denominator=denominator_dict['probability']
    for weight_data in weight_data_rows:
        numerator_dict = solve(symptoms,parameter_t, weight_data.disease_name)
        numerator=numerator_dict['probability']
        result[weight_data.disease_name] = numerator/denominator       
    return result

#wmc calculates only the wmc of giving symptoms (which is the denominator in the upper case)
#this function was used for the evaluation part of the master thesis
def wmc(symptoms,parameter_t):
    return solve(symptoms,parameter_t)