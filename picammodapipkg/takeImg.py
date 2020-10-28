<<<<<<< HEAD
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


=======
"""This module contains the function for taking a 1024x768 image.
This module is imported by the motion_detect.py module

"""
from time import sleep
from picamera import PiCamera
import datetime 

def takeImg():
    """Captures a 1024x768 image and saves it on storage"""
    camera = PiCamera()
    camera.resolution = (1024, 768)
    camera.start_preview()
    # This is the camera warm-up time
    e = datetime.datetime.now()
    sleep(5)
    currentDateTime =  '_'+str(e.year)+str(e.month)+str(e.day)+'_'+str(e.hour)+str(e.minute)+str(e.second)
    filename = 'img'+currentDateTime
    camera.capture('/home/pi/Desktop/'+filename+'.jpg')
    camera.stop_preview()
    camera.close()
>>>>>>> ea4eedec8cc8356c889d69ec0765d77532902832
