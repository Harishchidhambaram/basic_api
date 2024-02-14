from typing import List
from fastapi import APIRouter,Depends,Response,status,HTTPException
from ..hashing import Hash
from .. import schema, database, models
from sqlalchemy.orm import Session
from  ..repository import user
router = APIRouter(
    prefix="/user",
    tags=['User']
)


@router.get('/',response_model=List[schema.Showblog])
def all(db:Session = Depends(database.get_db)):
    return user.get_all(db)

@router.post('/',status_code=200) 
def create(req_data: schema.User, db: Session = Depends(database.get_db)):
    return user.create(req_data,db)

@router.get('/{id}',status_code=200,response_model=schema.Showblog)
def show(id, response: Response, db: Session = Depends(database.get_db)):
    blog = db.query(models.User).filter(models.User.id == id).first()
    if not blog:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'detail': f"blog with the id {id} is not available"}
    return blog

@router.delete('/{id}',status_code=200)
def destroy(id, db: Session = Depends(database.get_db)):
    db.query(models.User).filter(models.User.id == id).delete(synchronize_session=False)
    db.commit()
    return 'done'

@router.put('/{id}',status_code=200)
def update(id, req_data: schema.User, db: Session = Depends(database.get_db)):
    blog = db.query(models.User).filter(models.User.id == id)
    if not blog.first():
        raise HTTPException(status_code=404,detail=f"User with id {id} not found")
    blog.update(req_data.dict())
    db.commit()
    return 'updated'