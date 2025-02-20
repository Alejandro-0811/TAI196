from fastapi import FastAPI, HTTPException
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

#Crear una nueva tarea.
@app.post('/tareas/', tags=['Tareas'])
def AgregarTarea(tareaNueva: dict):
    for tarea in tareas:
        if tarea["id"]==tareaNueva.get("id"):
            raise HTTPException(status_code=400, detail="El id ya existe")
    tareas.append(tareaNueva)
    return tareaNueva

#Actualizar una tarea existente.
@app.put('/tareas/{id}', tags=['Tareas'])
def ActualizarTarea(id:int, tareaActualizada: dict):
    for tarea in tareas:
        if tarea["id"]==id:
            tarea.update(tareaActualizada)
            return {"mensaje":"Tarea actualizada"}
    raise HTTPException(status_code=404, detail="Tarea no encontrada")


