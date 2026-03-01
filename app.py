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
4️⃣ Facilities🚌
"""

    elif incoming_msg == "1":
        msg.media("https://drive.google.com/uc?export=download&id=1qZcrfrgNR4lzItRAKHD2w0GOlppJjyh3")
        msg.body("DY Patil College of Engineering and Technology, Kolhapur, is a premier institution dedicated to excellence in technical education. With modern infrastructure, experienced faculty, and industry-oriented programs, the college prepares students for successful careers in engineering, innovation, and research.About DY Patil College Brochure Link is given above: \n\nType 2️⃣ to return to Courses menu.")
        return str(response)

    elif incoming_msg == "2":
        reply = """📚 Courses Offered:

Reply with course code:

 A 🖥️Computer Science Engineering
 B 🌐CSE(Data Science)
 C 🤖CSE(AI&ML)
 D 🏚️Civil Engineering
 E 🧪Chemical Engineering
 F ⚡Electrical Engineering
 G  🚗Mechanical Engineering
 H 📄 Cutoff List
"""

    elif incoming_msg == "a":
        msg.media("https://drive.google.com/uc?export=download&id=1o1s7TXSydZRVAu_LQ3sjSevxgZ3r4tan")
        msg.body("DY Patil College offers a comprehensive Computer Science Engineering (CSE).🖥️ program that focuses on programming, software development, AI, and data science. Students gain hands-on experience with modern technologies and are prepared for careers in IT and research\n\nType 2️⃣ to return to Courses menu.")
        return str(response)
        
    elif incoming_msg == "b":
        msg.media("https://drive.google.com/uc?export=download&id=1mZjQXQUZjH6DZQLvuSatK9S9QO8JcAT0")
        msg.body("📄The CS Data Science program at DY Patil College emphasizes data management, machine learning, and analytics.\n\nType 2️⃣ to return to Courses menu.")
        return str(response)
        
    elif incoming_msg == "c":
        msg.media("https://drive.google.com/uc?export=download&id=165KbsNUqyvVNVKW5WxYDbGO75vniEWrL")
        msg.body("The AI & ML program 🤖 at DY Patil College focuses on artificial intelligence, machine learning, and data analysis. Students learn to develop intelligent systems and apply AI solutions to real-world problems.\n\nType 2️⃣ to return to Courses menu.")
        return str(response)

    elif incoming_msg == "d":
        msg.media("https://drive.google.com/uc?export=download&id=1HkoInTHKu4O9VRIV-0WE0SV-LOv2pbEv")
        msg.body("The Civil Engineering program 🏚️ at DY Patil College emphasizes construction, structural design, and infrastructure development. Students gain practical knowledge in building safe and sustainable structures.\n\nType 2️⃣ to return to Courses menu.")
        return str(response)
         
    elif incoming_msg == "e":
        msg.media("https://drive.google.com/uc?export=download&id=1Vo7KxZAFxft9vSylEDtTySs_rjYyZYmr")
        msg.body("The Chemical Engineering program 🧪 at DY Patil College focuses on chemical processes, industrial operations, and material science. Students learn to design and manage safe, efficient chemical production systems.\n\nType 2️⃣ to return to Courses menu.")
        return str(response)
        
    elif incoming_msg == "f":
        msg.media("https://drive.google.com/uc?export=download&id=177WUJaxxInFR5sjxNNth-DBffnTytwbe")
        msg.body("The Electrical Engineering program ⚡ at DY Patil College focuses on power systems, electrical machines, and energy management. Students gain hands-on experience in designing, operating, and maintaining electrical infrastructure.\n\nType 2️⃣ to return to Courses menu.")
        return str(response)
        

    elif incoming_msg == "g":
        msg.media("https://drive.google.com/uc?export=download&id=1QAusOiXYO1cdmhYaxj7_n0SSYpebycFB")
        msg.body("The Mechanical Engineering program 🚗 at DY Patil College focuses on design, thermodynamics, and machinery. Students gain practical skills in mechanical systems, manufacturing processes, and engineering problem-solving\n\nType 2️⃣ to return to Courses menu.")
  
    elif incoming_msg == "h":
        msg.media("https://drive.google.com/uc?export=download&id=1iQd1_x99xhyvVct0nkqXuL1r1ain8ot2")
        msg.body("📄 Here is the official cutoff list.\n\nType 2️⃣ to return to Courses menu.")
        return str(response)

    elif incoming_msg == "3":
        reply = "📞 Contact Us:\nPhone: 0231-2601431/32/33\nEmail:info.dypcet@dypgroup.edu.in"

    elif incoming_msg == "4":
        reply = "1️⃣ Bus🚌 Our college provides safe and reliable bus transportation covering major city routes for students and staff \n\n2️⃣ Library📚 The college library offers a vast collection of books, journals, digital resources, and a peaceful study environment.\n\n3️⃣LLC (Liberal Learning Courses)🎓 Our college offers 25 Liberal Learning Course (LLC) clubs that enhance students’ skills beyond academics through diverse extracurricular activities.\n\n4️⃣ Canteen🍽️ The college canteen serves hygienic, affordable, and nutritious food for students and staff.\n\n5️⃣ NCC🎖️ NCC develops discipline, leadership, and patriotism through structured military training programs.️⃣ NSS🤝 NSS encourages social responsibility by engaging students in community service and social development activities.\n\n7️⃣ Cultural Activities🎭 The cultural committee organizes events, competitions, and festivals to showcase students’ creative talents.\n\n8️⃣ Sports / Gymkhana🏆 The Gymkhana promotes physical fitness through various indoor and outdoor sports facilities and tournaments. "

    else:
        reply = "Please type 'Hi' to return to main menu."

    msg.body(reply)
    return str(response)

if __name__ == "__main__":
    app.run(debug=True)















