from db.user_db import usuario
from db.user_db import update_user, get_user, add_user

from db.client_db import cliente
from db.client_db import delete_cliente, update_client, get_client, add_client

from db.product_db import producto
from db.product_db import delete_product, update_product, get_product, add_product

from db.invoice_db import InvoiceInDb
from db.invoice_db import save_invoice

from models.user_models import UserIn, UserOut
from models.client_models import ClientIn, ClientOut
from models.product_models import ProductIn, ProductOut
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
    "https://myoptimalbusiness-app.herokuapp.com"
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


@api.get("/client/{client_id}/")
async def get_name(client_id:int):

    client_in_db=get_client(client_id)

    if client_in_db==None:
        raise HTTPException(status_code=404, 
                            detail="No se encontró cliente")
    client_out=ClientIn(**client_in_db.dict())
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

    return "Deleted client {client_id}"


# FUNCIONES DE LA CLASE PRODUCT

@api.post("/product/create/")
async def create_product(product_in: ProductIn):

    product_in_db = get_product(product_in.product_id)

    if product_in_db != None:
        raise HTTPException(status_code = 422, detail = "El producto ya existe")

    created_product = producto(**product_in.dict())
    add_product(created_product)
    return created_product


@api.get("/product/{product_id}/")
async def get_name(product_id: int):

    product_in_db = get_product(product_id)

    if product_in_db == None:
        raise HTTPException(status_code = 404, detail = "No se encontró producto")
    product_out = ProductOut(**product_in_db.dict())
    return product_out


@api.put("/product/EditData")
async def update_product_data(product_in: ProductIn):

    product_in_db = get_product(product_in.product_id)

    if(product_in_db == None):
        raise HTTPException(status_code = 404, detail = "No se encontró producto")

    update_product(product_in)

    product_out=ProductIn(**product_in.dict())

    return product_out


@api.delete("/product/del/{product_id}")
async def eliminate_product(product_id: int):

    deleted_product=get_product(product_id)

    if(deleted_product == None):
        raise HTTPException(status_code = 404, detail = "No sé encontró producto")
    
    delete_product(product_id)

    return "Eliminado producto con ID: {product_id}"

#TODO FUNCIONES DE LA CLASE INVOICE

