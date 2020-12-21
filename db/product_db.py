from typing import Dict
from pydantic import BaseModel
from datetime import datetime

class producto(BaseModel):
    product_id:int
    nombre_producto:str
    tipo_producto:str
    valor_compra:int
    valor_venta:int

database_products = Dict[int,producto]

database_products = {
        100001 : producto(**{"product_id":100001,
                            "nombre_producto":"Llave hexagonal",
                            "tipo_producto":"Herramienta manual",
                            "valor_compra":15000,
                            "valor_venta":17000}),
        100002 : producto(**{"product_id":100002,
                            "nombre_producto":"Martillo de bola",
                            "tipo_producto":"Herramienta manual",
                            "valor_compra":19000,
                            "valor_venta":23000})
}

def add_product(product_in_db:producto):
    if not product_in_db.product_id in database_products.keys():
        database_products[product_in_db.product_id]=product_in_db
        return product_in_db

def get_product(product_id: int):
    if product_id in database_products.keys():
        return database_products[product_id]
    else:
        return None

def update_product(product_in_db: producto):
    database_products[product_in_db.product_id]=product_in_db
    return product_in_db

def delete_product(product_id:int):
    if product_id in database_products.keys():
        del database_products[product_id]
