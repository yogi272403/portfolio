import os
from flask import Flask, request, jsonify
from contact_email import send_email  # Import your existing email function

app = Flask(__name__)

@app.route('/send-email', methods=['POST'])
def send_email_api():
    data = request.json
    sender_email = data.get("email")
    sender_name = data.get("name")
    message_body = data.get("message")

    if not sender_email or not sender_name or not message_body:
        return jsonify({"error": "Missing required fields"}), 400

    result = send_email(sender_email, sender_name, message_body)
    if result == "success":
        return jsonify({"message": "Email sent successfully!"}), 200
    else:
        return jsonify({"error": "Failed to send email"}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))  # Default to 10000 if PORT is not set
    app.run(host="0.0.0.0", port=port, debug=True)
