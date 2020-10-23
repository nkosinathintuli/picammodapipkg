import takeImg 
#import takeVid
import motionDetect
import smtplib
import anvil.server

anvil.server.connect('BP2P6K2WEAVZG7EMXI56O6AU-2HHQWLD3DEXHTCGB')
server=smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login("iraspberry87@gmail.com","cam25project")
moitionState = False
online2=False
message2=" "

@anvil.server.callable
def detectmotion():
    global online2
    if online2==False:
        online2=True
    elif online2==True:
        online2=False

@anvil.server.callable
def display_message2():
    global message2
    return "Motion detection started"

while True:
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login("iraspberry87@gmail.com","cam25project")
    motionState = motionDetect.motion()
    
    if online2==True:
        if motionState:
            takeImg.takeImg()
            message2="MOTION DETECTED!"
            message="motion was detected at the site"
            mse="Subject: {}\n\n{}".format("MOTION DETECTED",message)
            server.sendmail("iraspberry87@gmail.com","iraspberry87@gmail.com",mse)
            server.quit()
            print("MOTION DETECTED!")
#            online2=False
#        print("Motion was detected!")
