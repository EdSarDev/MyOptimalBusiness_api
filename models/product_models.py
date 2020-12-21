from pydantic import BaseModel
from datetime import datetime

class ProductIn(BaseModel):
    product_id:int
    nombre_producto:str
    tipo_producto:str
    valor_compra:int
    valor_venta:int

class ProductOut(BaseModel):
    product_id:int
    nombre_producto:str
    tipo_producto:str
    valor_venta:int