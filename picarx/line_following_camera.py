import cv2
import numpy as np
from vilib import Vilib
from picarx_improved import Picarx
from sensor_classes_w3 import CONTROL
import os
px = Picarx()
import time

C = CONTROL(px, scale_factor = 30)

def find_line(name, path):
    #Greyscale
    frame = cv2.imread(f'{path}/{name}.jpg')

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
        cv2.circle(frame, (x_center, frame.shape[0] // 2), 5, (0, 0, 255), -1)  # Red dot
        # Save the modified image
        cv2.imwrite(f'{path}/{name}.jpg', frame)
        

    print(("X_position",x_ratio))

    
    return x_ratio

# def calculate_angle(xval, frame_width):

#     scale_factor = (frame_width/2 - xval-frame_width/20)/frame_width

#     angle = scale_factor*90
#     print("Calculated angle: ", angle)

#     return angle


start = input("Press 'y' to begin line following. Once started, press 's' to stop")

px.set_cam_tilt_angle(-30)
Vilib.camera_start()
Vilib.display()

time.sleep(0.5)
speed = 25
t = 1
while start == "y":
    name = f"image{t}"  
    path = "picarx"
    
    status = Vilib.take_photo(name, path)  # Take the photo

    if status:
        full_path = f"{path}/{name}.jpg"
        if Vilib.img is not None and isinstance(Vilib.img, np.ndarray):
            cv2.imwrite(full_path, Vilib.img)  # Explicitly save the image
            t += 1
            print("Image", t, "saved successfully.")
        else:
            print("Error: Captured image is not valid.")
            continue
        
        if os.path.exists(full_path):  # Check if the image exists
            xval = find_line(name, path)
            #xval is where the line is, car is opposite:
            xval = -1* xval
            C.correct_car(xval)
        else:
            print(f"Image file does not exist: {full_path}")
            continue  # Handle the error appropriately

    px.forward(speed)
    time.sleep(0.2)

