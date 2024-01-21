from djitellopy import tello
from time import sleep

tellin = tello.Tello()
tellin.connect()
print(tellin.get_battery())

tellin.takeoff()
tellin.send_rc_control(0,50,0,0)
sleep(2)
tellin.send_rc_control(0,-50,0,0)
sleep(2)
tellin.land()




