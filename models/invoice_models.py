from pydantic import BaseModel
from datetime import datetime

class InvoiceIn(BaseModel):
    nombre_cliente:str
    total:int

class InvoiceOut(BaseModel):
    id_factura:int
    nombre_cliente:str
    date:datetime
    total:int