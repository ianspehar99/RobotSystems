import cv2
import numpy as np
from vilib import Vilib
from picarx_improved import Picarx
from sensor_classes_w3 import CONTROL
import time
import rossros as rr

px = Picarx()

#Line following functions:
def sensor_cam():

    Vilib.camera_start()
    Vilib.display()
    time.sleep(0.2)
    t = 1
   
    name = f"image{t}"  
    path = "picarx"

    status = Vilib.take_photo(name, path)
    if status:
        full_path = f"{path}/{name}.jpg"
        if Vilib.img is not None and isinstance(Vilib.img, np.ndarray):
            cv2.imwrite(full_path, Vilib.img)  # Save the image
            t += 1
            frame = cv2.imread(f'{path}/{name}.jpg')
            return frame 
        else:
            print("Image not valid")

def interp_cam(frame):

    if frame is None:
        print("No frame available")
          # Sleep briefly to avoid busy waiting

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
        # Draw a red dot at the x_center position
        # cv2.circle(frame, (x_center, frame.shape[0] // 2), 5, (0, 0, 255), -1)  # Red dot
        # # Save the modified image
        # cv2.imwrite(f'{path}/{name}.jpg', frame)
    if x_ratio is not None:
        return x_ratio
    else:
        print("x was None")

def angle_controller(x):
    C = CONTROL(px, scale_factor = 30)
        
    #print("X RATIO CONTROLLER YIPPIE:", x)
    xval = -1*x
    C.correct_car(xval)

    #px.forward(25)

#Ultrasonic sensor functions:

#1. Read sensor
def sonic_sensor():
    distance = round(px.ultrasonic.read(), 2)
    return distance

#2. Decide to move px.forward or px.stop based on sensor reading
def sonic_stop(distance):
    safe_d = 40
    speed = 25
    if distance >= safe_d:
        px.forward(speed)
    elif distance < safe_d:
        px.stop
    else:
        px.forward(speed)

    
#Create wrapper for each of the ultrasonicconsumers/producers like in the example code, 
# then when you create the list at the end include everything
#Then, use rr.run_concurrently with that comprehensive list as the input



 

        
