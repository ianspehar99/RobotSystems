import cv2
import numpy as np
from vilib import Vilib
from picarx_improved import Picarx
from sensor_classes_w3 import CONTROL
import os
import concurrent.futures
px = Picarx()
import time



#FOR POLLING SENSE FASTER THAN INTERPRET, INTEPRPRET FASTER THAN CONTROL
#iNTERPRETER ALREADY LAGS, SO WANT IT TO BE TAKING IN THE MOST RECENT SENSOR VALUE AS POSSIBLE
#scale of 5 each time you go up
#0.5,0.1,0.02
#Define general bus class
class Bus:

    def __init__(self):
        self.message = None

    def read(self):
        return(self.message)

    def write(self, data):
        self.message = data

bus12 = Bus()  #Bus instance for transfer from sensor to interpreter

bus23 = Bus() #Bus instance for transfer from interpreter to controller

#Set delay for loops
sensor_delay = 0.02
interp_delay = 0.1
control_delay = 0.5
#Producer function
def sensor(bus12,sensor_delay):

    Vilib.camera_start()
    Vilib.display()
    time.sleep(0.5)
    t = 1
    go = True
    while go:
        name = f"image{t}"  
        path = "picarx"

        status = Vilib.take_photo(name, path)
        if status:
            full_path = f"{path}/{name}.jpg"
            if Vilib.img is not None and isinstance(Vilib.img, np.ndarray):
                cv2.imwrite(full_path, Vilib.img)  # Save the image
                t += 1
                frame = cv2.imread(f'{path}/{name}.jpg')
                print("Image", t, "saved successfully.")
                bus12.write(frame)
                
            else:
                print("Image not valid")
                continue

        time.sleep(sensor_delay)
    
#Read and write function

def interpreter(bus12, bus23,interp_delay):

    go = True
    while go:
        frame = bus12.read()

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        #Get binary image
        _, binary = cv2.threshold(gray, 60, 255, cv2.THRESH_BINARY_INV)
        
        #Focus on bottom half of image
        frame_height = frame.shape[0]
        frame_width = frame.shape[1]

        lower_half = binary[frame_height//2:,:]
        #Find contours
        contours, _ = cv2.findContours(lower_half, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        center_line = max(contours, key = cv2.contourArea)

        
        # Find centroid point of the largest contour
        centroid = cv2.moments(center_line)
        if centroid['m00'] !=0:
            x_center = int(centroid['m10'] / centroid['m00'])
            x_ratio = (x_center - frame_width / 2) / (frame_width / 2) #Get x in terms of -1 to 1

        time.sleep(interp_delay)
        bus23.write(x_ratio)


#Consumer function -- Changes angle based on x_value
def controller(bus23,control_delay):
    C = CONTROL(px, scale_factor = 30)
    go = True
    while go:
        x = bus23.read()
        xval = -1*x
        C.correct_car(xval)
        time.sleep(delay)

start = input("Press 'y' to begin line following. Once started, press 's' to stop")

px.set_cam_tilt_angle(-30)

with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
    eSensor = executor.submit(sensor, bus12,
    sensor_delay)
    eInterpreter = executor.submit(interpreter,
    bus12, bus23,interp_delay)
    eController = executor.submit(controller,bus23,control_delay)

