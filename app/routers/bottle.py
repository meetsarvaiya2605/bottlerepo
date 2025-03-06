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

@router.get("/{id}")
def get_bottle(id:int,db:Session=Depends(get_db)):
    bottle = db.query(models.Bottle).filter(models.Bottle.id == id).first()
    if not bottle:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="bottlen not found")
    return bottle

@router.delete("/{id}")
def delete_bottle(id:int,db:Session=Depends(get_db)):
    bottle = db.query(models.Bottle).filter(models.Bottle.id ==id)
    if bottle.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="bottle not faound")
    bottle.delete(synchronize_session=False)
    db.commit()
    return f"bottle {id} deleted successfully"
    
    