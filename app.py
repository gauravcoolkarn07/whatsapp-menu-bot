from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "DY Patil WhatsApp Bot is Running 🚀"

@app.route("/whatsapp", methods=["POST"])
def whatsapp():
    incoming_msg = request.values.get("Body", "").strip().lower()
    response = MessagingResponse()
    msg = response.message()

    # Welcome Trigger
    if incoming_msg in ["hi", "hello", "hey", "start"]:
        reply = """Welcome to DY Patil College of Engineering and Technology 🎓

We are delighted to connect with you! Our institution is committed to providing quality education, innovation, and excellent career opportunities.

How can we assist you today?

1️⃣ About College
2️⃣ Courses Offered
3️⃣ Contact Details
4️⃣ Admission Process
"""

    elif incoming_msg == "1":
        reply = "DY Patil College of Engineering and Technology is located in Kolhapur and provides quality technical education with modern infrastructure."

    elif incoming_msg == "2":
        reply = "We offer BTech programs in CSE, IT, Mechanical, Civil, and more."

    elif incoming_msg == "3":
        reply = "📞 Contact Us:\nPhone: +91-XXXXXXXXXX\nEmail: info@dypatil.edu"

    elif incoming_msg == "4":
        reply = "Admissions are based on entrance exams and merit. Visit our official website for detailed admission procedures."

    else:
        reply = """Please choose a valid option:

1️⃣ About College
2️⃣ Courses Offered
3️⃣ Contact Details
4️⃣ Admission Process

Type 'Hi' to return to main menu.
"""

    msg.body(reply)
    return str(response)


if __name__ == "__main__":
    app.run(debug=True)

