from fastapi import APIRouter,Depends,status,HTTPException
from ..import schema,database,models
from sqlalchemy.orm import Session
from ..hashing import Hash

router = APIRouter(
    tags=['Authentication']
)

@router.post('/login')
def login(req_data:schema.Login,db:Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.email == req_data.email).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="User not found")
    if not Hash.verfiy(req_data.password,user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="password wrong")
    return user

