import anvil.server
import picamera
import time
import adc
import smtplib
import motionDetect

motionState = False
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login("iraspberry87@gmail.com","cam25project")
online=False
online2=False

anvil.server.connect("BP2P6K2WEAVZG7EMXI56O6AU-2HHQWLD3DEXHTCGB")

camera = picamera.PiCamera();
camera.resolution = (1024, 768);
message = " "

@anvil.server.callable
def takevideo():
    global online
    if online==False:
        online=True
        start_stop(online)
    elif online==True:
        online=False
        start_stop(online)

'''@anvil.server.callable
def detectmotion():
    global online2
    if online2==False:
        online2=True
#        motiondetect(online2)
    elif online2==True:
        online2==False
#        motiondetect(online2)'''

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

'''def motiondetect(on2):
    global motionState
    global server
    if on2==True:
        while True:
            motionState = motionDetect.motion()
            if motionState:
                mse="MOTION WAS DETECTED!"
                server.sendmail("iraspberry87@gmail.com","ntaboka87@gmail.com",mse)
                server.quit()'''

@anvil.server.callable
def display_message():
    global message
    return message

def main():
# global online2
#    global server
#    global motionState
    while True:
#        if online2==True:
#            motionState=motionDetect.motion()
#            if motionState:
#                mse="MOTION WAS DETECTED!"
#                server.sendmail("iraspberry87@gmail.com","iraspberry87@gmail.com",mse)
#                server.quit()
#                 print("nl")'''
        if adc.readadc(0)<100:
            print("light level is low")
            print(adc.readadc(0))
            print(" ")
        elif adc.readadc(0)<200:
            print("light level is medium")
            print(adc.readadc(0))
            print(" ")
        else:
            print("light level is high")
            print(adc.readadc(0))
            print(" ")

if __name__=="__main__":
    main()

