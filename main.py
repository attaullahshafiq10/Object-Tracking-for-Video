#attaullah

# Import the OpenCV and NumPy modules:
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Create a Video Capture object for the input video called lemon.mp4:
cap = cv2.VideoCapture('E:\Attaullah.mp4')


# Check whether the video was opened successfully or not:
if cap.isOpened == False:
    print('Opening error in video')


#Create three windows. These will be used to display our input frame, our output frame, and the mask.
cv2.namedWindow('Input Video', cv2.WINDOW_NORMAL)
cv2.namedWindow('Output Video', cv2.WINDOW_NORMAL)
cv2.namedWindow('Mask', cv2.WINDOW_NORMAL)


# Create an infinite while loop for reading frames, processing them, and displaying the output frames:
while True:
    # Capture a frame from the video using cap.read():
    ret, frame = cap.read()
    
    # Check whether the video has ended or not.
    if ret == False:
        break
        
    # Convert our frame into the HSV color space. We are doing this so that we can easily use the hue channel for thresholding:
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    #Next, obtain the hue channel and apply thresholding. Set all the pixels greater than 40 to 0 and less or equal set to 1. 
    h = hsv[:, :, 0]
    # applying thresholding, We arrive at the value 40 by trial and error.
    hcopy = h.copy()
    h[hcopy > 40] = 0
    h[hcopy <= 40] = 1
    
    # we will display the new mask (h), input the video frame, and output the frame
    cv2.imshow('input video', frame)
    cv2.imshow('output video', frame * h[:, :, np.newaxis])
    cv2.imshow('Hue', h * 255)
        
    # We can quit the process in the middle of it being run if we press the Esc key:
    k = cv2.waitKey(10)
    if k == 27:
        break

# Outside of the while loop, release the VideoCapture object and close all the open display windows:
cap.release()
cv2.destroyAllWindows()