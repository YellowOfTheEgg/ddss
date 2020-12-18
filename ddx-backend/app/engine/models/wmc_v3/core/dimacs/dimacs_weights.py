from app.engine.models.wmc_v3.models.wmc_variable import WmcVariable


def create_weights(dimacs_body: [[WmcVariable]])->[int]:
    #print('create weights')
    
    wmc_vars = [item for sublist in dimacs_body for item in sublist]
  
    unique = set(wmc_vars)
  
    sorted_vars = sorted(unique)
    weights = []
    for wmc_var in sorted_vars:
        if wmc_var.type == "parameter":
            weights.append(wmc_var.weight)
            weights.append(1 - wmc_var.weight)
        else:
            weights.extend([1, 1])

    return weights