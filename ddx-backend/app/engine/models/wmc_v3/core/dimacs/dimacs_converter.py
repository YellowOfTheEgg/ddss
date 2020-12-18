import math
import app.engine.models.wmc_v3.crud as crud
from app.engine.models.wmc_v3.core.dimacs.dimacs_present import get_bodies_for_present_symptom
from app.engine.models.wmc_v3.core.dimacs.dimacs_absent import create_body_for_absent_symptoms
from app.engine.models.wmc_v3.core.dimacs.dimacs_weights import create_weights
from app.engine.models.wmc_v3.db.session import Session
from app.engine.models.wmc_v3.models.wmc_variable import WmcVariable
import itertools
from app.engine.models.wmc_v3.db.session import Session
from fastapi.logger import logger

#This file creates WMC1-Encoding in DIMACS-Format based on given symptoms and the data from the knowledge-base

#The decreasion of dimacs ids (parameter_ids, aux_ids and indicator_ids) is needed because cachet will not work otherwise
def decrease_variable_ids(dimacs_body: [[WmcVariable]])->[[WmcVariable]]:
    wmc_vars = [item for sublist in dimacs_body for item in sublist]
    unique = set(wmc_vars)
   
    sorted_vars = sorted(unique)
    id_counter = 1
    id_map = {}
    for wmc_var in sorted_vars:
        id_map[wmc_var.id] = id_counter
        id_counter += 1
    decreased_id_body = []
    for dnf in dimacs_body:
        decreased_dnf = []
        for literal in dnf:
            decreased_wmc_var = WmcVariable(
                id=id_map.get(literal.id),
                negation=literal.negation,
                weight=literal.weight,
            )
            decreased_dnf.append(decreased_wmc_var)
        decreased_id_body.append(decreased_dnf)
    return decreased_id_body

#Creates a human-readable format from dimacs
def dimacs_to_readable(dimacs_expression):
    def wmc_var_to_str(literal, prefix=''):
        literal_str=''
        if literal.type=='indicator' and literal.negation==True:
            literal_str=f' {prefix} not I_{literal.indicator_name}'
        elif literal.type=='indicator' and literal.negation==False:
            literal_str=f' {prefix} I_{literal.indicator_name}'
        elif literal.type=='auxiliary' and literal.negation==True:
            literal_str=f' {prefix} not W_{literal.disease_name}/{literal.symptom_name}'
        elif literal.type=='auxiliary' and literal.negation==False:
            literal_str=f' {prefix} W_{literal.disease_name}/{literal.symptom_name}'
        elif literal.type=='parameter' and literal.negation==True:
            literal_str=f' {prefix} not P_{literal.disease_name}/{literal.symptom_name}'
        elif literal.type=='parameter' and literal.negation==False:
            literal_str=f' {prefix} P_{literal.disease_name}/{literal.symptom_name}'
        else:
            literal_str=f"WHAT IS ABOUT {literal} ????"
        return literal_str

    res=''
    for row in dimacs_expression:
        row_str='('
        first=True
        for literal in row:
            if first:
                first=False
                row_str += wmc_var_to_str(literal)
            else:
                row_str += wmc_var_to_str(literal,prefix='V')
        row_str+=" )\n"
        res+=f" ^ {row_str}"
    return res


#creates dimacs-string from a given array of objects
def create_dimacs_string(dimacs_weights:[int], dimacs_body:[[WmcVariable]])->str:
    number_of_literals = len(set([item for sublist in dimacs_body for item in sublist]))
    number_of_clauses = len(dimacs_body)
    dimacs_header = f"p cnf {number_of_literals} {number_of_clauses}"   
    dimacs_weights_str = "w " + " ".join(map(str, dimacs_weights))
    dimacs_body_str = ""
    for dnf in dimacs_body:
        if len(dnf)>0:
            dnf_str = " ".join(map(str, dnf))
            dimacs_body_str += f"\n{dnf_str} 0"
    dimacs_str = dimacs_header + "\n" + dimacs_weights_str + dimacs_body_str
    return dimacs_str

#creates dimacs body for diseases
def create_body_priors(db: Session, disease: str) -> [[WmcVariable]]:    
    indicator_var = crud.node_data.get_by_indicator_name(db=db,indicator_name=disease)
    return [WmcVariable(id=indicator_var.indicator_id, weight=1)]
    

#creates the whole dimacs-string based on knowledgebase data, given symptoms and optionaly given disease
def run(symptom_names,parameter_t ,disease):
    
    threshold=parameter_t
    priors=[]
    
    if disease is not None:
        priors=create_body_priors(db=Session(),disease=disease)   
    indifferent_symptoms = crud.weight_data.get_indifferent_symptoms(db=Session(), true_symptoms=symptom_names)
    indif_wmc_vars = crud.wmc_variable.get_by_symptom_names(db=Session(), symptom_names=indifferent_symptoms)
    body_for_absent_symptoms=create_body_for_absent_symptoms(indif_wmc_vars)
    present_symptoms_bodies = []
    for symptom_name in symptom_names:        
        wmc_weights = crud.wmc_variable.get_by_symptom_names(db=Session(), symptom_names=[symptom_name])
        bodies_for_present_symptom=get_bodies_for_present_symptom(wmc_weights, threshold)
        present_symptoms_bodies.append(bodies_for_present_symptom)
    combs_of_present_bodies = list(itertools.product(*present_symptoms_bodies))
    cnfs=[]
   
    for comb in combs_of_present_bodies:
        comb_sum=[]
        for cnf in comb:
            comb_sum+=cnf          
        comb_sum+=body_for_absent_symptoms
        if len(priors)>0:
            comb_sum.append(priors)      
        weights=create_weights(comb_sum)
        full_body=decrease_variable_ids(comb_sum)
        dimacs_str=create_dimacs_string(weights,full_body)
        readable_dimacs=dimacs_to_readable(full_body)       
        cnfs.append(dimacs_str)

    return cnfs