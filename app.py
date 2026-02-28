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

We are delighted to connect with you! Our institution is committed to providing quality education and innovation.🤖🔥


How can we assist you today?🤝😎

1️⃣ About College 🏫
2️⃣ Courses Offered 📚
3️⃣ Contact Details ☎️
4️⃣ Admission Process 🚌
"""

    elif incoming_msg == "1":
        msg.media("https://drive.google.com/uc?export=download&id=10l5hIezC8o9IMdY-auwKp_3i2jb62r68")
        msg.body("\n\nType 2️⃣ to return to Courses menu.")
        return str(response)

    elif incoming_msg == "2":
        reply = """📚 Courses Offered:

Reply with course code:

 A 🖥️Computer Science Engineering
 B 🌐CS Specialization in Data Science
 C 🚗Mechanical Engineering
 D 🏚️Civil Engineering
 E 🧪Chemical Engineering
 F ⚡Electrical Engineering
 G 🤖Artificial intelligence and machine learning
 H 📄 Cutoff List
"""

    elif incoming_msg == "a":
        msg.media("https://drive.google.com/uc?export=download&id=1UZ5w2lS_dg7ll2ezRMehSPaGMfh1vV67")
        msg.body("DY Patil College of Engineering and Technology, Kolhapur, offers quality technical education with modern infrastructure and experienced faculty. We provide programs in engineering, AI, and emerging technologies to prepare students for successful careers.\n\nType 2️⃣ to return to Courses menu.")
        return str(response)
        
    elif incoming_msg == "b":
        msg.media("https://drive.google.com/uc?export=download&id=1s7HKZ_ea7mEG9s-MTNBNOWE8bZ3h6BbA")
        msg.body("📄The CS Data Science program at DY Patil College emphasizes data management, machine learning, and analytics. Students learn to extract insights from large datasets and apply modern AI and data science tools for real-world solutions\n\nType 2️⃣ to return to Courses menu.")
        return str(response)
        
    elif incoming_msg == "c":
        msg.media("https://drive.google.com/uc?export=download&id=1JRQarK_87ehltm1DxaZLTB7FBE1sFUMc")
        msg.body("The Mechanical Engineering program at DY Patil College focuses on design, thermodynamics, and machinery. Students gain practical skills in mechanical systems, manufacturing processes, and engineering problem-solving\n\nType 2️⃣ to return to Courses menu.")
        return str(response)

    elif incoming_msg == "d":
        msg.media("https://drive.google.com/uc?export=download&id=1kQ_7wQ-bbJAMlrbABWxNDIoJAp-9NA8j")
        msg.body("The Civil Engineering program at DY Patil College emphasizes construction, structural design, and infrastructure development. Students gain practical knowledge in building safe and sustainable structures.\n\nType 2️⃣ to return to Courses menu.")
        return str(response)
         
    elif incoming_msg == "e":
        msg.media("https://drive.google.com/uc?export=download&id=1Vn2G2wdyD0pRu1R_tuNu4GteJYnYNNwv")
        msg.body("The Chemical Engineering program at DY Patil College focuses on chemical processes, industrial operations, and material science. Students learn to design and manage safe, efficient chemical production systems.\n\nType 2️⃣ to return to Courses menu.")
        return str(response)
        
    elif incoming_msg == "f":
        msg.media("https://drive.google.com/uc?export=download&id=1qpXdv9atZJKxYdiC-NW__AKMaWGcDb2h")
        msg.body("The Electrical Engineering program at DY Patil College focuses on power systems, electrical machines, and energy management. Students gain hands-on experience in designing, operating, and maintaining electrical infrastructure.\n\nType 2️⃣ to return to Courses menu.")
        return str(response)
        

    elif incoming_msg == "g":
        msg.media("https://drive.google.com/uc?export=download&id=1DP6VJYwKu_ipGmCA1zgM2nYux0MrW_Fa")
        msg.body("The AI & ML program at DY Patil College focuses on artificial intelligence, machine learning, and data analysis. Students learn to develop intelligent systems and apply AI solutions to real-world problems.\n\nType 2️⃣ to return to Courses menu.")
        return str(response)
  
    elif incoming_msg == "h":
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







