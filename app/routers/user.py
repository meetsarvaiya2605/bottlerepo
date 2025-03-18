from fastapi import FastAPI, HTTPException, Response, status, APIRouter, Depends,Request

from sqlalchemy.orm import Session
import models, schemas,utils
from database import get_db
import oauth2
from datetime import datetime
from fastapi.responses import JSONResponse

router = APIRouter(prefix="/users")


@router.post("/")
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    hashed_password = utils.hash_password(user.password)
    user.password = hashed_password
    new_user = models.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    bottle = models.Bottle(user_id=new_user.id)
    db.add(bottle)
    db.commit()
    db.refresh(bottle)
    access_token = oauth2.create_access_token(data={"user_id": new_user.id})
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={"message": "user created successfully",
        "access_token": access_token,
         "token_type": "Bearer",
        }
    )



@router.get("/all")
def get_users(db: Session = Depends(get_db)):
    return db.query(models.User).all()


@router.get("/{id}", response_model=schemas.UserResponse)
def get_user(db: Session = Depends(get_db),current_user: models.User = Depends(oauth2.get_current_user),):
    user = db.query(models.User).filter(models.User.id == current_user.id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.delete("/{id}")
def delete_user(id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id)
    if user.first() == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="user not found"
        )
    user.delete(synchronize_session=False)
    db.commit()
    return f"user {id} deleted successfull"


@router.put("/{id}", response_model=schemas.UserResponse)
def update_user( id: int,updated_user: schemas.UserCreate, db: Session = Depends(get_db)):
    user_query = db.query(models.User).filter(models.User.id ==id)
    user = user_query.first()
    if user == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"post with id: {id} was not found",
        )
    user_query.update(updated_user.dict(exclude_unset=True))
    db.commit()
    return user_query.first()


@router.post("/drink_time", response_model=schemas.UserResponse)
def update_last_drink_time(
    user_id: int,
    db: Session = Depends(get_db),
):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if user:
        user.last_drink_time = datetime.utcnow()
        db.commit()
        db.refresh(user)
    return user
