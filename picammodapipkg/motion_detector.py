"""This module contains the functions involved in
motion detection and sending of email alerts.

"""

import takeImg 
import motionDetect
import smtplib
import anvil.server

from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders

anvil.server.connect('BP2P6K2WEAVZG7EMXI56O6AU-2HHQWLD3DEXHTCGB')
server=smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login("iraspberry87@gmail.com","cam25project")
moitionState = False
online2=False
message2=" "

@anvil.server.callable
def detectmotion():
    """This callable function enables or disables motion detection"""
    global message2
    global online2
    if online2==False:
        online2=True
        message2="Motion detection started"
    elif online2==True:
        online2=False
        message2="Motion detection stopped"

@anvil.server.callable
def display_message2():
    """This callable function returns an alert message on button press"""
    global message2
    return message2

def send_mail(filename):
    """Send an email with image attachment"""
    msg = MIMEMultipart()
    msg['From'] = 'iraspberry87@gmail.com'
    msg['To']='iraspberry87@gmail.com'
    msg['Subject']='Movement Detected'
    body ='Picture attached'
    msg.attach(MIMEText(body, 'plain'))
    attachement=open(filename, 'rb')
    part=MIMEBase('application','octet-stream')
    part.set_payload((attachement).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition','attachement; filename=%s'% filename)
    msg.attach(part)
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login('iraspberry87@gmail.com','cam25project')
    text=msg.as_string()
    server.sendmail('iraspberry87@gmail.com','iraspberry87@gmail.com',text)
    server.quit()

try:
    while True:
        server=smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()
        server.login("iraspberry87@gmail.com","cam25project")
        motionState = motionDetect.motion()
        if online2==True:
            if motionState:
                img=takeImg.takeImg()
                send_mail(img)
                print("MOTION DETECTED!")
except KeyboardInterrupt:
    print("program terminated")  # This is the output when the program is terminated
