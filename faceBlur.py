# Import libraries
import os
import shutil

import cv2
import matplotlib.pyplot as plt
import numpy as np

# Initialize Directories
os.chdir('C:/Users/Khadija_Hammawa/Documents/GitHub/faceBlur/')
src_dir = 'C:/Users/Khadija_Hammawa/Documents/GitHub/faceBlur/'


SUBID='jamie'#input('Enter subject ID: ')
INPUT_DIR=f'{src_dir}{SUBID}/' 
OUTPUT_DIR=f'{src_dir}{SUBID}/blur/'

try:
    shutil.rmtree(OUTPUT_DIR)
except:
    os.mkdir(OUTPUT_DIR)
'''
for i,image in enumerate(os.listdir(INPUT_DIR)):
    if image.split('.')[-1].lower() == 'jpg' and image.split('_')[3].lower() == 'u0':
        filename = image
        print(OUTPUT_DIR + filename)
        image = cv2.imread(INPUT_DIR + filename)


        h, w = image.shape[:2]

        kernel_width = (w//7) | 1
        kernel_height = (h//7) | 1
        
        # # Draw rectangle around the faces which is our region of interest (ROI)
        #for x, y, w, h in faces:
        cv2.namedWindow('image', cv2.WINDOW_NORMAL)
        r = cv2.selectROI('image', image, showCrosshair=True)
        face_roi = image[int(r[1]):int(r[1]+r[3]),int(r[0]):int(r[0]+r[2])]
        
        # applying a gaussian blur over this new rectangle area
        blurred_face = cv2.GaussianBlur(face_roi, (kernel_width, kernel_height), 0)
        
        # impose this blurred image on original image to get final image
        image[int(r[1]):int(r[1]+r[3]),int(r[0]):int(r[0]+r[2])] = blurred_face
    
        cv2.imwrite(filename, image)
'''
#######selecting multiple ROIs#########
for i, image in enumerate(os.listdir(INPUT_DIR)):
    if image.split('.')[-1].lower() == 'jpg' and image.split('_')[3].lower() == 'u0':
        filename = image
        blurred_file = str(image)
        
        # = read image
        image = cv2.imread(INPUT_DIR + filename)
        
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
            cv2.imwrite('DEID_TEXTURE.JPG', image)

#############################################