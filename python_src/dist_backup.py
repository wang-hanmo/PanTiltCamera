#!usr/bin/python
# -*- coding: utf-8 -*-
#定义编码，中文注释
 
#import the necessary packages
import numpy as np
import cv2
 
# 找到目标函数
def find_marker(image):
    # convert the image to grayscale, blur it, and detect edges
    color_lower = np.array([0, 43, 26])
    color_upper = np.array([10, 255, 255])
    frame = cv2.GaussianBlur(image, (5, 5), 0)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, color_lower, color_upper)
    # 图像学膨胀腐蚀
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.GaussianBlur(mask, (3, 3), 0)
    res = cv2.bitwise_and(frame, frame, mask=mask)
    #gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  
    #gray = cv2.GaussianBlur(image, (5, 5), 0)        
    #edged = cv2.Canny(gray, 35, 125)               
    #ret,binary = cv2.threshold(gray,0,255,cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
    # find the contours in the edged image and keep the largest one;
    # we'll assume that this is our piece of paper in the image
    #(_,contours,_) = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)  
    (_,contours,_) = cv2.findContours(mask.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    if len(contours) == 0:
	return 0
    c = contours[0]
    maxarea = 0
    for cnt in range(len(contours)):
	epsilon = 0.01 * cv2.arcLength(contours[cnt],True)
	approx = cv2.approxPolyDP(contours[cnt],epsilon,True)
	corners = len(approx)
	# 求解中心位置
        #mm = cv2.moments(contours[cnt])
	#if mm['m00'] == 0:
	#   continue
        #cx = int(mm['m10'] / mm['m00'])
        #cy = int(mm['m01'] / mm['m00'])
        # 颜色分析
        #color = frame[cy][cx]
	#print(color[0], color[1], color[2])
	if corners >= 10:
	    #if color[0] < 83 and color[1] < 85 and color[2] > 215:
	    #if cv2.minAreaRect(contours[cnt])[1][0] - cv2.minAreaRect(contours[cnt])[1][1] < 50 and cv2.minAreaRect(contours[cnt])[1][1] - cv2.minAreaRect(contours[cnt])[1][0] < 50: 
		if cv2.contourArea(contours[cnt]) > maxarea:
		    c = contours[cnt]
		    maxarea = cv2.contourArea(contours[cnt])
    # 求最大面积 
    #c = max(cnts, key = cv2.contourArea)
    # compute the bounding box of the of the paper region and return it
    # cv2.minAreaRect() c代表点集，返回rect[0]是最小外接矩形中心点坐标，
    # rect[1][0]是width，rect[1][1]是height，rect[2]是角度
    return cv2.minAreaRect(c)
 
# 距离计算函数 
def distance_to_camera(knownWidth, focalLength, perWidth):  
    # compute and return the distance from the maker to the camera
    return (knownWidth * focalLength) / perWidth            
 
KNOWN_WIDTH = 4.9 #已知物体宽度

focalLength = 450.148739  #像素焦距
 
#打开摄像头
camera = cv2.VideoCapture('rtsp://admin:admin@192.168.42.108:554/cam/realmonitor?channel=1&subtype=0')#获取云台主视频流
 
while camera.isOpened():
    # get a frame
    (grabbed, frame) = camera.read()
    frame = cv2.resize(frame,(720,540))
    #hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    #define the high limit and low limit
    #lower_white = np.array([0,20,20])
    #higher_white = np.array([10, 255, 255])
    #get the white part from picture
    #cv2.imwrite("./1.png",frame)
    #mask = cv2.inRange(hsv, lower_white, higher_white)
    #cv2.imwrite("./2.png",mask)
    #left_white = cv2.bitwise_and(frame, frame, mask = mask)
    #cv2.imwrite("./3.png",left_white)
    marker = find_marker(frame)
    if marker == 0:
	#print(marker)
	continue
    if marker[1][0] == 0:
	continue
    inches = distance_to_camera(KNOWN_WIDTH, focalLength, marker[1][0])
 
    # draw a bounding box around the image and display it
    box = np.int0(cv2.boxPoints(marker))
    cv2.drawContours(frame, [box], -1, (0, 255, 0), 2)
    #box = np.int0(cv2.boxPoints(circle))
    #cv2.drawContours(frame,[box],-1,(0,255,0),2)
    # inches 转换为 cm
    cv2.putText(frame, "%.2fcm" % (inches),
             (frame.shape[1] - 300, frame.shape[0] - 20), cv2.FONT_HERSHEY_SIMPLEX,2.0, (0, 255, 0), 3)
 
    # show a frame
    cv2.imshow("capture", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
camera.release()
cv2.destroyAllWindows() 
 
