from typing import Dict
from pydantic import BaseModel
from datetime import datetime

class cliente(BaseModel):
    client_id:int
    nombre:str
    apellido:str
    fecha_registro:datetime=datetime.now()
    email:str
    celular:int

database_clients = Dict[int,cliente]

database_clients = {
        100001 : cliente(**{"client_id":100001,
                            "nombre":"Hugo",
                            "apellido":"Boss",
                            "email":"hugoboss@gmail.com",
                            "celular":1111111111}),
        100002 : cliente(**{"client_id":100002,
                            "nombre":"Christian",
                            "apellido":"Dior",
                            "email":"christiandior@gmail.com",
                            "celular":2222222222}),
        100003 : cliente(**{"client_id":100003,
                            "nombre":"Coco",
                            "apellido":"Channel",
                            "email":"cocochannel@gmail.com",
                            "celular":3333333333}),
        100004 : cliente(**{"client_id":100004,
                            "nombre":"Stefano",
                            "apellido":"Gabbana",
                            "email":"stefanogabbana@gmail.com",
                            "celular":4444444444}),
}

def add_client(client_in_db:cliente):
    if not client_in_db.client_id in database_clients.keys():
        database_clients[client_in_db.client_id]=client_in_db
        return client_in_db

def get_client(client_id: int):
    if client_id in database_clients.keys():
        return database_clients[client_id]
    else:
        return None

def update_client(client_in_db: cliente):
    database_clients[client_in_db.client_id]=client_in_db
    return client_in_db

def delete_cliente(client_id:int):
    if client_id in database_clients.keys():
        del database_clients[client_id]
