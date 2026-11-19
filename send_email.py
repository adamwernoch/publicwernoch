import os
import smtplib
from email.message import EmailMessage

sender = os.environ["GMAIL_ADDRESS"]
password = os.environ["GMAIL_APP_PASSWORD"]
recipient = os.environ["RECIPIENT"]

msg = EmailMessage()
msg["From"] = f"STOP APARTMENT BOT <{sender}>"
msg["To"] = recipient
msg["Subject"] = "APARTMENT BOT"
msg.set_content("TURN IT OFF")

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
    smtp.login(sender, password)
    smtp.send_message(msg)

print("Sent to", recipient)
