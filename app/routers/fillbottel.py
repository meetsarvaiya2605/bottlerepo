from fastapi import FastAPI ,HTTPException,Response, status,APIRouter,Depends

from sqlalchemy.orm import Session
import models,schemas
from database import get_db
import oauth2


router = APIRouter()


@router.post("/fill_bottle/")
def fill_bottle(fill:bool = False,db:Session=Depends(get_db)):
    bottle = db.query(models.Fill_Bottle).first()
    if not bottle:
        bottle = models.Fill_Bottle()
        db.add(bottle)

    bottle.is_filled = fill
    db.commit()
    return{"message":f"bottle filled {fill}"}