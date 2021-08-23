from sqlalchemy.orm import Session
from . import models, schema

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_users(db: Session):
    return db.query(models.User).filter(models.User.status == 1).all()

def create_user(db: Session, u: schema.UserModel):
    nu = models.User(
            firstName = u.firstName,
            lastName = u.lastName,
            email = u.email,
            phoneNumber = u.phoneNumber,
            idNumber = u.idNumber,
            status = 1
        )

    db.add(nu)
    db.commit()
    db.refresh(nu)
    return nu

def edit_user(db: Session, user: schema.UserModel, user_id: int):

    db.query(models.User).filter(models.User.id == user_id).update({models.User.firstName:user.firstName,models.User.lastName:user.lastName,models.User.email:user.email,models.User.phoneNumber:user.phoneNumber,models.User.idNumber:user.idNumber}, synchronize_session=False)
    db.commit()
    
    return db.query(models.User).filter(models.User.id == user_id).first()

def deactivate_user(db: Session, user_id: int):

    db.query(models.User).filter(models.User.id == user_id).update({models.User.status:0}, synchronize_session=False)
    db.commit()
    
    return db.query(models.User).filter(models.User.id == user_id).first()