#!usr/bin/python
# -*- coding: utf-8 -*-
#定义编码，中文注释
 
#import the necessary packages
import numpy as np
import cv2
 
# 找到目标函数
def find_marker(image):
    # convert the image to grayscale, blur it, and detect edges
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  
    gray = cv2.GaussianBlur(gray, (5, 5), 0)        
    edged = cv2.Canny(gray, 35, 125)               
    #ret,binary = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
    # find the contours in the edged image and keep the largest one;
    # we'll assume that this is our piece of paper in the image
    (_,cnts,_) = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)  
    #(_,cnts,_) = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # 求最大面积 
    c = max(cnts, key = cv2.contourArea) 
    # compute the bounding box of the of the paper region and return it
    # cv2.minAreaRect() c代表点集，返回rect[0]是最小外接矩形中心点坐标，
    # rect[1][0]是width，rect[1][1]是height，rect[2]是角度
    return cv2.minAreaRect(c)
 
# 距离计算函数 
def distance_to_camera(knownWidth, focalLength, perWidth):  
    # compute and return the distance from the maker to the camera
    return (knownWidth * focalLength) / perWidth            
 
# initialize the known distance from the camera to the object, which
# in this case is 24 inches
#KNOWN_DISTANCE = 24.0
KNOWN_DISTANCE = 27.48

# initialize the known object width, which in this case, the piece of
# paper is 11 inches wide
# A4纸的长和宽(单位:inches)
#KNOWN_WIDTH = 11.69
KNOWN_WIDTH = 3.43
#KNOWN_HEIGHT = 8.27
KNOWN_HEIGHT = 4.50 
# initialize the list of images that we'll be using
IMAGE_PATHS = "Picture3.png"
 
# load the furst image that contains an object that is KNOWN TO BE 2 feet
# from our camera, then find the paper marker in the image, and initialize
# the focal length
#读入第一张图，通过已知距离计算相机焦距
image = cv2.imread(IMAGE_PATHS) 
marker = find_marker(image)          
print(marker[1][0],marker[1][1],marker[2]) 
focalLength = (marker[1][0] * KNOWN_DISTANCE) / KNOWN_WIDTH  
 
#通过摄像头标定获取的像素焦距
#focalLength = 811.82
print('focalLength = ',focalLength)

box = np.int0(cv2.boxPoints(marker))
cv2.drawContours(image, [box], -1, (0, 255, 0), 2)
while(1):
    # show a frame
    cv2.imshow("capture", image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows() 
 
