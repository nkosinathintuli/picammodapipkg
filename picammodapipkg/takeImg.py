import time 
import picamera
import datetime 

def takeImg():

    camera = picamera.PiCamera()
    camera.resolution = (1024, 768)
    camera.start_preview()
    # Camera warm-up time
    time.sleep(2)

    dateAndTime = datetime.datetime.now()
    prefix = 'img_'
    suffix = dateAndTime.strftime("%Y%m%d_%H%M%S")
    filename = prefix+suffix

    camera.capture('/home/pi/picammodapipkg/picammodapipkg/imgOutput/'+filename+'.jpg')
    print("Image saved!")
    camera.stop_preview()
    camera.close()


