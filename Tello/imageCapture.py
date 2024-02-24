from djitellopy import tello
from time import sleep

tellin = tello.Tello()
tellin.connect()
print(tellin,get_battery())

tellin.streamon()
