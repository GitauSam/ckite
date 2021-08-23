from typing import List
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schema
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/users")
async def get_user(db: Session = Depends(get_db)):
    u = crud.get_users(db)

    if u is None:
        raise HTTPException(status_code=404, detail="Users not found")
    return u

@app.get("/user/{user_id}")
async def get_user(user_id: int, db: Session = Depends(get_db)):
    u = crud.get_user(db, user_id=user_id)

    if u is None:
        raise HTTPException(status_code=404, detail="User not found")
    return u

@app.post("/user/create", response_model=schema.UserModel)
async def create_user(user: schema.UserModel, db: Session = Depends(get_db)):
    return crud.create_user(db=db, u=user)

@app.post("/user/edit/{user_id}")
async def update_user(user_id: int, user: schema.UserModel, db: Session = Depends(get_db)):
    return crud.edit_user(db=db,user=user,user_id=user_id)

@app.get("/user/delete/{user_id}")
async def deactivate_user(user_id: int, db: Session = Depends(get_db)):
    return crud.deactivate_user(db=db,user_id=user_id)
