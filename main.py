#!/usr/bin/env python
trackImage = ['blackcrack.png' , 'blackstar.png' ,'redheart.png', 'green', 'red'] 
a = 4
import cv2
import numpy as np
import RPi.GPIO as GPIO
import time
import os
import motor
from opencv_wrapper import *

import serial

ser = serial.Serial('/dev/rfcomm0', 9600,timeout=0)
data = "nodetect\r\n"


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

os.system('sudo modprobe bcm2835-v4l2')
video_capture = cv2.VideoCapture(0)
video_capture.set(cv2.CAP_PROP_FPS,10)
video_capture.set(cv2.CAP_PROP_FRAME_WIDTH ,320)
video_capture.set(cv2.CAP_PROP_FRAME_HEIGHT,240)


methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
            'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']





print(trackImage[a])
lower_blue = np.array([150, 50, 0]) #빨간색을 검출하기위한 최소 hsv
upper_blue = np.array([220, 255, 255])#최대 hsv
while(True):
    _, img = video_capture.read()

    if a  < 3:
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        template = cv2.imread(trackImage[a],0)
        w, h = template.shape[::-1]
        res = cv2temp(trackImage,cv2.TM_SQDIFF ,img_gray, template)

        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        top_left = min_loc
        print(min_val)
        bottom_right = (top_left[0] + w, top_left[1] + h)
        cv2.rectangle(img,top_left, bottom_right, 255, 2)
        cx,cy = top_left[0] + w /2, top_left[1]+h/2
        if min_val < 12000000:
            bottom_right = (top_left[0] + w, top_left[1] + h)
            cv2.rectangle(img,top_left, bottom_right, (0,255,0), 2)
            cx,cy = top_left[0] + w /2, top_left[1]+h/2
            if cx < 110:
                print('right') 
                motor.left()
            elif cx > 210:
                print('left')
                motor.right()
            elif cy < 200:
                print ('go')
                motor.go()
            else:
                motor.stop()
                print ('stop')
        else:
            ser.write(data.encode('utf-8'))
            print ('nodect')
            motor.stop()
            cv2.rectangle(img,top_left, bottom_right, (255,0,0), 2)
        cv2.imwrite('pic.jpg',img)
        cv2.imshow('pic.jpg',img)
        cv2.waitKey(1)
    else:
        lower_blue = np.array([150, 50, 0]) #빨간색을 검출하기위한 최소 hsv
        upper_blue = np.array([220, 255, 255])#최대 hsv
        if a == 3:
            lower_blue = np.array([50, 150, 150]) #빨간색을 검출하기위한 최소 hsv
            upper_blue = np.array([70, 255, 255])#최대 hsv

        hsv= cv2.cvtColor(img, cv2.COLOR_BGR2HSV) #1개 는 hsv로 변경
        mask = cv2.inRange(hsv, lower_blue, upper_blue) #마스킹 씌움
        res = cv2and(img,mask,150,50,220,50,70,np.uint8 , np.uint32)  #결과값 
        contours, hierarchy = cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE) #윤곽선 정보얻음
        if len(contours) != 0:
            areas = [cv2.contourArea(c) for c in contours] 
            max_index = np.argmax(areas) 
            cnt=contours[max_index]
            x,y,w,h = cv2.boundingRect(cnt)
            cx =x + w/2
            cy =y + h/2
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2) # 가장큰곳에 사각형을 그림
            print(cv2.contourArea(contours[max_index]))
            if cv2.contourArea(contours[max_index]) > 200 :
                if cx < 110:
                    motor.left()
                    print('right')
                elif cx > 210:
                    motor.right()
                    print('left')
                elif cy < 200:
                    motor.go()
                    print ('go')
            else:
                motor.stop()
                ser.write(data.encode('utf-8'))
                print ('stop')
        cv2.imwrite('pic.jpg',img)
        cv2.imshow('pic.jpg',img)
        cv2.waitKey(1)


cv2.destroyAllWindows()
