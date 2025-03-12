from fastapi import FastAPI ,HTTPException,Response, status,APIRouter,Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
import models,schemas
from database import get_db
import oauth2
from ..routers import email
from datetime import  datetime,timedelta
from apscheduler.schedulers.background import BackgroundScheduler
from sqlalchemy.orm import Session
from database import SessionLocal  # Your DB session
# from your_app.check_reminder import check_user_last_drink
# from .fillbottel import get_bottel
from sqlalchemy import TIMESTAMP
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

    goal = db.query(models.WaterGoal).filter(models.WaterGoal.user_id==current_user.id).first()
    if not goal:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="goal not found")
    goal.set_goal -= amount
    if goal.set_goal <= 0:
        email.send_goal_achieved_email(current_user.email_id)

        goal.set_goal = 0
    db.commit()
    db.refresh(goal)
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
        
        
            "success": True,
            "msg":"drink successfully",
            "id":bottle.id,
            "bottle_amount":bottle.bottle_amount,
            "bottle_capacity":bottle.bottle_capacity,
            "set_goal":goal.set_goal,
            "user_id":goal.user_id,
        
        }
        
    )


def check_user_last_drink(db: Session = SessionLocal()):
    now_time = datetime.utcnow()
    twenty_minutes_ago = now_time - timedelta(minutes=1)

    print(f"Check users who have not drunk water {twenty_minutes_ago}")

    users = db.query(models.User).all()
    for user in users:
        if user.notification_on and user.last_drink_time and user.last_drink_time < twenty_minutes_ago:

            # print(f"Sending reminder to {user.email_id}")
            email.send_reminder_email(user.email_id)
            # print( email.send_reminder_email(user.email_id))

        else:
            print(f"{user.email_id}  no reminder sent.")

def start_schedular():

    scheduler = BackgroundScheduler()
    def job():
        # print("Running scheduled job: check_user_last_drink")
        db = SessionLocal()
        try:
            check_user_last_drink(db)
        finally:
            db.close()


    scheduler.add_job(job, 'interval',minutes =1 )

    scheduler.start()
    print("Scheduler started!")