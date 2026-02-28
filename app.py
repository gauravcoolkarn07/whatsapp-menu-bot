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

    if incoming_msg in ["hi","hii","hello","hey","start"]:
        reply = """Welcome to DY Patil College of Engineering and Technology 🎓

We are delighted to connect with you! Our institution is committed to providing quality education and innovation.

How can we assist you today?

1️⃣ About College
2️⃣ Courses Offered
3️⃣ Contact Details
4️⃣ Admission Process
"""

    elif incoming_msg == "1":
        reply = """DY Patil College of Engineering and Technology is located in Kolhapur and provides quality technical education with modern infrastructure.

Visit our official website for more information:
https://coek.dypgroup.edu.in/
"""

    elif incoming_msg == "2":
        reply = """📚 Courses Offered:

Reply with course code:

C1️⃣ Computer Science Engineering
C2️⃣ CS Specialization in Data Science
C3️⃣ Mechanical Engineering
C4️⃣ Civil Engineering
C5️⃣ Chemical Engineering
C6️⃣ Electrical Engineering
C7️⃣ AI & ML
C8️⃣ Robotics & Automation
C9️⃣ 📄 Cutoff List
"""

    elif incoming_msg == "c1":
        reply = "CSE focuses on programming, AI, Data Science and software development."

    elif incoming_msg == "c2":
        reply = "CSDS focuses on Data management and Data mining."

    elif incoming_msg == "c3":
        reply = "Mechanical Engineering focuses on machines, thermodynamics and design."

    elif incoming_msg == "c4":
        reply = "Civil Engineering focuses on construction and infrastructure."

    elif incoming_msg == "c5":
        reply = "Chemical Engineering focuses on chemicals and industrial processes."

    elif incoming_msg == "c6":
        reply = "Electrical Engineering focuses on power systems and electrical machines."

    elif incoming_msg == "c7":
        reply = "AI & ML focuses on Machine Learning and data analysis."

    elif incoming_msg == "c8":
        reply = "Robotics & Automation focuses on intelligent machines and automation systems."

    elif incoming_msg == "c9":
        msg.media("https://drive.google.com/uc?export=download&id=1iQd1_x99xhyvVct0nkqXuL1r1ain8ot2")
        msg.body("📄 Here is the official cutoff list.\n\nType 2️⃣ to return to Courses menu.")
        return str(response)

    elif incoming_msg == "3":
        reply = "📞 Contact Us:\nPhone: +91-XXXXXXXXXX\nEmail: info@dypatil.edu"

    elif incoming_msg == "4":
        reply = "Admissions are based on entrance exams and merit. Visit our official website for details."

    else:
        reply = "Please type 'Hi' to return to main menu."

    msg.body(reply)
    return str(response)

if __name__ == "__main__":
    app.run(debug=True)

