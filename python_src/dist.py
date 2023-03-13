#!usr/bin/python
# -*- coding: utf-8 -*-
#定义编码，中文注释
 
#import the necessary packages
import numpy as np
import cv2
 
# 找到目标函数
def find_marker(image):
    # convert the image to grayscale, blur it, and detect edges
    #gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  
    circle1 = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 100, param1=180, param2=50, minRadius=10, maxRadius=270)
    if circle1 is None:
	return None
    circles = circle1[0, :, :]
    if circles is None:
	return None
    circles = np.uint16(np.around(circles))
    return circles
 
# 距离计算函数 
def distance_to_camera(knownWidth, focalLength, perWidth):  
    # compute and return the distance from the maker to the camera
    return (knownWidth * focalLength) / perWidth            
 
KNOWN_WIDTH = 25 #已知物体宽度

focalLength = 643.069627  #像素焦距
inches_reg = 0.0 
inches = 0.0
#打开摄像头
camera = cv2.VideoCapture('rtsp://admin:admin@192.168.42.108:554/cam/realmonitor?channel=1&subtype=0')#获取云台主视频流
while camera.isOpened():
    # get a frame
    (grabbed, frame) = camera.read()
    frame = cv2.resize(frame,(960,540))
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    circles = find_marker(gray)
    if circles is None:
	cv2.imshow("capture", gray)
	if cv2.waitKey(1) & 0xFF == ord('q'):
             break
	continue
    circle = circles[0]
    maxradius = 0
    flag = 0
    for i in circles[:]:
	if i[0] > 400 and i[0] < 560 and i[1] > 220 and i[1] < 320:
	   if i[2] > maxradius:
	   	 circle = i
	         maxradius = i[2]
		 flag = 1
    if flag == 1:
	inches_reg = inches
	cv2.circle(gray,(circle[0],circle[1]),circle[2],(255,0,0),5)
        cv2.circle(gray,(circle[0],circle[1]),2,(255,0,0),10)
	inches = distance_to_camera(KNOWN_WIDTH, focalLength, 2*circle[2])
    else:
	inches = inches_reg
    # draw a bounding box around the image and display it
    # inches 转换为 cm
    cv2.putText(gray, "%.2fcm" % (inches),
             (gray.shape[1] - 300, gray.shape[0] - 20), cv2.FONT_HERSHEY_SIMPLEX,2.0, (0, 255, 0), 3)
    print("%.2fcm" % inches) 
    # show a frame
    cv2.imshow("capture", gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
camera.release()
cv2.destroyAllWindows() 
 
