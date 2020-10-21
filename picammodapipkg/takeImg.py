from time import sleep
from picamera import PiCamera
import datetime 

def takeImg():

    camera = PiCamera()
    camera.resolution = (1024, 768)
    camera.start_preview()
    # Camera warm-up time
    e = datetime.datetime.now()
    sleep(2)

    currentDateTime =  '_'+str(e.year)+str(e.month)+str(e.day)+'_'+str(e.hour)+str(e.minute)+str(e.second)
    filename = 'img'+currentDateTime
    camera.capture('/home/pi/picammodapipkg/picammodapipkg/imgOutput/'+filename+'.jpg')
    camera.stop_preview()
    camera.close()

