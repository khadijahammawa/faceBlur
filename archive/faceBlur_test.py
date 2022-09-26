# Import libraries
import os
import shutil

import cv2
import matplotlib.pyplot as plt
import numpy as np

img_path ='C:/Users/Khadija_Hammawa/Documents/GitHub/faceBlur/jamie/grass_test_LOD0_u0_v0.jpg'
        
image = cv2.imread(img_path)
        
h, w = image.shape[:2]

kernel_width = (w//7) | 1
kernel_height = (h//7) | 1

# adjust window
cv2.namedWindow("Select Rois", cv2.WINDOW_NORMAL)
# select ROIs function
ROIs = cv2.selectROIs("Select Rois",image)

# print rectangle points of selected roi
print(ROIs)

# loop over every boundaing box to save in array "ROIs"
for rect in ROIs:
    x1 = rect[0]
    y1 = rect[1]
    x2 = rect[2]
    y2 = rect[3]

    #print((x1, y1), (x2,y2))
    #select face roi
    face_roi = image[y1:y1+y2,x1:x1+x2]

    # applying a gaussian blur over this new rectangle area
    blurred_face = cv2.GaussianBlur(face_roi, (kernel_width, kernel_height), 0)

    # impose this blurred image on original image to get final image
    image[y1:y1+y2,x1:x1+x2] = blurred_face
    cv2.imwrite('C:/Users/Khadija_Hammawa/Documents/GitHub/faceBlur/blurred_img.jpg', img=image)

cv2.waitKey(0)