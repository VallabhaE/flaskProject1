import os

from flask import Flask, render_template, redirect
from flask import request
import smtplib
import re
class Projects:
    number = 1
    git = ""
    name = ""
    data = ""
    def __init__(self,n,git,name,data):
        self.number = n
        self.git = git
        self.name = name
        self.data = data

project1 = Projects(1,"https://github.com/VallabhaE/TicTacToe","Tic Tac Toe GUI Python","I have created Tic Tac Toe Gui using Python and Tkinter in a simple Way")
project2 = Projects(2,"https://github.com/VallabhaE/Text_to_Morse_GUI/blob/master/main.py","Text2Morse","a sleek and intuitive GUI text-to-Morse code converter. This innovative tool seamlessly transforms written words into Morse code with a user-friendly interface,")
project3 = Projects(3,"https://github.com/VallabhaE/WaterMarkonImage/blob/master/main.py","ImageWatermarkingSystem","I managed to create a gui application for my watermarking app on image.i have to add functions to buttions.still lot more to do in this porject ,just stopped in middle")
project4 = Projects(4,"https://github.com/VallabhaE/WPMChecker","WordsPerMinChecker","🚀 Just built a sleek Words-Per-Minute checker with a cool GUI! ✨ Test your typing speed and challenge yourself.#CodingFun,")
emailLogin = "eashwarvallabha180@gmail.com"
information = ''' 
Hello! I'm Eswar Vallabha R, a software developer who graduated with a B.Tech from Karunya University in 2024. I began my professional journey with an internship at Skill Vertix during my final year, followed by a second internship at ZOHO, which transitioned into a full-time developer role. I was also a runner-up in the TRIOS Hackathon at my college. My technical skills include proficiency in Linux and Go, along with experience in Java (competitive programming), Python, Flask, React, and Angular. I excel at quickly learning and adapting to new technologies, continuously striving to expand my expertise and stay ahead in the tech field. Additionally, I am an active participant on LeetCode, where I have solved over 250 problems, honing my problem-solving and coding skills.
 '''
app = Flask(__name__)
projectInfoData = []
projectInfoData.append(project1)
projectInfoData.append(project2)
projectInfoData.append(project3)
projectInfoData.append(project4)
app.config['SECRET_KEY'] = os.environ.get('FLASK_KEY')
@app.route('/')
def Home(username=None,be=0):
    return render_template('index.html',e=username,c=be)

@app.route("/contact")
def contact():
    return render_template('contact.html')

@app.route("/about")
def about():
    return render_template('about.html',data=information,ResumeLink="https://drive.google.com/file/d/1ZZSUPFtIZunlVjx5yFA5DM0rIBv3OQUo/view")

@app.route("/works")
def work():
    return render_template("work.html",projectInfoData=projectInfoData)

@app.route("/<string:a>")
def red(a="/"):
    try:
        return render_template(a)
    except:
        return redirect("/")

@app.route("/submit",methods=["POST","GET"])
def sumbit_form():
    if request.method=="POST":
        email=request.form["email"]
        subject=request.form["subject"]
        messgae=request.form["message"]
        regex = r'\b[A-Za-z0-9._%+-]+@gmail.com'
        if not (re.fullmatch(regex, email)):
            return render_template('error.html',error = "Error Wrong Email Buddy Cant send your Email Please Check It")

        print(email,messgae)
        server = smtplib.SMTP("smtp.gmail.com", 587, timeout=120)
        server.starttls()
        server.login(emailLogin,app.config['SECRET_KEY'])
        server.sendmail(emailLogin,email,"ThankYou for Giving FeedBack")
        server.sendmail(emailLogin,"ramagownieswar@karunya.edu.in","From\n"+email+"\n"+messgae)
        return redirect("/")
    return "Give Proper Resopnse"


if __name__=="__main__":
    app.run(debug=True)
