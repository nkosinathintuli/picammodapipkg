import anvil.server
import picamera
import smtplib
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login("iraspberry87@gmail.com","32113140997")
online=False

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
        server.sendmail("iraspberry87@gmail.com","ntaboka87@gmail.com",mse)
        server.quit()

@anvil.server.callable
def display_message():
    global message
    return message

def main():
    global online
    while True:
        print(" ")

if __name__=="__main__":
    main()

