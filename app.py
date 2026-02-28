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
    if incoming_msg == "menu":
        msg.body(
            "🤖 CaptainBot Main Menu\n\n"
            "1️⃣ IPL Info\n"
            "2️⃣ Python Help\n"
            "3️⃣ Motivation\n"
            "4️⃣ About\n\n"
            "Reply with number (1-4)"
        )

    # OPTION 1
    elif incoming_msg == "1":
        msg.body(
            "🏏 IPL Info:\n"
            "• Season starts March 2026\n"
            "• 10 Teams Competing\n\n"
            "Type 'menu' to go back."
        )

    # OPTION 2
    elif incoming_msg == "2":
        msg.body(
            "💻 Python Help:\n"
            "• Practice daily\n"
            "• Build projects\n"
            "• Learn Flask & APIs\n\n"
            "Type 'menu' to go back."
        )

    # OPTION 3
    elif incoming_msg == "3":
        msg.body(
            "🔥 Motivation:\n"
            "Discipline > Motivation\n"
            "Consistency wins ❤️‍🔥\n\n"
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