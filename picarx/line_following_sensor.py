from sensor_classes_w3 import SENSOR, INTERP,CONTROL
from picarx_improved import Picarx
import time

px = Picarx()

s = SENSOR(px)
i = INTERP(px)
c = CONTROL(px)

start = input("Press 'y' to begin line following. Once started, press 's' to stop")

speed = 25
while start == "y":
    px.forward(speed)
    sensor_vals = s.sensor_read()
    position = i.get_position(sensor_vals)
    c.correct_car(position)
    time.sleep(0.1)
    
    


    
    




