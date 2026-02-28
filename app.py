from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import os

app = Flask(__name__)

@app.route("/whatsapp", methods=["POST"])
def whatsapp_bot():
    incoming_msg = request.values.get('Body', '').strip().lower()
    resp = MessagingResponse()
    msg = resp.message()

    # MAIN MENU
    if incoming_msg == "hi":
        msg.body(
            "Welcome to DY Patil College of Engineering and Technology 🎓
We are delighted to connect with you! Our institution is committed to providing quality education, innovation, and excellent career opportunities. Please let us know how we can assist you today — whether it’s about courses, admissions, or campus facilities. We’re here to help!\n\n"
            "1️⃣college info\n"
            "2️⃣ Admissions\n"
            "3️⃣ branches\n"
            "4️⃣ contact\n\n"
            "Reply with number (1-4)"
        )

    # OPTION 1
    elif incoming_msg == "1":
        msg.body(
            "Located in kolhapur\n"
            "•Has 3.5+ avg LPA\n"
            "•Create oppurtuinities\n\n"
            "Type 'menu' to go back."
        )

    # OPTION 2
    elif incoming_msg == "2":
        msg.body(
            "Basically based on CET Rounds\n"
            "• Cutoff based system\n"
            "• All scholerships available\n"
            "Type 'menu' to go back."
        )

    # OPTION 3
    elif incoming_msg == "3":
        msg.body(
            "8+ branches available\n"
            "Gives most of demsnding branches\n"
            "Special faculty for each branch\n\n"
            "Type 'menu' to go back."
        )

    # OPTION 4
    elif incoming_msg == "4":
        msg.body(
            "🤖 CaptainBot v1.0\n"
            "Built with Python + Flask\n"
            "Deployed on Cloud 🚀\n\n"
            "Type 'menu' to go back."
        )

    else:
        msg.body("Type 'menu' to start.")

    return str(resp)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))

    app.run(host="0.0.0.0", port=port)
