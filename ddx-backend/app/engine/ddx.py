import app.engine.models.wmc_v3.ddx as wmc_v3_ddx


def ddx_wmc_v3(symptoms, parameter_t):
    return wmc_v3_ddx.ddx(symptoms,parameter_t)

def wmc_v3(symptoms,parameter_t):
    return wmc_v3_ddx.wmc(symptoms,parameter_t)

