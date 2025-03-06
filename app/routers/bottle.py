from fastapi import FastAPI ,HTTPException,Response, status,APIRouter,Depends

from sqlalchemy.orm import Session
import models,schemas
from database import get_db
import oauth2


router =APIRouter(
    prefix="/bottles"
)

@router.post("/",response_model=schemas.BottleResponse)
def create_bottle(bottle:schemas.BottleCreate,db:Session=Depends(get_db)):
    new_bottle = models.Bottle(**bottle.dict())
    db.add(new_bottle)
    db.commit()
    db.refresh(new_bottle)
    return new_bottle