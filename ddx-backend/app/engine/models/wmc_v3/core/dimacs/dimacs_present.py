import app.engine.models.wmc_v3.crud as crud
from app.engine.models.wmc_v3.models.wmc_variable import WmcVariable
import math
import numpy as np
import itertools
from fastapi.logger import logger

#these functions create the parts of the WMC1-Encoding for given symptoms. The clause enumeration is based on the WMC1-Formula in the masterthesis

def create_first_clause(wmc_vars, stable_clause_ids,threshold):
 #allready optimized: roundup(20/18)=2 => array with two entries, both have 9 entries
 
#    def split_clause(first_clause,threshold):
#        dnf_len=len(first_clause)       
#        num_of_clauses=math.ceil(dnf_len/threshold)    
#        splitted=np.array_split(first_clause,num_of_clauses)    
#        return list(map(lambda arr: list(arr), splitted))

    #without optimization
    
    def split_clause(first_clause,treshhold):
        res=[]
        for i in range(0,len(first_clause),treshhold):
            el=list(first_clause[i:i+treshhold])
            res.append(el)
        return res

    def create_opt_expression(splitted_clause, stable_clause_ids):
        result = []
        for clause_id in stable_clause_ids:
            result.append(splitted_clause[clause_id])
        clause_ids=range(len(splitted_clause))
        unstable_clause_ids=set(clause_ids)-set(stable_clause_ids)
        for clause_id in unstable_clause_ids:
            unstable_clause=splitted_clause[clause_id]
            for literal in unstable_clause:
                literal.negation=True
                result.append([literal])
        return result
   
    first_clause = list(
        map(lambda wmc_var: WmcVariable(
                id = wmc_var.auxiliary_id, 
                negation = False, 
                weight = 1, 
                type = "auxiliary", 
                disease_name = wmc_var.disease_name, 
                symptom_name = wmc_var.symptom_name
            ),
            wmc_vars)
    )
 
    if len(first_clause)>threshold:
        splitted_clause = split_clause(first_clause,threshold)
        first_clause = create_opt_expression(splitted_clause, stable_clause_ids)
    else:
        first_clause=[first_clause]    
    return first_clause

def create_second_clause(wmc_var):
    return [
            WmcVariable(
                id=wmc_var.indicator_id, negation=True, weight=1, type="indicator", indicator_name=wmc_var.indicator_name
            ),
            WmcVariable(
                id=wmc_var.parameter_id,
                negation=True,
                weight=wmc_var.parameter_weight,
                type="parameter",
                disease_name=wmc_var.disease_name, 
                symptom_name=wmc_var.symptom_name
            ),
            WmcVariable(
                id=wmc_var.auxiliary_id, weight=1, negation=False, type="auxiliary",disease_name=wmc_var.disease_name, symptom_name=wmc_var.symptom_name
            ),
        ]

def create_third_clause(wmc_var):
    return [
            WmcVariable(
                id=wmc_var.indicator_id, negation=False, weight=1, type="indicator", indicator_name=wmc_var.indicator_name
            ),
            WmcVariable(
                id=wmc_var.auxiliary_id, weight=1, negation=True, type="auxiliary",disease_name=wmc_var.disease_name, symptom_name=wmc_var.symptom_name
            ),
        ]

def create_fourth_clause(wmc_var):
    return [
            WmcVariable(
                id=wmc_var.parameter_id,
                negation=False,
                weight=wmc_var.parameter_weight,
                type="parameter",
                disease_name=wmc_var.disease_name, 
                symptom_name=wmc_var.symptom_name
            ),
            WmcVariable(
                id=wmc_var.auxiliary_id, negation=True, weight=1, type="auxiliary",disease_name=wmc_var.disease_name, symptom_name=wmc_var.symptom_name
            ),
        ]
#creates the part of WMC1-Encoding for one element of WMC1-Zerlegung in DIMACS-Format
def create_body_for_present_symptom(wmc_vars, stable_clause_ids, threshold) -> [[WmcVariable]]:
    expression = []   
    symptom_name=wmc_vars[0].symptom_name

    first_clause = create_first_clause(wmc_vars,stable_clause_ids,threshold)
    
    expression=first_clause    
    for wmc_var in wmc_vars:
        second_clause = create_second_clause(wmc_var) 
    
        third_clause = create_third_clause(wmc_var)
        fourth_clause = create_fourth_clause(wmc_var)
        expression.extend([second_clause, third_clause, fourth_clause])    
   
    return expression


#creates the part of WMC1-Encoding for present symptoms in DIMACS-Format
#here the WMC1-Zerlegung is performed
def get_bodies_for_present_symptom(wmc_weights,threshold):
    stable_clause_ids_tpl=[]    
    if len(wmc_weights)>threshold:
            number_of_clauses = math.ceil(len(wmc_weights)/threshold)
            clause_ids = range(number_of_clauses)            
            for r in range(1,number_of_clauses):
                    stable_clause_ids_tpl+=list(itertools.combinations(clause_ids, r))            
    else:
        stable_clause_ids_tpl=[(1,)]    
    bodies_for_present_symptom=[]
    for stable_clause_ids in stable_clause_ids_tpl:
        body_for_present_symptoms = create_body_for_present_symptom(wmc_weights,stable_clause_ids,threshold)        
        bodies_for_present_symptom.append(body_for_present_symptoms)    
       
    return bodies_for_present_symptom