import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

EMAIL_ADDRESS = "meetsarvaiya41@gmail.com"
EMAIL_PASSWORD = "pfwr lcvx vgdc oexv"


def send_goal_achieved_email(receiver_email):
    try:
        # Email Content
        subject = "🎉 Goal Achieved!"
        body = f"Hi there!\n\nCongratulations! You have successfully achieved your water intake goal for today.\n\nStay hydrated! 💧"

        # Create message
        message = MIMEMultipart()
        message["From"] = EMAIL_ADDRESS
        message["To"] = receiver_email
        message["Subject"] = subject

        # Attach the body with MIMEText
        message.attach(MIMEText(body, "plain"))

        # Connect to Gmail SMTP server
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.ehlo()  # Can be omitted
            server.starttls()  # Secure the connection
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

            # Send the email
            server.sendmail(EMAIL_ADDRESS, receiver_email, message.as_string())

            print(f"✅ Email sent successfully to {receiver_email}")

    except Exception as e:
        print(f"❌ Failed to send email: {e}")


import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

EMAIL_ADDRESS = "meetsarvaiya41@gmail.com"
EMAIL_PASSWORD = "pfwr lcvx vgdc oexv"


def send_reminder_email(receiver_email):
    try:
        subject = "🚨 Hydration Reminder!"
        body = "Hey! You haven't drunk water in the last 20 minutes. Stay hydrated! 💧"

        message = MIMEMultipart()
        message["From"] = EMAIL_ADDRESS
        message["To"] = receiver_email
        message["Subject"] = subject
        message.attach(MIMEText(body, "plain"))

        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.sendmail(EMAIL_ADDRESS, receiver_email, message.as_string())

        print(f"✅ Reminder sent to {receiver_email}")

    except Exception as e:
        print(f"❌ Failed to send reminder to {receiver_email}: {e}")


import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

EMAIL_ADDRESS = "meetsarvaiya41@gmail.com"
EMAIL_PASSWORD = "pfwr lcvx vgdc oexv"


def send_warning_email(receiver_email):
    try:
        subject = "🚨 Hydration Warning!"
        body = "Hey! You haven't drunk water in the last 60 minutes. Stay hydrated! 💧 it's warning to stay hydrate otherwise your health will dehydrate "

        message = MIMEMultipart()
        message["From"] = EMAIL_ADDRESS
        message["To"] = receiver_email
        message["Subject"] = subject
        message.attach(MIMEText(body, "plain"))

        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.sendmail(EMAIL_ADDRESS, receiver_email, message.as_string())

        print(f"✅ Reminder  warning sent to {receiver_email}")

    except Exception as e:
        print(f"❌ Failed to send reminder to {receiver_email}: {e}")



import smtplib
from email.mime.text import MIMEText

def send_email(to, subject, body):
    sender_email = "meetsarvaiya41@gmail.com"
    sender_password = "pfwr lcvx vgdc oexv"

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = to

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, to, msg.as_string())

    print(f"Email sent to {to}")
