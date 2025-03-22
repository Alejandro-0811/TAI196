from pydantic import BaseModel, Field, EmailStr


#modelo de validacion de datos
class modelUsuario(BaseModel):
    name:str = Field(...,min_length=3, max_length=15, description="nombre debe contener solo letras y espacios")
    age:int
    email: str
    
class modelAuth(BaseModel):
    correo: EmailStr
    passw:str = Field(...,min_length=8, strip_whitespace=True, description="contraseña debe contener al menos 8 caracteres")