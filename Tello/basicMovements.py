from djitellopy import tello
import time

tellin = tello.Tello()
tellin.connect()
print("Bateria ne")
print(tellin.get_battery())

tellin.takeoff()
time.sleep(4)


tellin.move_forward(50)
time.sleep(5)
"""
tellin.send_rc_control(0,0,0,100)
sleep(4)
tellin.send_rc_control(0,0,0,0)
sleep(2)
tellin.send_rc_control(0,-30,0,0)
sleep(5)
tellin.send_rc_control(0,0,0,0)
sleep(2)
"""

#tellin.flip_forward()
tellin.land()
time.sleep(2)




