from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort, Response
import os
from subprocess import call
#from camera import VideoCamera

# import the necessary packages
try:
    from picamera.array import PiRGBArray
    from picamera import PiCamera
    from imutils.video import VideoStream #/usr/local/lib/python2.7/dist-packages/i$
    os = "Pi"
except:
    print("<Could not load picamera>")
    os = "Mac"
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


scale_factor = 3
# counter = 0
# shotCount = 0
# shootThreshold = 5
#
neighbours_F = 6
minSize_F = (30,30)
maxSize_F = (70,70)

birdF_cascade = cv2.CascadeClassifier('Haar/12mm_cascade1.xml')

cycleTime = 10
startTime = 8
EndTime = 19



OkToShoot = 0
minimumShoot = 2
totalShots = 0


#screenRes =(1088,864)
screenRes =(912,672)


IPaddress = ""
Port = 4000
UserList = []
UsersFile = "setup/Users.txt"
FaildLogins = []

Videoutput = ""
pastJPG = ""

birdFrontPos = []
birdLeftPos = []
birdRightPos = []

class LanIp():

    def run(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8",80))
        IP = (s.getsockname()[0])
        s.close()
        return IP

class loadUsers():

    def __init__(self):
        global UsersFile
        global UserList
        #User:Password
        try:

            f1 = open(UsersFile,'r')
            text = str(f1.read())
            f1.close()

            StartInd = text.find("[") +1
            StopInd = text.find("]")
            text =  str(text[StartInd:StopInd])

            text = text.split(',')
            for x in enumerate(text):
                #print x[1]
                Xinfo = str(x[1])
                try:
                    Xinfo = Xinfo.replace(" ", "")
                    Xinfo = Xinfo.replace("\'", "")
                    Xinfo = Xinfo.replace("\"", "")
                    Xinfo = Xinfo.replace("[", "")
                    Xinfo = Xinfo.replace("]", "")
                    #Xinfo = Xinfo.upper()

                    if (Xinfo== ""):
                        break

                    if (len(Xinfo) <0):
                        break
                    else:
                        UserList.append(Xinfo)

                except:
                    pass
        except:
            print ("<Users.txt file not found>")
            print ("<Creating Users.txt with default user credentials>")
            f1 = open(UsersFile,'w')
            f1.write("<USERS>")
            f1.close()

class SaveUsers():

    def __init__(self):
        global UsersFile
        global UserList

        #User:Password
        print ("<SaveSettings_Pwds>")

        if (not os.path.exists(UsersFile)):
            print ("<Pwds File does not exist>")
            f1 = open(UsersFile,'w')
            f1.write("<USERS>")
            f1.close()

        try:
            f1 = open(UsersFile,'w')
            try:
                PwdsString = ""
                for x in enumerate(UserList):
                    if x[0] != (len(UserList)-1):
                        PwdsString += "\'" + str(x[1]) + "\',"
                    else:
                        PwdsString += "\'" + str(x[1]) + "\'"
                saveString = "<USERS>[" + PwdsString +"]"
                f1.write(saveString)
                print ("<Users File Updated>")
            except:
                print ("Error in saving- Users File could not be updated")

            f1.close()

        except:
            print ("*<Error- ["+ str(UsersFile) + "] not found, Please create>*")

class runcamera(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        print("Camera Online")

        def gen(camera):
            global Videoutput
            global pastJPG

            global birdFrontPos
            global birdLeftPos
            global birdRightPos

            while True:
                try:
                    #Videoutput,birdFrontPos,birdLeftPos,birdRightPos = camera.get_frame()
                    Videoutput = camera.get_frame()
                    pastJPG = Videoutput
                except:
                    try:
                        Videoutput = pastJPG
                    except:
                        Videoutput = ""


        gen(VideoCamera())

class VideoCamera(object):

    def __init__(self):
        global screenRes
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

        global birdFrontPos
        global birdLeftPos
        global birdRightPos
        global OkToShoot
        global neighbours_F
        global minSize_F
        global maxSize_F




        # try:
        #     frame = self.vs.read()
        #     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        #     #roi = gray[240:620, 180:660]
        #     ##roi = gray
        #     ##mask2 = np.zeros(roi.shape, dtype=np.uint8)
        #     ##roi_corners = np.array([[(320,45),(480,40),(445,150),(190,150)]], dtype=np.int32)
        #     ##ignore_mask_color = (255,)
        #     ##cv2.fillPoly(mask2, roi_corners, ignore_mask_color)
        #     ##masked_image2 = cv2.bitwise_and(roi, mask2)
        #     #cv2.polylines(roi, [roi_corners], True, (255,255,255), 1)
        #
        #     # font = cv2.FONT_HERSHEY_SIMPLEX
        #     birdF = birdF_cascade.detectMultiScale(gray,scale_factor,neighbours_F,0,minSize_F,maxSize_F)
        #     for (x,y,w,h) in birdF:
        #             cv2.rectangle(gray,(x,y),(x+w,y+h),(0,0,255),2) #red
        #
        #
        #     ret, jpeg = cv2.imencode('.jpg',gray)
        #     return(jpeg.tobytes())
        #
        # except:
        #     return ""
        try:
            frame = self.vs.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            font = cv2.FONT_HERSHEY_SIMPLEX
            mask2 = np.zeros(gray.shape, dtype=np.uint8)
            #roi_corners = np.array([[(200,100),(860,100),(650,670),(0,670),(450,670),(720,185),(500,185),(300,350),(0,350),(0,250)]], dtype=np.int32)
            #roi_corners = np.array([[(200,100),(860,100),(650,670),(0,670),(450,670),(720,185),(85,185)]], dtype=np.int32)
            roi_corners = np.array([[(430,100),(860,100),(650,670),(0,670),(450,670),(720,185),(385,185)]], dtype=np.int32)
            ignore_mask_color = (255,)
            cv2.fillPoly(mask2, roi_corners, ignore_mask_color)
            masked_image2 = cv2.bitwise_and(gray, mask2)
            #cv2.polylines(gray, [roi_corners], True, (255,255,255), 1)

            birdF = birdF_cascade.detectMultiScale(masked_image2,scale_factor,neighbours_F,0,minSize_F,maxSize_F)
            for (x,y,w,h) in birdF:
                cv2.rectangle(gray,(x,y),(x+w,y+h),(0,0,255),2) #red
                #cv2.putText(gray,' Bird',((x-2),(y-2)), font, 0.5, (75,75,75), 2, cv2.LINE_AA)
                OkToShoot += 1


            ret, jpeg = cv2.imencode('.jpg',gray)
            return(jpeg.tobytes())

        except:
            return ""
class sckClient():

    def __init__(self):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        SeagullToggle = "09ptJ0400A5^"
        SeagullPulse = "11pcJ0409990005001D^"
        IP_address = '144.130.106.233'
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


class parallel(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        global OkToShoot
        global minimumShoot
        global startTime
        global EndTime
        global cycleTime
        global totalShots
        while True:
            timestamp = datetime.datetime.now().time() # Throw away the date information
            Thour = timestamp.hour
            Tminute = timestamp.minute
            # print(Thour, Tminute)
            start = datetime.time(startTime)
            end = datetime.time(EndTime)
            #print (start <= timestamp <= end)
            if (start <= timestamp <= end):
                if OkToShoot > minimumShoot:
                    sckClient()
                    totalShots += 1
                    print ("***Fire: " + str(totalShots)+ "***")
                    OkToShoot = 0
                else:
                    OkToShoot = 0

            if Thour == 1 and Tminute == 0:
                print("Resetting")
                time.sleep(3)
                call (['sudo', 'reboot'])

            time.sleep(cycleTime)

class runFlask():
    def __init__(self):
        global Videoutput
        app = Flask(__name__)
        print("Flask Online")

        @app.route('/')
        def home():
            if not session.get('logged_in'):
                return render_template('login.html')
            else:

                # return Response(gen(VideoCamera()),
                #             mimetype='multipart/x-mixed-replace; boundary=frame'),

                return Response(gen(),
                            mimetype='multipart/x-mixed-replace; boundary=frame'),

        @app.route('/login', methods=['POST'])
        def do_admin_login():
            # if request.form['password'] == 'password' and request.form['username'] == 'admin':
            #     session['logged_in'] = True
            for credentials in UserList:
                if  request.form['username'] + ":" + request.form['password'] == credentials:
                    session['logged_in'] = True

            else:
                flash('wrong password!')
                FaildLogins.append(request.form['username'] + ":" + request.form['password'])

            return home()

        @app.route("/logout")
        def logout():
            session['logged_in'] = False
            return home()


        def gen():
            while True:
                try:
                    #frame = camera.get_frame()
                    frame = Videoutput
                except:
                    frame = ""
                yield (b'--frame\r\n'
                           b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

        # def gen(camera):
        #     while True:
        #         try:
        #             frame = camera.get_frame()
        #         except:
        #             frame = ""
        #         yield (b'--frame\r\n'
        #                    b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


        app.secret_key = os.urandom(12)
        app.run(debug=False,host=IPaddress, port=Port)



if __name__ == "__main__":
    check_ip = LanIp()
    IPaddress = str(check_ip.run())
    loadUsers()

    tP = threading.Thread(target=runcamera, args=())
    tP.daemon = True
    tP.start()

    timer = threading.Thread(target=parallel, args=())
    timer.daemon = True
    timer.start()

    runFlask()
    #runcamera()


