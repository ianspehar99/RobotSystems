#!/usr/bin/env python3
from picarx_improved import Picarx 
import time

px = Picarx()

def calibrate(zero):
    px.dir_servo_calibrate(zero)
    

def forwards(angle,speed,t):
    px.set_dir_servo_angle(angle)
    px.forward(speed)
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
    reverse_angle_1 = 25
    reverse_angle_2 = 25
    
    if side == "left":
        px.set_dir_servo_angle(-1*reverse_angle_1)
        px.backward(speed)
        time.sleep(1)
        px.set_dir_servo_angle(1*reverse_angle_2)
        px.backward(speed)
        time.sleep(0.87)
        px.stop()
        px.set_dir_servo_angle(0)
        px.forward(1)
        time.sleep(1)
        px.stop()
    else:
        px.set_dir_servo_angle(1*reverse_angle_1)
        px.backward(speed)
        time.sleep(1)
        px.set_dir_servo_angle(-1*reverse_angle_2)
        px.backward(speed)
        time.sleep(0.87)
        px.stop()
        px.set_dir_servo_angle(0)
        time.sleep(1)
        px.forward(1)
        time.sleep(1)
        px.stop()

def k_turn(side):
    angle = 30
    speed = 40
    if side == "left":
        px.set_dir_servo_angle(1*angle)
        px.backward(speed)
        time.sleep(2)
        px.set_dir_servo_angle(-1*angle)
        #time.sleep(2)
        px.forward(speed)
        time.sleep(1.9)
        px.set_dir_servo_angle(0)
        px.forward(speed)
        time.sleep(1)
        px.stop()
    else:
        px.set_dir_servo_angle(-1*angle)
        px.backward(speed)
        time.sleep(2)
        px.set_dir_servo_angle(1*angle)
        #time.sleep(2)
        px.forward(speed)
        time.sleep(1.9)
        px.set_dir_servo_angle(0)
        px.forward(speed)
        time.sleep(1)
        px.stop()

