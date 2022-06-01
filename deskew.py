
# Deskewing process
# Created by Ramazan AYDINLI

import cv2 as cv
import numpy as np

# Assignment of image
img=cv.imread("img_path")

# Image parameters are defined
height_img=img.shape[0]
width_img=img.shape[1]

# Image turned into grayscale
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Some blur are applied
img_blur = cv.GaussianBlur(img_gray, (5,5), 1)

# Canny applied
img_canny = cv.Canny(img_blur,200,200)

# Dilation applied
kernel = np.ones((5,5))
img_dilated = cv.dilate(img_canny,kernel,iterations=2)

# Threshold image created
img_thres = cv.erode(img_dilated, kernel, iterations=1)

# Image copied, contours will be drawn on this copy
img_contour = img.copy()

# Opencv contour function
contours, hierarchy = cv.findContours(img_thres, cv.RETR_EXTERNAL,cv.CHAIN_APPROX_NONE)

# Biggest contour is assigned
biggest = np.array([])
maxArea = 0

# Loop below will execute all contours and returns the biggest one
for cnt in contours:
    area = cv.contourArea(cnt)
    if area > 5000:
        peri = cv.arcLength(cnt, True)
        approx = cv.approxPolyDP(cnt, 0.02*peri,True)
        if area > maxArea and len(approx) == 4:
            biggest = approx
            maxArea = area
        x,y,w,h = cv.boundingRect(approx)
    cv.drawContours(img_contour, biggest, -1, (255, 0, 0), 30)

# for taking the exact part of image, 4 corner points in the biggest array will be assigned as current points
current_points=biggest.reshape((4,2))

# code below are used to get the coordinates of the corners and seperating them according to their true location
new_points = np.zeros((4,1,2),np.int32)
add = current_points.sum(1)
new_points[0] = current_points[np.argmin(add)]
new_points[3]= current_points[np.argmax(add)]
diff = np.diff(current_points,axis=1)
new_points[1]=current_points[np.argmin(diff)]
new_points[2]=current_points[np.argmax(diff)]
biggest = new_points

# Code below gets the corner points and redraws the images useful part
# top left of the screen is the origin (0,0) point
points1=np.float32(biggest)
points2=np.float32([[0,0],[width_img,0],[0,height_img],[width_img,height_img]])
matrix = cv.getPerspectiveTransform(points1,points2)
img_Output = cv.warpPerspective(img, matrix, (width_img, height_img))
img_cropped = img_Output[10:img_Output.shape[0]-10,10:img_Output.shape[1]-10]
img_cropped = cv.resize(img_cropped,(width_img,height_img))

cv.imshow("Final Image", img_cropped)
cv.waitKey(0)
