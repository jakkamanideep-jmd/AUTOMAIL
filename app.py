from flask import Flask,render_template,url_for,flash,redirect
import smtplib
import speechrecognition as sr
import pyttsx3
from email.message import EmailMessage

listener=sr.Recognizer()
tts=pyttsx3.init()
app=Flask(__name__)

@app.route("/home",methods=["POST","GET"])
def home():
    return render_template("thehome.html")


@app.route("/mainpage",methods=["POST","GET"])
def mainpage():
    def speaker(text):
        say=tts.say(text)
        say.runandwait()

    def mic():
        with sr.Microphone() as source:
            voice=listener.listen(source)
            data=listener.recognize_google(voice)
            print(data)
            return data.lower()
    dic_t={"manideep":"jakkamanideep@gmail.com"}
    def sendmessage(receiver,subject,body):
        server=smtplib.SMTP("smtp.gmail.com",587)
        server.starttls()
        server.login("jakkamanideep@gmail.com","02558510")
        email=EmailMessage()
        email["From"]="jakkamanideep@gmail.com"
        email["To"]=receiver
        email["subject"]=subject
        email.setcontent(body)
        server.send_message(email)
        
    
    speaker("tell me the name of receiver") 
    name=mic()
    receiver=dic_t[name]
    speaker("tell me the subject")
    subject=mic()
    speaker("tell me the content")
    body=mic()
    sendmessage(receiver, subject, body)
    return render_template("mainpage.html",receiver=receiver,name=name,subject=subject,body=body)
    


if __name__=="__main__":
    app.run(debug=True)