from djitellopy import tello
from time import sleep
import numpy as np
import cv2
import Keypressmodel as kp


######## PARAMETERS #########
#speeds in cm/s

fSpeed = 117/10 # 15cm/s
aSpeed = 360/10 # degres/s
interval = 0.25

dInterval = fSpeed*interval
aInterval = aSpeed*interval
#############################

x,y = 500,500
a = 0

kp.init()
tello = tello.Tello()
tello.connect()
print(tello.get_battery())

#tello.streamon()


def getKeyboardInput():
    lr, fb, ud, yv = 0, 0, 0, 0
    speed = 50
    d = 0

    if kp.getKey("LEFT"):
        lr = -speed
    elif kp.getKey("RIGHT"):
        lr = speed
    if kp.getKey("UP"):
        fb = speed
    elif kp.getKey("DOWN"):
        fb = -speed
    if kp.getKey("w"):
        ud = speed
    elif kp.getKey("s"):
        ud = -speed
    if kp.getKey("a"):
        yv = speed
    elif kp.getKey("d"):
        yv = -speed

    if kp.getKey("q"): tello.land()
    if kp.getKey("e"): tello.takeoff()

    return [lr, fb, ud, yv]

def drawPoints():
    cv2.circle(img, (x,y), 5, (0,0,255), cv2.FILLED)

while True:
    vals = getKeyboardInput()
    tello.send_rc_control(vals[0], vals[1], vals[2], vals[3])

    img = np.zeros((1000,1000,3), np.uint8)
    drawPoints()
    cv2.imshow("Output", img)
    cv2.waitKey(1)
