from fastapi import FastAPI, HTTPException, Depends
from middlewares import BearerJWT
from fastapi.responses import JSONResponse
from typing import Optional, List
from modelsPydantic import modelUsuario, modelAuth
from TokenGen import createtoken 

app = FastAPI(
    title='Mi primer API 196',
    description='Alejandro Chavez',
    version='1.0.1'
)


usuarios=[
   {"id": 1,"nombre": "Rayo","edad": 22, "correo":"rayo@example.com"},
   {"id": 2,"nombre": "issac","edad": 21, "correo":"issac@example.com"},
   {"id": 3,"nombre": "emi","edad": 23, "correo":"emi@example.com"},
   {"id": 4,"nombre": "joss","edad": 20, "correo":"joss@example.com"}


]
    
@app.get('/',tags=["Inicio"])

def main():
    return {'Hello World, ale chavez'}

@app.post('/auth/',tags=["Autenticacion"])
def login(autorizado: modelAuth):
    if autorizado.correo=="ale@example.com" and autorizado.passw=="ale12345":
        token:str=createtoken({"usuario":autorizado.model_dump()})
        print(token)
        return JSONResponse(content=token)
    else:
        return {"AVISO":"Usuario no autorizado"}

#endpoint consultar todos los usuarios
@app.get('/usuarios',dependencies=[Depends(BearerJWT())], response_model=List[modelUsuario], tags=["Operaciones CRUD"])
def CosultarTodos():
    return usuarios

#endpoint agreagar un usuario

@app.post('/usuarios/',response_model=modelUsuario, tags=["Operaciones CRUD"])
def AgregarUsuario(usuarionuevo: modelUsuario):
    for usr in usuarios:
        if usr["id"]==usuarionuevo.id:
            raise HTTPException(status_code=400, detail="el id ya existe")
    usuarios.append(usuarionuevo)
    return usuarionuevo

#endpoint actualizar usuario
@app.put('/usuarios/{id}',response_model=modelUsuario, tags=["Operaciones CRUD"])
def ActualizarUsuario (id:int,usuarioactualizado:modelUsuario):
    for index, usr in enumerate (usuarios):
        if usr["id"]==id:
            usuarios[index]= usuarioactualizado.model_dump()
            return {"usuario actualizado"}
    raise HTTPException(status_code=404,detail="usuario no encontrado")
    


#endpoint eliminar usuario
@app.delete('/usuarios/{id}',tags=["Operaciones CRUD"])
def EliminarUsuario(id:int):
    for i in range(len(usuarios)):
        if usuarios[i]["id"]==id:
            usuarios.pop(i)
            return {"mensaje":"usuario eliminado"}
    raise HTTPException(status_code=404,detail="usuario no encontrado")