from fastapi import FastAPI ,HTTPException,Response, status,APIRouter,Depends

from sqlalchemy.orm import Session
import models,schemas
from database import get_db
import oauth2

router = APIRouter(
    prefix= "/users"
)

@router.post("/",response_model= schemas.UserResponse)
def create_user(user:schemas.UserCreate,db:Session=Depends(get_db)):
    new_user = models.User(**user.dict())

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user