from typing import List
from fastapi import APIRouter,Depends,Response,status,HTTPException
from .. import schema, database, models
from sqlalchemy.orm import Session
from  ..repository import blog
router = APIRouter(
    prefix="/blog",
    tags=['Blog']
)


@router.get('/',response_model=List[schema.Showblog])
def all(db:Session = Depends(database.get_db)):
    return blog.get_all(db)

@router.post('/',status_code=200) 
def create(req_data: schema.Blog, db: Session = Depends(database.get_db)):
    return blog.create(db)

@router.get('/{id}',status_code=200,response_model=schema.Showblog)
def show(id, response: Response, db: Session = Depends(database.get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'detail': f"blog with the id {id} is not available"}
    return blog

@router.delete('/{id}',status_code=200)
def destroy(id:int, db: Session = Depends(database.get_db)):
    return blog.destory(id,db)

@router.put('/{id}',status_code=200)
def update(id, req_data: schema.Blog, db: Session = Depends(database.get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=404,detail=f"Blog with id {id} not found")
    blog.update(req_data.dict())
    db.commit()
    return 'updated'