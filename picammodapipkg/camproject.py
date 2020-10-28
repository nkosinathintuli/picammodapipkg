import anvil.server
import picamera
import takeImg
import adc
import smtplib
import motionDetect

motionState = False
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login("iraspberry87@gmail.com","cam25project")
online=False
online2=False
started=False

anvil.server.connect("BP2P6K2WEAVZG7EMXI56O6AU-2HHQWLD3DEXHTCGB")

camera = picamera.PiCamera();
camera.resolution = (1024, 768);
message = " "
message2=" "

@anvil.server.callable
def takevideo():
    global online
    if online==False:
        online=True
        start_stop(online)
    elif online==True:
        online=False
        start_stop(online)

@anvil.server.callable
def takelightvideo():
    global message
    global online2
    if online2==False:
        online2=True
        message="light induced recording enabled"
    elif online2==True:
        online2=False
        message="light induced recording disabled"

def start_stop(on1):
    global message
    global server
    if on1==True:
        camera.start_recording('Desktop/footage.h264')
        message="recording started"
    elif on1==False:
        camera.stop_recording()
        message="footage captured"
        mse="Subject: {}\n\n{}".format("NEW FOOTAGE CAPTURED", "A new video recording has just been captured on your device")
        server.sendmail("iraspberry87@gmail.com","iraspberry87@gmail.com",mse)
        server.quit()

def light_induced(ldr):
    global started
    if started==False:
        if ldr<=200:
            camera.start_recording('Desktop/lightfootage.h264')
            started=True
    elif started==True:
        if ldr>200:
            camera.stop_recording()
            started=False
            server = smtplib.SMTP('smtp.gmail.com',587)
            server.starttls()
            server.login("iraspberry87@gmail.com","cam25project")
            mse="Subject: {}\n\n{}".format("NEW LIGHT INDUCED FOOTAGE CAPTURED", "A new light triggered video has been captured")
            server.sendmail("iraspberry87@gmail.com","iraspberry87@gmail.com",mse)
            server.quit()

@anvil.server.callable
def display_message():
    global message
    return message

try:
    while True:
        if online2==True:
            light_induced(adc.readadc(0))
        print "light = ",adc.readadc(0)
except KeyboardInterrupt:
    print("program terminated")

