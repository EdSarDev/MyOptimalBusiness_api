from pydantic import BaseModel
from datetime import datetime

class ClientIn(BaseModel):
    client_id:int
    nombre:str
    apellido:str
    email:str
    celular:int

class ClientOut(BaseModel):
    client_id:int
    nombre:str
    apellido:str
    fecha_registro:datetime