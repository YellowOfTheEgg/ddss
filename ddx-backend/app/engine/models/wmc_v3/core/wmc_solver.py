from subprocess import Popen, PIPE, check_output, call, run
import tempfile, os
import sys
import app.engine.models.wmc_v3.core.dimacs.dimacs_converter as dimacs_converter
import re
from app.engine.models.wmc_v3.db.session import Session
import time
import app.engine.models.wmc_v3.crud as crud
import time
from fastapi.logger import logger

#this function extracts the probability from the string which returns by cachet
def extract_probability_from_string(result_str):
    start_str = b"Satisfying probability\t\t\t"
    start = result_str.find(start_str) + len(start_str)
    end = result_str.find(b"\nNumber of solutions", start)
    str_prob = result_str[start:end]
    return float(str_prob)

#this function runs Cachet with given parameters
def run_solver(symptoms, parameter_t, disease=None):    
    cnfs = dimacs_converter.run(symptoms,parameter_t,disease) 
    results={'time':[],'probabilities':[]}
    for cnf in cnfs:
        tmp = tempfile.NamedTemporaryFile(delete=False)        
        try:
            tmp.write(bytes(cnf, "utf-8"))
            tmp.close()     
            start = time.time()
            proc = run(["app/engine/models/wmc_v3/cachet/cachet", tmp.name], capture_output=True)              
            end = time.time()
            results['time'].append(end-start)
            results['probabilities'].append(proc.stdout)
           # results.append(proc.stdout)

        finally:
            os.unlink(tmp.name)        
    return results


#this function inits run_solver and sums the probability results
def solve(symptoms,parameter_t, disease=None):
    result_strs = run_solver(symptoms, parameter_t,disease)  
    probabilities=[]
    for result_str in result_strs['probabilities']:
        prob = extract_probability_from_string(result_str)
        probabilities.append(prob)   
    res= {'runtime':sum(result_strs['time']),'probability':sum(probabilities)}

    return res