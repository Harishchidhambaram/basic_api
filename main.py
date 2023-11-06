from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    return "hey"

@app.get('/about')
def about():
    return {'data':{'about page'}}

@app.get('/blog/unpublished')
def unpublished():
    return {'data' : 'oll unpublished blogs'}

@app.get('/blog/{id}')
def show(id: int):
    return {'data':{'id':id}}


#@app.get('/blog/{id}/comments')
#def comments(id): 
    #return  {'data': {'1','2'}} 

#@app.get('/blog')
 #def index(limit=10, published: bool = True, sort: Optional[str] = None):
     #if published:
         #return {'data': f'{limit} published blogs from the db'}
     #else :
         #return {'data': f'{limit} blogs from the db'} 