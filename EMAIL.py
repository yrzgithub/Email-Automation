from smtplib import SMTP
from email.message import EmailMessage
from pyttsx3 import init
import emoji

convertor = init()


def Say(text):
    convertor.say(text)
    print(text)
    convertor.runAndWait()


server = SMTP(host="smtp.gmail.com", port=587)
server.starttls()  # Transport layer security..Mail is encrypted..
server.login("seenusanjay20102002@gmail.com", "")
email = EmailMessage()
email["From"] = "seenusanjay20102002@gmail.com"
email["To"] = "seenusanjay20102002@gmail.com"
email["Subject"] = "Testing of email automation...Sorry boss!" + emoji.emojize(":grinning_face_with_sweat:")

for i in range(1):
    msg = str(i) + ".Shall we add this feature of sending mails to other people in our project?"
    email.set_content(msg)
    server.send_message(email)
    Say(i)
