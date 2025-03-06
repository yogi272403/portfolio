import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Load SMTP credentials from environment variables
SMTP_SERVER = os.getenv("SMTP_SERVER")
SMTP_PORT = int(os.getenv("SMTP_PORT", 587))
SMTP_USERNAME = os.getenv("SMTP_USERNAME")
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD")

def send_email(sender_email, sender_name, message_body):
    print(f"🔗 Connecting to SMTP server: {SMTP_SERVER}:{SMTP_PORT}")
    print(f"📩 Sending email from: {SMTP_USERNAME} to yogipatel2724@gmail.com")

    receiver_email = "yogipatel2724@gmail.com"
    subject = f"New Contact Form Submission from {sender_name}"

    msg = MIMEMultipart()
    msg["From"] = SMTP_USERNAME  # Use your verified Sendinblue email
    msg["To"] = receiver_email
    msg["Reply-To"] = sender_email
    msg["Subject"] = subject

    body = f"Name: {sender_name}\nEmail: {sender_email}\n\nMessage:\n{message_body}"
    msg.attach(MIMEText(body, "plain"))

    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.set_debuglevel(1)  # Enable debug output
        server.starttls()
        print("🔑 Logging into SMTP...")
        server.login(SMTP_USERNAME, SMTP_PASSWORD)
        print("📨 Sending email...")
        server.sendmail(SMTP_USERNAME, receiver_email, msg.as_string())
        server.quit()

        print("✅ Email sent successfully!")
        return "success"
    except Exception as e:
        print(f"❌ Error sending email: {e}")
        return f"error: {e}"  # Return the actual error message
