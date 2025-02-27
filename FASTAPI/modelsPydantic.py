from pydantic import BaseModel, Field, EmailStr


#modelo de validacion de datos
class modelUsuario(BaseModel):
    id:int = Field(...,gt=0, description="id unico y solo numeros positivos")
    nombre:str = Field(...,min_length=3, max_length=15, description="nombre debe contener solo letras y espacios")
    edad:int = Field(...,gt=0,lt=130, description="edad debe ser un numero positivo y menor a 130")
    correo:EmailStr = Field(...,description="correo electronico valido", example=" example@.com")
    
