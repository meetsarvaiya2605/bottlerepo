from fastapi import APIRouter,HTTPException,Depends,status
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
import models,schemas
from database import get_db
import oauth2


router = APIRouter(
    prefix="/setgoal"
)
@router.post("/", response_model=schemas.GoalResponse)
def setgoal(goal: schemas.GoalSet,db: Session = Depends(get_db),current_user: models.User = Depends(oauth2.get_current_user)):
    setgoal = db.query(models.WaterGoal).filter(models.WaterGoal.user_id == current_user.id).first()
    
    if setgoal:
        setgoal.set_goal = goal.set_goal
    else:
   
        setgoal = models.WaterGoal(
            user_id=current_user.id, 
            set_goal=goal.set_goal
        )
        db.add(setgoal)
    db.commit()
    db.refresh(setgoal)
    return setgoal


@router.get("/")
def get_goal(db:Session=Depends(get_db),current_user:models.User= Depends(oauth2.get_current_user)):
    getgoal = db.query(models.WaterGoal).filter(models.WaterGoal.user_id==current_user.id).first()
    if not getgoal:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="goal not found")
    return getgoal