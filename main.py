from db.user_db import usuario
from db.user_db import update_user, get_user
from models.user_models import UserIn, UserOut

import datetime
from fastapi import FastAPI, HTTPException

api = FastAPI()

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
