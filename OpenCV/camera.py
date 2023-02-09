# import the necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
from imutils.video import VideoStream #/usr/local/lib/python2.7/dist-packages/i$
import cv2
import urllib
import numpy as np
import os
import threading
import datetime
import time
import socket
import select
import sys


scale_factor = 1.1
counter = 0
#shotCount = 0
#shootThreshold = 5

neighbours_F = 0
minSize_F = (48,48)
maxSize_F = (52,52)

neighbours_L = 2
minSize_L = (48,48)
maxSize_L = (52,52)

neighbours_R = 2
minSize_R = (47,47)
maxSize_R = (52,52)

cycleTime = 30
startTime = 8
EndTime = 19
birdF_cascade = cv2.CascadeClassifier('Haar/BF_cascade.xml')
birdR_cascade = cv2.CascadeClassifier('Haar/BR19_cascade.xml') #
birdL_cascade = cv2.CascadeClassifier('Haar/BL19_cascade.xml') #



OkToShoot = 0
minimumShoot = 5
totalShots = 0


#screenRes =(1088,864)
screenRes =(912,672)

class VideoCamera(object):
    def __init__(self):
    ## self.vs = VideoStream(usePiCamera=1).start()
        self.vs = VideoStream(usePiCamera=1, resolution=(screenRes)).start()
        time.sleep(2.0)

    ## self.video = cv2.VideoCapture(0)

    def __del__(self):
        self.vs.stop()

    def get_frame(self):
        global scale_factor
        global neighbours
        global minSize
        global maxSize

        # global birdFrontPos
        # global birdLeftPos
        # global birdRightPos
        # global OkToShoot
        global neighbours_F
        global minSize_F
        global maxSize_F

        global neighbours_L
        global minSize_L
        global maxSize_L

        global neighbours_R
        global minSize_R
        global maxSize_R


        birdFrontPos = []
        birdLeftPos = []
        birdRightPos = []

        try:
            frame = self.vs.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            roi = gray[240:620, 180:660]

            mask2 = np.zeros(roi.shape, dtype=np.uint8)
            roi_corners = np.array([[(320,45),(480,40),(445,150),(190,150)]], dtype=np.int32)
            ignore_mask_color = (255,)
            cv2.fillPoly(mask2, roi_corners, ignore_mask_color)
            masked_image2 = cv2.bitwise_and(roi, mask2)
            cv2.polylines(roi, [roi_corners], True, (255,255,255), 1)

            font = cv2.FONT_HERSHEY_SIMPLEX

            birdF = birdF_cascade.detectMultiScale(masked_image2,scale_factor,neighbours_F,0,minSize_R,maxSize_R)
            for (x,y,w,h) in birdF:
                #cv2.rectangle(gray,(x,y),(x+w,y+h),(255,255,255),2)
                center = (x,y) #bird Location
                #print "BL: "+ str(center)
                birdFrontPos.append(center)
            if len(birdFrontPos)> 25:
                ListF = [[x,birdFrontPos.count(x)] for x in set(birdFrontPos)]
                if 14 <= ListF[0][1] <= 16:
                    print "BF: "+ str(ListF[0][0]) +":" + str(ListF[0][1])
                    cv2.rectangle(roi,(ListF[0][0]),(ListF[0][0][0]+50,ListF[0][0][1]+50),(255,255,255),2)
                    cv2.putText(roi,'[B-F]',(ListF[0][0][0],ListF[0][0][1]-1), font, 0.4, (255,255,255), 1, cv2.LINE_AA)
                    #OkToShoot += 1
                #birdFrontPos = []


            birdL = birdL_cascade.detectMultiScale(masked_image2,scale_factor,neighbours_L,0,minSize_L,maxSize_L)
            for (x,y,w,h) in birdL:
                #cv2.rectangle(gray,(x,y),(x+w,y+h),(255,255,255),2)
                center = (x,y) #bird Location
                #print "BL: "+ str(center)
                birdLeftPos.append(center)

            if len(birdLeftPos)> 200:
                ListL = [[x,birdLeftPos.count(x)] for x in set(birdLeftPos)]
                if 1 <= ListL[0][1] <= 2:
                    print "BL: "+ str(ListL[0][0]) +":" + str(ListL[0][1])
                    cv2.rectangle(roi,(ListL[0][0]),(ListL[0][0][0]+50,ListL[0][0][1]+50),(255,255,255),2)
                    cv2.putText(roi,'[B-L]',(ListL[0][0][0],ListL[0][0][1]-1), font, 0.4, (255,255,255), 1, cv2.LINE_AA)
                    #OkToShoot += 1
                #birdLeftPos = []


            birdR = birdR_cascade.detectMultiScale(masked_image2,scale_factor,neighbours_R,0,minSize_R,maxSize_R)
            for (x,y,w,h) in birdR:
                #cv2.rectangle(gray,(x,y),(x+w,y+h),(255,255,255),2)
                center = (x,y) #bird Location
                #print "BR: "+ str(center)
                birdRightPos.append(center)

            if len(birdRightPos)> 200:
                ListR = [[x,birdRightPos.count(x)] for x in set(birdRightPos)]
                if 3 <= ListR[0][1] <= 4:
                    print "BR: "+ str(ListR[0][0]) +":" + str(ListR[0][1])
                    cv2.rectangle(roi,(ListR[0][0]),(ListR[0][0][0]+50,ListR[0][0][1]+50),(255,255,255),2)
                    cv2.putText(roi,'[B-R]',(ListR[0][0][0],ListR[0][0][1]-1), font, 0.4, (255,255,255), 1, cv2.LINE_AA)
                    #OkToShoot += 1
                #birdRightPos = []


            ret, jpeg = cv2.imencode('.jpg',roi)
            return (jpeg.tobytes(),birdFrontPos,birdLeftPos,birdRightPos)
        except:
            return ""




