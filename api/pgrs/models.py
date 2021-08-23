from sqlalchemy import Column, Integer, String

from .database import Base

class User(Base):
    __tablename__ = "users"
    id=Column(Integer, primary_key=True)
    firstName=Column(String)
    lastName=Column(String)
    email=Column(String, unique=True)
    phoneNumber=Column(String)
    idNumber=Column(Integer)
    status=Column(Integer)