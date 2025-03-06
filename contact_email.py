import smtplib
import json
import sys
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Load SMTP credentials from config.json
with open("config.json", "r") as config_file:
    config = json.load(config_file)

SMTP_SERVER = config["SMTP_SERVER"]
SMTP_PORT = config["SMTP_PORT"]
SMTP_USERNAME = config["SMTP_USERNAME"]
SMTP_PASSWORD = config["SMTP_PASSWORD"]

def send_email(sender_email, sender_name, message_body):
    receiver_email = "yogipatel2724@gmail.com"  # Your email to receive messages
    subject = f"New Contact Form Submission from {sender_name}"

    msg = MIMEMultipart()
    msg["From"] = SMTP_USERNAME  # Use your own email as the sender
    msg["To"] = receiver_email
    msg["Reply-To"] = sender_email  # Helps when replying
    msg["Subject"] = subject

    body = f"Name: {sender_name}\nEmail: {sender_email}\n\nMessage:\n{message_body}"
    msg.attach(MIMEText(body, "plain"))

    try:
        print("🔗 Connecting to SMTP server...")
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
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
        return "error"

# Test the function
if __name__ == "__main__":
    # Get input from command-line arguments
    if len(sys.argv) < 4:
        print("❌ Error: Missing arguments. Usage: python3 contact_email.py <email> <name> <message>")
        sys.exit(1)

    sender_email = sys.argv[1]
    sender_name = sys.argv[2]
    message_body = sys.argv[3]

    # Call the function to send an email
    result = send_email(sender_email, sender_name, message_body)
    
    # Print result for PHP to capture
    print(result)