from fastapi import  HTTPException, Depends
from middlewares import BearerJWT
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from modelsPydantic import modelUsuario, modelAuth
from DB.conexion import Session
from models.modelsDB import User
from fastapi import APIRouter

routerUsuario = APIRouter()

#dependencies=[Depends(BearerJWT())]        

#endpoint consultar todos los usuarios
@routerUsuario.get('/usuarios', tags=["Operaciones CRUD"])
def CosultarTodos():
    db = Session()
    try:
        consulta=db.query(User).all()
        return JSONResponse(content=jsonable_encoder(consulta))
    
    except Exception as x:
        return JSONResponse(status_code=500,content={"mensaje":"Error al consultar los usuarios", "Excepcion":str(x)})
    
    finally:
        db.close()

#endpoint consultar un usuario por id
@routerUsuario.get('/usuarios/{id}', tags=["Operaciones CRUD"])
def CosultarUno(id:int):
    db = Session()
    try:
        consulta=db.query(User).filter(User.id==id).first()
        if not consulta:
            return JSONResponse(content={"mensaje":"Usuario no encontrado"})
        
        return JSONResponse(content=jsonable_encoder(consulta))
    
    except Exception as x:
        return JSONResponse(status_code=404,content={"mensaje":"Error al consultar los usuarios", "Excepcion":str(x)})
    
    finally:
        db.close()
    

#endpoint agregar un usuario
@routerUsuario.post('/usuarios/',response_model=modelUsuario, tags=["Operaciones CRUD"])
def AgregarUsuario(usuarionuevo: modelUsuario):
    db = Session()
    try: 
        db.add(User(**usuarionuevo.model_dump()))
        db.commit()
        return JSONResponse(status_code=201,content={"mensaje":"usuario agregado", "usuario":usuarionuevo.model_dump()})
    except Exception as e:
        db.rollback()
        return JSONResponse(status_code=500,content={"mensaje":"usuario no agregado", "Excepcion":str(e)})
    finally:
        db.close()

#endpoint actualizar usuario
@routerUsuario.put('/usuarios/{id}',tags=["Operaciones CRUD"])
def ActualizarUsuario(id:int, usuarioactualizado: modelUsuario):
    db = Session()
    try:
        consulta=db.query(User).filter(User.id==id).first()
        if not consulta:
            return JSONResponse(content={"mensaje":"Usuario no encontrado"})
        
        db.query(User).filter(User.id==id).update(usuarioactualizado.model_dump())
        db.commit()
        return JSONResponse(content={"mensaje":"usuario actualizado"})
    
    except Exception as x:
        return JSONResponse(status_code=404,content={"mensaje":"Error al consultar los usuarios", "Excepcion":str(x)})
    
    finally:
        db.close()
    


#endpoint eliminar usuario
@routerUsuario.delete('/usuarios/{id}',tags=["Operaciones CRUD"])
def EliminarUsuario(id:int):
    db = Session()
    try:
        consulta=db.query(User).filter(User.id==id).first()
        if not consulta:
            return JSONResponse(content={"mensaje":"Usuario no encontrado"})
        
        db.query(User).filter(User.id==id).delete()
        db.commit()
        return JSONResponse(content={"mensaje":"usuario eliminado"})
    
    except Exception as x:
        return JSONResponse(status_code=404,content={"mensaje":"Error al consultar los usuarios", "Excepcion":str(x)})
    
    finally:
        db.close()
