#for create the database we have to import these three things and these 10 lines are the setup for database
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHAMY_DATABASE_URL = 'sqlite:///./blog.db'

#we have creating the database engine
engine = create_engine(SQLALCHAMY_DATABASE_URL,connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(bind=engine,autocommit=False,autoflush=False)

Base = declarative_base()



def get_db():
    db = SessionLocal()
    try:
        yield db
    except:
        db.close()