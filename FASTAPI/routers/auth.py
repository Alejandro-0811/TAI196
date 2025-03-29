from fastapi.responses import JSONResponse
from modelsPydantic import  modelAuth
from TokenGen import createtoken 
from fastapi import APIRouter


routerAuth = APIRouter()



@routerAuth.post('/auth/',tags=["Autenticacion"])
def login(autorizado: modelAuth):
    if autorizado.correo=="ale@example.com" and autorizado.passw=="ale12345":
        token:str=createtoken({"usuario":autorizado.model_dump()})
        print(token)
        return JSONResponse(content=token)
    else:
        return {"AVISO":"Usuario no autorizado"}