import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(sender_email, sender_name, message_body):
    SMTP_SERVER = "smtp-relay.brevo.com"
    SMTP_PORT = 587
    SMTP_USERNAME = "yogipatel2724@gmail.com"  
    SMTP_PASSWORD = "t6VJ5yHazkCb7KF1"  

    # Email content
    receiver_email = "yogipatel2724@gmail.com" 
    subject = f"New Contact Form Submission from {sender_name}"

    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg["Subject"] = subject

    body = f"Name: {sender_name}\nEmail: {sender_email}\n\nMessage:\n{message_body}"
    msg.attach(MIMEText(body, "plain"))

    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()  
        server.login(SMTP_USERNAME, SMTP_PASSWORD) 
        server.sendmail(sender_email, receiver_email, msg.as_string()) 
        server.quit()
        return "success"
    except Exception as e:
        return "error"
