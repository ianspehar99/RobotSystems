#!/usr/bin/env python3
from picarx_improved import Picarx 
import time

px = Picarx()


def forwards(angle,speed,t):
    print("rUNNING FW")
    px.set_dir_servo_angle(angle)
    print("aNGLE SET")
    px.forward(speed)
    print("PX FW called")
    time.sleep(t)
    px.stop()

#Instead of time, could change to distance
def backwards(angle,speed,t):
    px.set_dir_servo_angle(angle)
    px.backward(speed)
    time.sleep(t)
    px.stop()

def parallel_park(side):
    speed = 40
    reverse_angle_1 = 10
    reverse_angle_2 = 10
    
    if side == "left":
        px.set_dir_servo_angle(-1*reverse_angle_1)
        px.backward(speed)
        time.sleep(1)
        px.set_dir_servo_angle(1*reverse_angle_2)
        px.backward(speed)
        time.sleep(1)
        px.stop()
    else:
        px.set_dir_servo_angle(1*reverse_angle_1)
        px.backward(speed)
        time.sleep(1)
        px.set_dir_servo_angle(-1*reverse_angle_2)
        px.backward(speed)
        time.sleep(1)
        px.stop()

def k_turn(side):
    angle = 30
    speed = 30
    if side == "left":
        px.set_dir_servo_angle(-1*angle)
        px.backward(speed)
        time.sleep(2)
        px.set_dir_servo_angle(1*angle)
        px.forward(speed)
        time.sleep(2)
        px.set_dir_servo_angle(0)
        px.forward(speed)
        time.sleep(1)
        px.stop()
    else:
        px.set_dir_servo_angle(1*angle)
        px.backward(speed)
        time.sleep(2)
        px.set_dir_servo_angle(-1*angle)
        px.forward(speed)
        time.sleep(2)
        px.set_dir_servo_angle(0)
        px.forward(speed)
        time.sleep(1)
        px.stop()




