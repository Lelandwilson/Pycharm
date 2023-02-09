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

IPadd = ""

scale_factor = 3
# counter = 0
# shotCount = 0
# shootThreshold = 5
#
neighbours_F = 6
minSize_F = (30,30)
maxSize_F = (70,70)
#
# neighbours_L = 2
# minSize_L = (48,48)
# maxSize_L = (52,52)
#
# neighbours_R = 2
# minSize_R = (47,47)
# maxSize_R = (52,52)
#
# cycleTime = 30
# startTime = 8
# EndTime = 19

birdF_cascade = cv2.CascadeClassifier('12mm_cascade1.xml')
# birdF_cascade = cv2.CascadeClassifier('bird2-cascade.xml')

# cap = cv2.VideoCapture('BirdTester3.mp4')
cap = cv2.VideoCapture('12mm_mov/seagull2.mp4')

birdFrontPos = []
birdLeftPos = []
birdRightPos = []

OkToShoot = False


class sckClient():
    def __init__(self):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        SeagullToggle = "09ptJ0400A5^"
        SeagullPulse = "11pcJ0409990005001D^"
        IP_address = IPadd
        Port = 2101
        server.connect((IP_address, Port))
        print ("<NessLink_Init>")

        #while True:
        sockets_list = [sys.stdin, server]
        read_sockets,write_socket, error_socket = select.select(sockets_list,[],[])

        for socks in read_sockets:
            if socks == server:
                message = socks.recv(2048)
                if (len(message) > 0):
                    print (message)
                    try:
                        server.send(SeagullPulse)
                        print ("Message Successfully")
                    except:
                        print ("Could not complete request")

        server.close()


# class parallel(threading.Thread):
#     def __init__(self):
#         threading.Thread.__init__(self)
#         global OkToShoot
#         while True:
#             timestamp = datetime.datetime.now().time() # Throw away the date information
#             start = datetime.time(startTime)
#             end = datetime.time(EndTime)
#             #print (start <= timestamp <= end)
#             if (start <= timestamp <= end):
#                 if OkToShoot == True:
#                     print "<Fire>"
#                     sckClient()
#                     OkToShoot = False
#
#             time.sleep(cycleTime)
#
#
#
# timer = threading.Thread(target=parallel, args=())
# timer.daemon = True
# timer.start()


while True:
    # global scale_factor
    # global neighbours
    # global minSize
    # global maxSize
    # global OkToShoot
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    font = cv2.FONT_HERSHEY_SIMPLEX
    ##mask2 = np.zeros(gray.shape, dtype=np.uint8)
    ##roi_corners = np.array([[(320,45),(480,40),(445,150),(190,150)]], dtype=np.int32)
    ##ignore_mask_color = (255,)
    ##cv2.fillPoly(mask2, roi_corners, ignore_mask_color)
    ##masked_image2 = cv2.bitwise_and(gray, mask2)
    ##cv2.polylines(gray, [roi_corners], True, (255,255,255), 1)

    birdF = birdF_cascade.detectMultiScale(gray,scale_factor,neighbours_F,0,minSize_F,maxSize_F)
    for (x,y,w,h) in birdF:
            cv2.rectangle(gray,(x,y),(x+w,y+h),(0,0,255),2) #red
            cv2.putText(gray,' Bird',((x-2),(y-2)), font, 0.5, (75,75,75), 2, cv2.LINE_AA)
    #     #cv2.rectangle(gray,(x,y),(x+w,y+h),(255,255,255),2)
    #     center = (x,y) #bird Location
    #     #print "BL: "+ str(center)
    #     birdFrontPos.append(center)
    # if len(birdFrontPos)> 25:
    #     ListF = [[x,birdFrontPos.count(x)] for x in set(birdFrontPos)]
    #     if 14 <= ListF[0][1] <= 16:
    #         print "BF: "+ str(ListF[0][0]) +":" + str(ListF[0][1])
    #         cv2.rectangle(gray,(ListF[0][0]),(ListF[0][0][0]+50,ListF[0][0][1]+50),(255,255,255),2)
    #         cv2.putText(gray,'[B-F]',(ListF[0][0][0],ListF[0][0][1]-1), font, 0.4, (255,255,255), 1, cv2.LINE_AA)
    #         OkToShoot = True
    #     birdFrontPos = []


    cv2.imshow('img',gray)


    key = cv2.waitKey(1)#pauses for 3 seconds before fetching next image
    if key == 27:#if ESC is pressed, exit loop
        cv2.destroyAllWindows()
        break


