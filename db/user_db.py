from typing import  Dict
from pydantic import BaseModel

class usuario(BaseModel):
    username: str
    nombres: str
    password: str
    id_rol: int
    
database_users = Dict[str, usuario]

database_users = {
    "carlos123": usuario(**{"username":"carlos123",
                             "nombres": "Carlos Campo",
                             "password": "cc147",
                             "id_rol": 1 }),

    "victor181": usuario(**{"username":"victor181",
                             "nombres": "Víctor Anaya",
                             "password":"va789",
                             "id_rol": 2 }),
    
    "edilson753": usuario(**{"username":"edilson753",
                             "nombres": "Edilson Sarmiento",
                            "password":"es369",
                            "id_rol": 3}),
    
    "norma456": usuario(**{"username":"norma456",
                            "nombres": "Norma Velandia",
                            "password":"nm789",
                            "id_rol": 4})
}


def get_user(username: str):
    if username in database_users.keys():
        return database_users[username]
    else:
        return None

def update_user(user_in_db: usuario):
    database_users[user_in_db.username] = user_in_db
    return user_in_db
