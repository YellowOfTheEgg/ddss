import app.engine.models.wmc_v3.crud as crud
from app.engine.models.wmc_v3.models.wmc_variable import WmcVariable


def create_clause(wmc_var):
    indicator_var = WmcVariable(
            id=wmc_var.indicator_id, negation=True, weight=1, type="indicator", indicator_name=wmc_var.indicator_name
        )
    parameter_var = WmcVariable(
        id=wmc_var.parameter_id,
        negation=True,
        weight=wmc_var.parameter_weight,
        type="parameter",
        symptom_name=wmc_var.symptom_name,
        disease_name=wmc_var.disease_name
    )
    return [indicator_var, parameter_var]

#creates the part of the WMC1-Encoding for absent symptoms
def create_body_for_absent_symptoms(wmc_vars) -> [[WmcVariable]]:    
    expression = []
    for wmc_var in wmc_vars:
        dnf_clause=create_clause(wmc_var)
        expression.append(dnf_clause)
    return expression