import picamera
import subprocess
import datetime 
import io
import os

import motionDetect

def takeVid(duration):

    camera = picamera.PiCamera()
    camera.resolution = (640, 480)

    e = datetime.datetime.now()
    currentDateTime =  str(e.year)+str(e.month)+str(e.day)+'_'+str(e.hour)+str(e.minute)+str(e.second)
    filePath =  '/home/pi/picammodapipkg/picammodapipkg/vidOutput/'
    fileName = 'vid_'+currentDateTime
    fileName_ext = fileName + '.h264'
    vidFile = filePath+fileName_ext
    #pathToFilename = '/home/pi/picammodapipkg/picammodapipkg/vidOutput/'+filename
    #filename_ext = filename+ 'h264'
    camera.start_recording(vidFile)
    camera.wait_recording(duration)
    camera.stop_recording()
    camera.close() # The camera is now closed.
    print("Finished recording!")
    convertVidToMp4(fileName, filePath)

def convertVidToMp4(filename, filepath):
    vidFile = filepath+filename
    print("The video is being converted to mp4")
    # Define the command we want to execute.
    command = "MP4Box -add "+vidFile+".h264" + " " +vidFile+ ".mp4"
    # Execute our command
    subprocess.call ([command], shell=True)
    # Video converted.
    print(filename+".h264 was successfully converted to " + filename+".mp4")
    os.remove(vidFile+'.h264')
    print(filename+".h264 removed!")

def takeVidOnMotion():
    
    camera = picamera.PiCamera()
    stream = picamera.PiCameraCircularIO(camera, seconds=20)
    camera.start_recording(stream, format='h264')
    try:
        while True:
            camera.wait_recording(1)
            if motionDetect.motion():
                # Keep recording for 10 seconds and only then write the
                # stream to disk
                camera.wait_recording(10)
                stream.copy_to('motion.h264')
    finally:
        camera.stop_recording()
    