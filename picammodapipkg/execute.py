import takeImg 
import takeVid
import motionDetect


moitionState = False
while True:
    motionState = motionDetect.motion()
    if motionState:
        takeImg.takeImg()
        print("Motion was detected!")
