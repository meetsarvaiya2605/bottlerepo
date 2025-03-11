from fastapi import FastAPI ,HTTPException,Response, status,APIRouter,Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
import models,schemas
from database import get_db
import oauth2
# from .fillbottel import get_bottel
# from models import Bottle
 
router = APIRouter(
    prefix="/bottles"
)

@router.get("/", response_model=schemas.BottleResponse)
def get_user_bottle(db: Session = Depends(get_db), current_user: models.User = Depends(oauth2.get_current_user)):
    bottle = db.query(models.Bottle).filter(models.Bottle.user_id == current_user.id).first()

    if not bottle:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Bottle not found")
    return bottle

@router.post("/fill")
def fill_bottle(db: Session = Depends(get_db), current_user: models.User = Depends(oauth2.get_current_user)):
    bottle = db.query(models.Bottle).filter(models.Bottle.user_id == current_user.id).first()

    if not bottle:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Bottle not found")


    bottle.bottle_amount = bottle.bottle_capacity
    db.commit()
    db.refresh(bottle)
    # return {"message ":"bottle filled"}
  
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            "success": True,
            "msg":"filled successfully",
            "id": bottle.id,
            "bottle_capacity": bottle.bottle_capacity,
            "bottle_amount": bottle.bottle_amount,
            "created_at": bottle.created_at.isoformat()
        }
        
    )


@router.post("/empty")
def empty_bottle(db:Session=Depends(get_db),current_user: models.User = Depends(oauth2.get_current_user)):
    bottle = db.query(models.Bottle).filter(models.Bottle.user_id == current_user.id).first()

    if not bottle:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="bottle not found")

    bottle.bottle_amount=0
    db.commit()
    db.refresh(bottle)
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            "success": True,
            "msg":"empty successfully",
            "id":bottle.id
            

        }
        
    )

@router.post("/drink")
def drink_water(amount:int,db:Session=Depends(get_db),current_user: models.User = Depends(oauth2.get_current_user)):
    bottle = db.query(models.Bottle).filter(models.Bottle.user_id== current_user.id).first()

    if not bottle:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="bottle not found")
    
    if amount<=0:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="amount is not should be zero ")
    
    if amount>bottle.bottle_amount:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="user input is not valid or not enough space in bottle")
    
    bottle.bottle_amount-= amount
    db.commit()
    db.refresh(bottle)
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            "success": True,
            "msg":"drink successfully",
            "id":bottle.id,
            "bottle_amount":bottle.bottle_amount,
            "bottle_capacity":bottle.bottle_capacity
        }
        
    )

