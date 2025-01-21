import picarx_improved as px
import time


def forwards(angle,speed,time):
    px.set_dir_servo_angle(angle)
    px.forward(speed)
    time.sleep(time)
    px.stop()

#Instead of time, could change to distance
def backwards(angle,speed,time):
    px.set_dir_servo_angle(angle)
    px.backward(speed)
    time.sleep(time)
    px.stop()

def parallel_park(side):
    speed = 10
    reverse_angle_1 = 20
    reverse_angle_2 = 20
    
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



