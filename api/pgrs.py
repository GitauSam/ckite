from sqlalchemy import create_engine
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from typing import List, Optional
from pydantic import BaseModel
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder

app = FastAPI()

SQLALCHEMY_DATABASE_URL = "postgresql://phi:phi2021@127.0.0.1:5432/ckite"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

session  = SessionLocal()

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id=Column(Integer, primary_key=True)
    firstName=Column(String)
    lastName=Column(String)
    email=Column(String, unique=True)
    phoneNumber=Column(String)
    idNumber=Column(Integer)
    status=Column(Integer)

class UserModel(BaseModel):
    id: Optional[int]
    firstName: Optional[str]
    lastName: Optional[str]
    email: Optional[str]
    phoneNumber: Optional[str]
    idNumber: Optional[int]
    status: Optional[int] = 0

    class Config:
        orm_mode = True


@app.get("/user/{user_id}")
async def get_user(user_id):
    return session.query(User).filter(User.id == user_id).first()

# @app.post("/user/create")
# async def create_user(userModel: UserModel):
#     userModel.status = 1

#     conn.execute("INSERT INTO users (FIRSTNAME, LASTNAME, EMAIL, PHONENUMBER, IDNUMBER, STATUS) VALUES (?, ?, ?, ?, ?, ?)", (userModel.firstName, userModel.lastName, userModel.email, userModel.phoneNumber, userModel.idNumber, 1 ));

#     conn.commit()

#     print("user inserted successfully")

#     return "user inserted successfully"

# @app.get("/user/delete/{user_id}")
# async def deactivate_user(user_id: int):
#     cursor = conn.execute("UPDATE users SET status = ? WHERE ID = ?", (0, user_id))

#     return "user deleted successfully"

# @app.put("/user/edit/{user_id}")
# async def update_user(user_id: int, u: UserModel):

#     cursor = conn.execute("UPDATE users SET firstName = ?, lastName = ?, email = ?, phoneNumber = ?, idNumber = ?, status = ? WHERE ID = ?", (u.firstName, u.lastName, u.email, u.phoneNumber, u.idNumber, u.status, user_id))

#     return "user updated successfully"
