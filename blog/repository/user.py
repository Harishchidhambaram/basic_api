from sqlalchemy.orm import Session
from  .. import models,database,schema
from fastapi import Depends,HTTPException,status
from .. import hashing
    
def get_all(db:Session):
    user = db.query(models.User).all()
    return user

def create(req_data:schema.User,db: Session):
    user = db.query(models.User).filter(models.User.email == req_data.email).first()
    if user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail={"message":"user already exist"})
    else:
        new_user = models.User(
            name=req_data.name,
            email=req_data.email,
            password=hashing.Hash.bcrypt(password=req_data.password)
            )
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user


