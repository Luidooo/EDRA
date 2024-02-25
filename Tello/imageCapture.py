from djitellopy import tello
import cv2

tellin = tello.Tello()
tellin.connect()
print(tellin.get_battery())

tellin.streamon()

while  True:
    img = tellin.get_frame_read().frame
    img = cv2.resize(img,(360,240))
    cv2.imshow("Image", img)
    cv2.waitKey(1)

