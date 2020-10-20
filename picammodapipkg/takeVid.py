import picamera
from subprocess import call
import os
import datetime 

def takeVid():

    camera = picamera.PiCamera()
    camera.resolution = (640, 480)

    e = datetime.datetime.now()
    currentDateTime =  '_'+str(e.year)+str(e.month)+str(e.day)+'_'+str(e.hour)+str(e.minute)+str(e.second)
    filename = 'vid'+currentDateTime
    #filename_ext = filename+ 'h264'
    camera.start_recording('/home/pi/picammodapipkg/picammodapipkg/vidOutput/'+filename+'.h264')
    camera.wait_recording(30)
    camera.stop_recording()
    print("Finished recording!")


    # The camera is now closed.
    pathToFilename = '/home/pi/picammodapipkg/picammodapipkg/vidOutput/'+filename

    print("The video is being converted to mp4")
    # Define the command we want to execute.
    command = "MP4Box -add "+pathToFilename+".h264" + " " +pathToFilename+ ".mp4"
    # Execute our command
    call ([command], shell=True)
    # Video converted.
    print(filename+".h264 was successfully converted to " + filename+".mp4")
    os.remove(pathToFilename+'.h264')
    print(filename+".h264 deleted!")