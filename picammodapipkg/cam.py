import subprocess
import picamera
import datetime 
import time
import io
import os

import motionDetect

class cam: 
    defaultPath = ""
    defaultImgSet = ""
    defaultVidSet = ""
    #defaultImgName ="" 
    #defaultVidName = ""
    defaultVidLen = ""
    defaultVidExt = ""
    defaultImgExt = ""

    def takeImg():
        camera = picamera.PiCamera()
        camera.resolution = (1024, 768)
        camera.start_preview()
        # Camera warm-up time
        time.sleep(2)
        filename = generateDefaultName("img")
        camera.capture(filename+'.jpg')
        print(filename+" captured!")
        camera.stop_preview()
        camera.close()
    
    def takeImg(path):
        camera = picamera.PiCamera()
        camera.resolution = (1024, 768)
        camera.start_preview()
        # Camera warm-up time
        time.sleep(2)
        filename = generateDefaultName("img")
        camera.capture(path+filename+'.jpg')
        print(filename+" captured!")
        camera.stop_preview()
        camera.close()
    
    def setDefaultImgSet(settings):
        pass
    def takeVid():
        pass
    
    def takeVid(duration):
        camera = picamera.PiCamera()
        camera.resolution = (640, 480)
        filename = generateDefaultName("vid")
        camera.start_recording(filename+"h264")
        camera.wait_recording(duration)
        camera.stop_recording()
        camera.close() # The camera is now closed.
        print("video "+filename+" recorded")

    def takeVid(duration, path):
        camera = picamera.PiCamera()
        camera.resolution = (640, 480)
        filename = generateDefaultName("vid")
        camera.start_recording(path+filename+"h264")
        camera.wait_recording(duration)
        camera.stop_recording()
        camera.close() # The camera is now closed.
        print("video "+filename+" recorded")
    
    def takeVidOnMotion(settings):
        pass
    def setDefaultVidSet(settings):
        pass
    def folderExist(foldername):
        pass
    def fileExist(filename):
        pass
    
    def generateDefaultName(prefix):
        dateAndTime = datetime.datetime.now()
        suffix = dateAndTime.strftime("%Y%m%d_%H%M%S")
        filename = prefix+"_"+suffix
        return filename
    
    