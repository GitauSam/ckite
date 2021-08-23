from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

userStore = {}

class UserModel(BaseModel):
    id: Optional[int]
    firstName: str
    lastName: str
    email: str
    phoneNumber: str
    idNumber: int
    status: Optional[int] = 0

@app.get("/")
async def get_users():
    result = {}
    for key, value in userStore.items():
        if value.status == 1:
            result[key] = value
    return result

@app.post("/user/create")
async def get_users(userModel: UserModel):
    userId = len(userStore) + 1
    userModel.id = userId
    userModel.status = 1
    userStore[userId] = userModel
    return userStore

@app.get("/user/delete/{user_id}")
async def deactivate_user(user_id: int):
    u = userStore[user_id]
    u.status = 0
    return u

@app.put("/user/edit/{user_id}")
async def update_user(user_id: int, u: UserModel):
    u.status = 1
    userStore[user_id] = u
    return userStore[user_id]
