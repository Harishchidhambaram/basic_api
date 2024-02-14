from pydantic import BaseModel

class Blog(BaseModel):
    title: str
    body: str 


class User(BaseModel):
    name: str
    email: str
    password: str


class Showuser(BaseModel):
    name: str
    email: str
    class Config():
        orm_mode = True


class Showblog(BaseModel):
    title: str
    body: str
    creator : Showuser

    class Config():
        orm_mode = True


class Login(BaseModel):
    email:str
    password:str
    
    