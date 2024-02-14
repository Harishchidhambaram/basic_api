from fastapi import FastAPI
from . import  models
from .database import engine
from  .routers import blog, user,authentication
app = FastAPI()

#we create the table in the database this line will create the table in database
models.Base.metadata.create_all(engine)


#Router
app.include_router(authentication.router)
app.include_router(blog.router)
app.include_router(user.router)

# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     except:
#         db.close()

# #insert
# @app.post('/blog',status_code=200) 
# def create(req_data: schema.Blog, db: Session = Depends(get_db)):
#     new_blog = models.Blog(title=req_data.title, body=req_data.body,user_id = req_data)
#     db.add(new_blog)
#     db.commit()
#     db.refresh(new_blog)
#     return new_blog

# delete
# @app.delete('/blog/{id}',status_code=200)
# def destroy(id, db: Session = Depends(get_db)):
#     db.query(models.Blog).filter(models.Blog.id == id).delete(synchronize_session=False)
#     db.commit()
#     return 'done'

#update(There are two method of writeing the query in this code i have put one method only)
# @app.put('/blog/{id}',status_code=200)
# def update(id, req_data: schema.Blog, db: Session = Depends(get_db)):
#     blog = db.query(models.Blog).filter(models.Blog.id == id)
#     if not blog.first():
#         raise HTTPException(status_code=404,detail=f"Blog with id {id} not found")
#     blog.update(req_data.dict())
#     db.commit()
#     return 'updated'
    
# get all
# @app.get('/blog',response_model=List[schema.Showblog])
# def all(db:Session = Depends(get_db)):
#     blogs = db.query(models.Blog).all()
#     return blogs

# get one
# @app.get('/blog/{id}',status_code=200,response_model=schema.Showblog)
# def show(id, response: Response, db: Session = Depends(get_db)):
#     blogs = db.query(models.Blog).filter(models.Blog.id == id).first()
#     if not blogs:
#         response.status_code = status.HTTP_404_NOT_FOUND
#         return {'detail': f"Blog with the id {id} is not available"}
#     return blogs

#create(user)
# @app.post('/user', status_code=200,response_model=schema.Showuser,tags=['user'])
# def create_user(req: schema.User,db:Session=Depends(get_db)): 
#     if create_user:
#         return HTTPException(404,"User already exist")
#     else:
#         new_user = models.User(name = req.name,email=req.email,password=Hash.bcrypt(req.password))
#         db.add(new_user)
#         db.commit()
#         db.refresh(new_user)
#         return new_user


#delete(user)
# @app.delete('/user/{id}',status_code=200)
# def destroy(id, db: Session = Depends(get_db)):
#     db.query(models.User).filter(models.User.id == id).delete(synchronize_session=False)
#     db.commit()
#     return 'done'


#update(user)
# @app.put('/user/{id}',status_code=200)
# def update(id, req_data: schema.User, db: Session = Depends(get_db)):
#     user = db.query(models.User).filter(models.User.id == id)
#     if not user.first():
#         raise HTTPException(status_code=404,detail=f"Blog with id {id} not found")
#     user.update(req_data.dict())
#     db.commit()
#     return 'updated'
    

#get one(user)
# @app.get('/user/{id}',status_code=200,response_model=schema.Showblog)
# def show(id, response: Response, db: Session = Depends(get_db)):
#     user = db.query(models.User).filter(models.User.id == id).first()
#     if not user:
#         response.status_code = status.HTTP_404_NOT_FOUND
#         return {'detail': f"User with the id {id} is not available"}
#     return user

#get all
# @app.get('/User',response_model=List[schema.Showblog])
# def all(db:Session = Depends(get_db)):
#     blogs = db.query(models.User).all()
#     return blogs