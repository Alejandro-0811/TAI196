from fastapi import FastAPI
from DB.conexion import  engine, Base
from routers.usuarios import routerUsuario
from routers.auth import routerAuth

app = FastAPI(
    title='Mi primer API 196',
    description='Alejandro Chavez',
    version='1.0.1'
)

#levanta las tablas definidas en los modelos
Base.metadata.create_all(bind=engine)


@app.get('/',tags=["Inicio"])

def main():
    return {'Hello World, ale chavez'}

app.include_router(routerUsuario)
app.include_router(routerAuth)
    



