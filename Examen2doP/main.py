from fastapi import FastAPI, HTTPException
from typing  import Optional, List
from pydantic import BaseModel
from models import modelEnvios  


app = FastAPI(
    title='Mi primer API 196',
    description='Alejandro Chavez',
    version='1.0.1'
)



envios=[
   {"codigo_postal": "98756","destino":"rumania","peso": 22},
   {"codigo_postal": "54326","destino":"egipto","peso": 21},
   {"codigo_postal": "86479","destino":"españa","peso": 23},
   {"codigo_postal": "76751","destino":"brasil","peso": 20}
 

]

@app.get('/envios', response_model=List[modelEnvios], tags=["Operaciones CRUD"])
def CosultarTodos():
    return envios  

@app.delete('/envios/{codigo_postal}',tags=["Operaciones CRUD"])
def EliminarEnvio(codigo_postal:str):
    for i in range(len(envios)):
        if envios[i]["codigo_postal"]==codigo_postal:
            envios.pop(i)
            return {"mensaje":"envio eliminado"}
    raise HTTPException(status_code=404,detail="envio no encontrado")