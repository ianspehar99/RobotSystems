import cv2
import numpy as np
from vilib import Camera
from picarx import Picarx
px = Picarx()
import time

def find_line(frame):
    #Greyscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    #Get binary image
    _, binary = cv2.threshold(gray, 60, 255, cv2.THRESH_BINARY_INV)
    
    #Find contours
    contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    center_line = max(contours, key = cv2.contourArea)
    # Find the leftmost point of the largest contour
    left_point = tuple(center_line[center_line[:,:,0].argmin()][0])
        
    # Get the x-coordinate of the leftmost point
    xval = left_point[0]
        
    # Get the width of the frame
    frame_width = frame.shape[1]

    
    return xval, frame_width

def calculate_angle(xval, frame_width):

    scale_factor = (frame_width/2 - xval-frame_width/20)/frame_width

    return scale_factor*90




start = input("Press 'y' to begin line following. Once started, press 's' to stop")

px.set_cam_tilt_angle(-20)
speed = 25
while start == "y":
    px.forward(speed)
    camera = Camera()
    frame = camera.read()
    xval, frame_width = find_line(frame)    
    angle = calculate_angle(xval, frame_width)  
    px.set_dir_servo_angle(angle)
    
    time.sleep(0.1)
    start = input("Press 's' to stop the car")


        
    

    





        
       

