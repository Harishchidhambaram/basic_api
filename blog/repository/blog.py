from sqlalchemy.orm import Session
from  .. import models,database,schema
from fastapi import Depends

def get_all(db:Session):
    blogs = db.query(models.Blog).all()
    return blogs

def create(req_data:schema,Blog,db: Session):
    new_blog = models.Blog(title=req_data.title, body=req_data.body,user_id = req_data)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def destroy (id, db: Session = Depends(database.get_db)):
    db.query(models.Blog).filter(models.Blog.id == id).delete(synchronize_session=False)
    db.commit()
    return 'done'