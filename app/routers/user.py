from fastapi import FastAPI, HTTPException, Response, status, APIRouter, Depends

from sqlalchemy.orm import Session
import models, schemas
from database import get_db
import oauth2

router = APIRouter(prefix="/users")


@router.post("/", response_model=schemas.Token)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    new_user = models.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    access_token = oauth2.create_access_token(data={"user_id": new_user.id})
    return {"access_token": access_token, "token_type": "Bearer"}

    # return new_user

@router.get("/{id}", response_model=schemas.UserResponse)
def get_user(id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.delete("/{id}")
def delete_user(id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id ==id)
    if user.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="user not found")
    user.delete(synchronize_session=False)
    db.commit() 
    return f"user {id} deleted successfull"

@router.put("/{id}", response_model=schemas.UserResponse)
def update_user(id:int, updated_user: schemas.UserCreate,db:Session = Depends(get_db)):
    user_query = db.query(models.User).filter(models.User.id == id)
    user = user_query.first()
    if user ==  None:
       raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                detail= f"post with id: {id} was not found")
    user_query.update(updated_user.dict(),synchronize_session=False)
    db.commit()   
    return user_query.first()