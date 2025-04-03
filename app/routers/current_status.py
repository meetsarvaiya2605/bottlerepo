from apscheduler.schedulers.background import BackgroundScheduler
from sqlalchemy.orm import Session
from datetime import date
import models
from database import SessionLocal
from ..routers import email
from apscheduler.triggers.cron import CronTrigger


scheduler = BackgroundScheduler()


def send_daily_status_emails():
    db: Session = SessionLocal()
    try:
        users = db.query(models.User).all()

        for user in users:
            bottle = db.query(models.Bottle).filter(models.Bottle.user_id == user.id).first()

            total_capacity = bottle.bottle_capacity  
       
            total_drink = bottle.total_amount if bottle.total_amount else 0
            remaining = total_capacity - total_drink
            subject = f"Your Daily Water Intake Summary - {date.today().strftime('%d %b %Y')}"
            message = (
                f"Hello {user.firstname},\n\n"
                f"Here is your water intake summary for today:\n"
                f"- Total Bottle Capacity: {total_capacity} ml\n"
                f"- Water Drank Today: {total_drink} ml\n"
                f"- Remaining Water: {remaining if remaining > 0 else 0} ml\n\n"
                "Remember to stay hydrated!\n\n"
                "Best,\n"
                "Bottle Management Team"
            )

            # Call your email sending function
            email.send_email(to=user.email_id, subject=subject, body=message)
            bottle.total_amount = 0
            db.commit()

            # print(f"Sent daily status email to {user.email_id}")

    except Exception as e:
        print(f"Error sending daily emails: {e}")

    finally:
        db.close()



def start_scheduler():
    
    scheduler.add_job(
        send_daily_status_emails,
        trigger=CronTrigger(hour=0, minute=0),
        id='daily_email_job',
        replace_existing=True
    )

    scheduler.start()
    