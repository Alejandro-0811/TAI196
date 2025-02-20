from fastapi import FastAPI
from typing import Optional 
#declaramos un objeto 
app = FastAPI(
    title='Tareas', 
    description='Chávez Becerra Brayan Alejandro',
    version='1.0.1'
)

tareas=[
    {"id":1, "titulo":"Estudiar para el examen", "descripcion": "Reparar los apuntes de TAI", "vencimiento":"14-02-24", "Estado":"Completada"},
    {"id":2, "titulo":"Desayunar", "descripcion": "Desayunar para tener energias", "vencimiento":"15-02-24", "Estado":"Completada"},
    {"id":3, "titulo":"Ir al gimnasio", "descripcion": "Ir a reventar vena", "vencimiento":"16-02-24", "Estado":"No Completada"},
    {"id":4, "titulo":"Tarea", "descripcion": "Terminar la tarea", "vencimiento":"16-02-24", "Estado":"Completada"}
]

#Obtener todas las tareas.
@app.get('/tareas', tags=['Tareas'])
def ConsultarTodas():
    return {"Tareas":tareas}

#Obtener una tarea específica por su ID.
@app.get('/tareaid/{id}', tags=['Tareas'])
def ConsultarPorId(id:int):
    for tarea in tareas:
        if tarea["id"]==id:
            return tarea
    return {"mensaje":"Tarea no encontrada"}



