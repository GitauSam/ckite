from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel
import sqlite3
from fastapi.encoders import jsonable_encoder

app = FastAPI()

conn = sqlite3.connect(':memory:')

print("Opened database successfully");\

conn.execute('''CREATE TABLE users
         (ID INTEGER PRIMARY KEY    AUTOINCREMENT     NOT NULL,
         FIRSTNAME           TEXT    NOT NULL,
         LASTNAME           TEXT    NOT NULL,
         EMAIL           CHAR(180)    NOT NULL,
         PHONENUMBER           CHAR(15)    NOT NULL,
         IDNUMBER            INT     NOT NULL,
         STATUS       INT   NOT NULL);''')

print("Table created successfully")

# conn.close()

class UserModel(BaseModel):
    id: Optional[int]
    firstName: Optional[str]
    lastName: Optional[str]
    email: Optional[str]
    phoneNumber: Optional[str]
    idNumber: Optional[int]
    status: Optional[int] = 0

@app.get("/user/{user_id}")
async def get_user(user_id):

    cursor = conn.execute("SELECT id, firstName, lastName, email, phoneNumber, idNumber, status FROM users WHERE ID = ?", (user_id))

    userModel: UserModel = UserModel()

    for row in cursor:
        userModel.id = row[0]
        userModel.firstName = row[1]
        userModel.lastName = row[2]
        userModel.email = row[3]
        userModel.phoneNumber = row[4]
        userModel.idNumber = row[5]
        userModel.status = row[6]

    return jsonable_encoder(userModel)

@app.post("/user/create")
async def create_user(userModel: UserModel):
    userModel.status = 1

    conn.execute("INSERT INTO users (FIRSTNAME, LASTNAME, EMAIL, PHONENUMBER, IDNUMBER, STATUS) VALUES (?, ?, ?, ?, ?, ?)", (userModel.firstName, userModel.lastName, userModel.email, userModel.phoneNumber, userModel.idNumber, 1 ));

    conn.commit()

    print("user inserted successfully")

    return "user inserted successfully"

@app.get("/user/delete/{user_id}")
async def deactivate_user(user_id: int):
    cursor = conn.execute("UPDATE users SET status = ? WHERE ID = ?", (0, user_id))

    return "user deleted successfully"

@app.put("/user/edit/{user_id}")
async def update_user(user_id: int, u: UserModel):

    cursor = conn.execute("UPDATE users SET firstName = ?, lastName = ?, email = ?, phoneNumber = ?, idNumber = ?, status = ? WHERE ID = ?", (u.firstName, u.lastName, u.email, u.phoneNumber, u.idNumber, u.status, user_id))

    return "user updated successfully"