import cv2
import numpy as np
from vilib import Camera

def process_frame(frame):
    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Apply a binary threshold to get a binary image
    _, binary = cv2.threshold(gray, 60, 255, cv2.THRESH_BINARY_INV)
    
    # Find contours in the binary image
    contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Draw contours on the original frame
    cv2.drawContours(frame, contours, -1, (0, 255, 0), 2)
    
    return frame

def main():
    # Initialize the camera
    camera = Camera()
    
    while True:
        # Capture a frame from the camera
        frame = camera.read()
        
        # Process the frame to detect the line
        processed_frame = process_frame(frame)
        
        # Display the processed frame
        cv2.imshow('Line Following', processed_frame)
        
        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    # Release the camera and close all OpenCV windows
    camera.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()