from db.user_db import usuario
from db.user_db import update_user, get_user, add_user

from db.client_db import cliente
from db.client_db import delete_cliente, update_client,get_client, add_client

from db.invoice_db import InvoiceInDb
from db.invoice_db import save_invoice

from models.user_models import UserIn, UserOut
from models.client_models import ClientIn, ClientOut
from models.invoice_models import InvoiceIn,InvoiceOut

import datetime
from fastapi import FastAPI,HTTPException

from fastapi.middleware.cors import CORSMiddleware

api=FastAPI()

# Políticas CORS

origins = [
    "http://localhost.tiangolo.com", 
    "https://localhost.tiangolo.com",
    "http://localhost", 
    "http://localhost:8080", 
    "https://myoptimalbusiness-api.herokuapp.com"
]

api.add_middleware(
    CORSMiddleware, allow_origins=origins,
    allow_credentials=True, allow_methods=["*"], allow_headers=["*"],
)

#FUNCIONES DE LA CLASE USER

@api.post("/user/auth/")
async def auth_user(user_in: UserIn):

    user_in_db = get_user(user_in.username)

    if user_in_db == None:
        raise HTTPException(status_code=404, detail="El usuario no existe")

    if user_in_db.password != user_in.password:
        return  {"Autenticado": False}

    return  {"Autenticado": True}


@api.get("/user/rol/{username}")
async def get_rol(username: str):

    user_in_db = get_user(username)
    

    if user_in_db == None:
        raise HTTPException(status_code=404, detail="El usuario no existe")

    user_out = UserOut(**user_in_db.dict())

    return  user_out


@api.put("/user/ChangeRole/")
async def change_Rol(user_in: UserOut):

    user_in_db = get_user(user_in.username)

    if user_in_db == None:
        raise HTTPException(status_code=404, detail="El usuario no existe")

    user_in_db.id_rol = user_in.id_rol
    update_user(user_in_db)

    return  user_in_db

@api.post("/user/create")
async def create_user(user_in:usuario):

    user_in_db=get_user(user_in.username)

    if user_in_db!=None:
        raise HTTPException(status_code=422,
                            detail="El usuario ya existe")
    
    created_user=usuario(**user_in.dict())
    add_user(created_user)
    return create_user



#FUNCIONES DE LA CLASE CLIENT

@api.post("/client/create/")
async def create_client(client_in:ClientIn):

    client_in_db=get_client(client_in.client_id)

    if client_in_db!=None:
        raise HTTPException(status_code=422,
                            detail="El cliente ya existe")

    created_client=cliente(**client_in.dict())
    add_client(created_client)
    return created_client


@api.get("/client/{client_id}}/")
async def get_name(client_id:int):

    client_in_db=get_client(client_id)

    if client_in_db==None:
        raise HTTPException(status_code=404, 
                            detail="No se encontró cliente")
    client_out=ClientOut(**client_in_db.dict())
    return client_out


@api.put("/client/EditData")
async def update_client_data(client_in:ClientIn):

    client_in_db= get_client(client_in.client_id)

    if(client_in_db==None):
        raise HTTPException(status_code=404, 
                            detail="No se encontró cliente")

    update_client(client_in)

    client_out=ClientIn(**client_in.dict())

    return client_out


@api.delete("/client/del/{client_id}")
async def eliminate_client(client_id:int):

    deleted_client=get_client(client_id)

    if(deleted_client==None):
        raise HTTPException(status_code=404, detail="No sé encontró cliente")
    
    delete_cliente(client_id)

    return f"Deleted client {client_id}"

#TODO FUNCIONES DE LA CLASE INVOICE

