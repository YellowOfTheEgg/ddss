import requests
from starlette.datastructures import QueryParams
from starlette.responses import Response
from concurrent.futures import ThreadPoolExecutor
from fastapi.logger import logger as fastapi_logger
import json

def query_params_to_dict(query_params):
    tpls=query_params.multi_items()
    res={}
    for tpl in tpls:
        k=tpl[0]
        v=tpl[1]
        if res.get(k) is not None:
            tmp=res.get(k)
            if not isinstance(tmp,list):                
                tmp=[tmp]
            tmp.append(v)
            res[k]=tmp
        else:
            res[k]=v        
    return res

# this function forwards requests to other backend-services and returns the response from them
async def _proxy(request, endpoint):
    headers={key: value for key, value in request.headers.items() if key != "Host"}    
    headers['Authorization']=f"Bearer {request.cookies.get('Authorization','')}"    
    resp = requests.request(
        method=request.method,
        url=endpoint,
        headers=headers,
        params=query_params_to_dict(request.query_params),
        data=await request.body(),
        cookies=request.cookies,
        allow_redirects=False,
    )    
    return {'status_code': resp.status_code,'body':resp.json()}
