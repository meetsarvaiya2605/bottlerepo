from fastapi import FastAPI
from database import engine
import models
from app.routers import user, bottle, auth, email, fillbottel, goal_set
from app.routers.fillbottel import start_schedular
from database import SessionLocal
from app.routers.current_status import send_daily_status_emails 


app = FastAPI()
models.Base.metadata.create_all(bind=engine)


app.include_router(user.router)
app.include_router(bottle.router)
app.include_router(auth.router)
# app.include_router(email.router)
app.include_router(fillbottel.router)
app.include_router(goal_set.router)

@app.on_event("startup")
def startup_event():
    start_schedular()

@app.get("/send-daily-emails")
def trigger_daily_emails():
    send_daily_status_emails()    
    # start_schedular()
    return {"message": "Daily status emails sent!"}