from fastapi import FastAPI, HTTPException,APIRouter
from pydantic import BaseModel, EmailStr
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

router= APIRouter()
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SMTP_EMAIL = "meetsarvaiya41@gmail.com"  
SMTP_PASSWORD = "pfwr lcvx vgdc oexv" 

class EmailRequest(BaseModel):
    to_email: EmailStr
    subject: str
    body: str

@router.post("/send-email/")
def send_email(request: EmailRequest):
    try:
        # Create email message
        msg = MIMEMultipart()
        msg["From"] = SMTP_EMAIL
        msg["To"] = request.to_email
        msg["Subject"] = request.subject
        msg.attach(MIMEText(request.body, "plain"))

        # Connect to SMTP server
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()  # Secure connection
        server.login(SMTP_EMAIL, SMTP_PASSWORD)
        server.sendmail(SMTP_EMAIL, request.to_email, msg.as_string())
        server.quit()

        return {"message": "Email sent successfully", "to": request.to_email}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to send email: {str(e)}")
