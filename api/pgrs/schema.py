from typing import List, Optional

from pydantic import BaseModel

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