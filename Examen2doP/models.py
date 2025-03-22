from pydantic import BaseModel, Field


#modelo de validacion de datos
class modelEnvios(BaseModel):
    codigo_postal:str = Field(min_length=5, description="minimo 5")
    destino:str = Field(min_length=6, description="minimo 6")
    peso:int = Field(gt=1,lt=499, description="solo numeros mayores a 0 y menores a 500")

