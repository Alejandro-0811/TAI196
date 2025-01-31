from fastapi import FastAPI
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

@app.get('/promedio',tags=["Calificación"])

def promedio():
    return {'12'}

@app.get('/usuario/{id}',tags=['Parametro obligatorio'])
def consultaUsuario(id:int):
    #conectamosBD
    #hacemos consulta retornamos resultset
    return{"Se encontro usuario": id}

@app.get('/usuariox/',tags=['Parametro opcional'])
def consultaUsuario2(id:Optional[int]=None):
    if id is not None: 
        for usuario in usuarios:
            if usuario ["id"] == id:
                return {"mensaje":"Usuario encontrado", "usuario":usuario}
        return{"mensaje":f"No se encontro el id:{id}"}
    else:
        return{"mensaje":"No se proporciono"}

#endpoint con varios parametro opcionales
@app.get("/usuarios/", tags=["3 parámetros opcionales"])
async def consulta_usuarios(
    usuario_id: Optional[int] = None,
    nombre: Optional[str] = None,
    edad: Optional[int] = None
):
    resultados = []

    for usuario in usuarios:
        if (
            (usuario_id is None or usuario["id"] == usuario_id) and
            (nombre is None or usuario["nombre"].lower() == nombre.lower()) and
            (edad is None or usuario["edad"] == edad)
        ):
            resultados.append(usuario)

    if resultados:
        return {"usuarios_encontrados": resultados}
    else:
        return {"mensaje": "No se encontraron usuarios que coincidan con los parámetros proporcionados."}