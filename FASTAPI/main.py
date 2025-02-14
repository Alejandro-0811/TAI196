from fastapi import FastAPI, HTTPException
from typing import Optional

app = FastAPI(
    title='Mi primer API 196',
    description='Alejandro Chavez',
    version='1.0.1'
)

usuarios=[
   {"id": 1,"nombre": "Rayo","edad": 22},
   {"id": 2,"nombre": "issac","edad": 21},
   {"id": 3,"nombre": "emi","edad": 23},
   {"id": 4,"nombre": "joss","edad": 20}


]
    
@app.get('/',tags=["Inicio"])

def main():
    return {'Hello World, ale chavez'}

#endpoint consultar todos los usuarios
@app.get('/usuarios',tags=["Operaciones CRUD"])
def CosultarTodos():
    return {"usuarios registrados":usuarios}

#endpoint agreagar un usuario

@app.post('/usuarios/',tags=["Operaciones CRUD"])
def AgregarUsuario(usuarionuevo: dict):
    for usr in usuarios:
        if usr["id"]==usuarionuevo.get("id"):
            raise HTTPException(status_code=400, detail="el id ya existe")
    usuarios.append(usuarionuevo)
    return usuarionuevo

#endpoint actualizar usuario
@app.put('/usuarios/{id}',tags=["Operaciones CRUD"])
def ActualizarUsuario (id:int,usuarioactualizado:dict):
    for usr in usuarios:
        if usr["id"]==id:
            usr.update(usuarioactualizado)
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