from fastapi import FastAPI
from typing  import Optional
#To declare the request body we importing the pydantic
from pydantic import BaseModel
app = FastAPI()

@app.get('/')
def index():
    return "hey"

@app.get ('/about')  
def about():
    return {'data':{'about page'}}

@app.get('/blog/unpublished')
def unpublished():
    return {'data' : 'all unpublished blogs'}

@app.get('/blog/{id}')
def show(id: int):
    return {'data':{'id':id}}
    
 

@app.get('/blog/{id}/comments')
def comments(id): 
    return  {'data': {'1','2'}} 

#Query Parameter
@app.get('/blog')
def index(limit=10, published: bool = True, sort: Optional[str] = None):
    if published:
        return {'data': f'{limit} published blogs from the db'}
    else:
        return {'data': f'{limit} blogs from the db'} 

#Post
class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]
@app.post('/blog')
def create_blog(request: Blog):
    return request
    return {'data' : "Blog is created"}

#Debug fastapi application
#@app.post('/blog')
#def create_blog(blog: Blog):
    #return {'data': f"Blog is created with title as {blog.title}"}