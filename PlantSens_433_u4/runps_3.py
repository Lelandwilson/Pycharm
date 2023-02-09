#--------------Imports--------------------#
import socket
import http.server
import urllib.request, urllib.error, urllib.parse
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import http.server, http.server
import ssl
import matplotlib
matplotlib.use("TkAgg")
import numpy as np
from serial import *
from tkinter import *
from PIL import ImageTk, Image
import time
import json
import os
import glob
import re
from sys import platform as _platform
from PIL import ImageFont
from PIL import ImageDraw
import threading
import csv
import string
import calendar
from datetime import datetime
import textwrap
import itertools

import sys
import ssl
from SimpleWebSocketServer import WebSocket, SimpleWebSocketServer, SimpleSSLWebSocketServer
from optparse import OptionParser
from numpy import *
import ast
#-----------------------------------------#
#----------------File Paths---------------#
linuxSerialport ="/dev/ttyAMA0"
linuxSerialport2 ="/dev/ttyACM0"
winSerialport = "com1"

linuxFileloc ="/home/pi/psens/Pics/"
macFileloc = "Pics/"
winFileloc = "C:/"

linuxHomeloc = "/home/pi/psens/"
macHomeloc =""

linuxFont = "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"
macFont = "Verdana"
#-----------------------------------------#
#------------------Files------------------#
CSV1File = 'PastDay.csv'  ##Collects on the hour for 24 hours
CSV2File = 'PastWeek.csv' ##Collects on the 7th day for past 7 days
CSV3File = 'PastMonth.csv' ##Collects on the 30th day for past 30 days
CSV4File = 'PastYear.csv' ##Collects on the 256 day for past 256 days

LuxFile = 'LuxGraphdata.txt'  #Graphing data for website
TempFile = 'TempGraphdata.txt'  #Graphing data for website
HumFile = 'HumGraphdata.txt'    #Graphing data for website
SmstFile = 'SmstGraphdata.txt'  #Graphing data for website

Gstreamfile = "datastream.txt"
Ggraphfile = "graphdata.txt"

weatherfile1 = "weatherdata1.txt"
weatherfile2 = "weatherdata2.txt"
weatherfile3 = "weatherdata3.txt"

datefile = "Timestamp.txt"

settingsFile = "Settings.txt"

#-----------------------------------------#
#-----------Settings page variables-------#
Debug = False
WebserverPort = 8888
StreamPort = 8889
ProbeList = ["AAA1","AAA2","AAA3","AAA4"]

RelayID = "RRR1"
RelayNames = ["Relay 1","Relay 2","Relay 3","Relay 4"]

RestartDelay = 5
TempOffset = 1
HumOffset = 1
#-----------------------------------------#
#-----------Place holder variables--------#
DebugText = ""
SensorCallText = ""
GFont = ""
Ghomeloc = ""
Gfileloc = ""

serBuffer = ""
relayMSG= ""

threads = []
BKGimg = [None,None,None,None,None,None,None,None,None,None]  #Page background list

GID = [0,1,2,3,4,5,6,7,8,10]
GTemp = [0,1,2,3,4,5,6,7,8,10]
GHum = [0,1,2,3,4,5,6,7,8,10]
GLux = [0,1,2,3,4,5,6,7,8,10]
GSMst = [0,1,2,3,4,5,6,7,8,10]
GResp = [0,1,2,3,4,5,6,7,8,10]
GBat = [0,1,2,3,4,5,6,7,8,10]
GSig = [0,1,2,3,4,5,6,7,8,10]



PlistIndex = 0
cnt0 = 0
cnt1 = 0
CycleCount = 180

StList = [0,0,0,0,0,0,0,0,0,0]

hourIteration = 0
dayIteration = 0
dayIteration2 = 0
weekIteration = 0
weekIteration2 = 0
monthIteration = 0
monthIteration2 = 0
pageNo = 0
Relays = ["OFF","OFF","OFF","OFF"]   #relay states

Boolchecktime = False


StatusLock = threading.Lock()
No_cycles = len(ProbeList) +1

defaultWebserverPort = 8888
defaultStreamPort = 8889
defaultTempOffset = 0
defaultHumOffset = 0
defaultProbeList = ["AAA1","AAA2","AAA3","AAA4"]
defaultRelayID = "RRR1"
defaultRelayNames = ["Relay 1","Relay 2","Relay 3","Relay 4"]
defaultCycleCount = 150

SetupFlag = False
internetConnection = False
WANip = ""
LANip = ""
#-----------------------______________________----------------------------#


#---------------------Sensors Page-----------------------#
class GUI(Tk):

    def __init__(self, *args, **kwargs):

        Tk.__init__(self, *args, **kwargs)
        Tk.wm_title(self, "Plant Sensor Interface")

        print( "Progam Initiated")
        time.sleep(0)

        # -------------------Load settings from file--------------#
        try:
            Loadsetings()

        except:
            print( "Failed to load setting from file")



        if _platform == "linux" or _platform == "linux2":
            font = ImageFont.truetype(linuxFont, 22)
            #label = Label(canvas, text="", font=(linuxFont, 12))
            imageAddress = linuxFileloc
        else:
            #label = Label(canvas, text="", font=(macFont, 12))
            imageAddress = macFileloc
            font = ImageFont.truetype(macFont, 22)


        BKGimg[0] = Image.open(imageAddress + "LayoutXLoading.png")#.convert("RGBA")
        draw = ImageDraw.Draw(BKGimg[0])
        draw.text((32, 150), "Loading...",(250,250,250),font=font)#(10,10,200) Blue
        BKGimg[0].save(imageAddress + 'BKG0.png')

        BKGimg[0] = ImageTk.PhotoImage(Image.open(imageAddress + "BKG0.png"))


        canvas = Canvas(self,width=480,height=320)
        canvas.config(highlightthickness=0,bd=0, highlightcolor='black', highlightbackground='black', background='black')
        canvas.pack()
        imagesprite = canvas.create_image(240,160,image=BKGimg[0])

        #-------------------Create Home Screen--------------#
        #RUN = SerialThread(canvas,imagesprite)
        tX = threading.Thread(target =SerialThread, args=(canvas,imagesprite,))
        tX.daemon = True
        tX.start()


        self.bind("<Escape>", lambda e: e.widget.destroy())
        def click(event):
            global pageNo
            #print( pageNo

            if (pageNo == 0):
                #print( "Link to page 1"  #-------------Weather info---------------#
                for child in canvas.winfo_children():
                    child.destroy()
                Page1(imageAddress,canvas,imagesprite)
                pageNo = 1

                return

            if (pageNo == 1):
                #print( "Link to page 2" #-------------Relays---------------#
                #for child in canvas.winfo_children():
                #    child.destroy()
                Page2(imageAddress,canvas,imagesprite) #New background loaded
                pageNo = 2

                return

            if (pageNo == 2):
                #print( "Link to page 3" #-------------Settings---------------#
                pageNo = 3
                for child in canvas.winfo_children():
                    child.destroy()

                Page3(imageAddress,canvas,imagesprite) #New background loaded

                return

            if (pageNo == 3):
                #print( "Link to page 0" #-------------Homepage---------------#
                for child in canvas.winfo_children():
                    child.destroy()
                Page4(imageAddress,canvas,imagesprite) #New background loaded
                pageNo = 4

                return

            if (pageNo == 4):
                #print( "Link to page 0" #-------------Homepage---------------#
                for child in canvas.winfo_children():
                    child.destroy()
                Page5(imageAddress,canvas,imagesprite) #New background loaded
                pageNo = 5

                return

            if (pageNo == 5):
                #print( "Link to page 0" #-------------Homepage---------------#
                for child in canvas.winfo_children():
                    child.destroy()
                Page6(imageAddress,canvas,imagesprite) #New background loaded
                pageNo = 6

                return

            if (pageNo == 6):
                #print( "Link to page 0" #-------------Homepage---------------#
                for child in canvas.winfo_children():
                    child.destroy()
                canvas.itemconfig(imagesprite,image = BKGimg[0]) #New background loaded
                pageNo = 0

                return





        canvas.bind("<Button-1>", click)

#---------------------Weather Page-----------------------#
class Page1(): #----------Weather data page-----------#
    def __init__(self,imageAddress,canvas,imagesprite):
        global Ghomeloc
        global weatherfile1
        global weatherfile2
        page = 1

        if _platform == "linux" or _platform == "linux2":
            font1 = ImageFont.truetype(linuxFont, 18)
            font2 = ImageFont.truetype(linuxFont, 12)
            #label = Label(self, text="", font=(linuxFont, 12))
            imageAddress = linuxFileloc
        else:
            #label = Label(self, text="", font=(macFont, 12))
            imageAddress = macFileloc
            font1 = ImageFont.truetype(macFont, 18)
            font2 = ImageFont.truetype(macFont, 12)

        fAddress1 = Ghomeloc + weatherfile1
        fAddress2 = Ghomeloc + weatherfile2

        file = open(fAddress1, 'r')
        data1 = file.read()
        file.close()

        file = open(fAddress2, 'r')
        data2 = file.read().replace('.', '.\n')
        file.close()

        #print( data2)
        data2= textwrap.fill(data2, 65)
        #print( data2)



        BKGimg[page] = Image.open(imageAddress + "LayoutXLoading.png")#.convert("RGBA")
        draw = ImageDraw.Draw(BKGimg[page])
        draw.text((10, 70), "Weather details:" ,(250,250,250),font=font1)#(10,10,200) Blue
        draw.text((10, 90), str(data1) + "\n\n" + str(data2) ,(250,250,250),font=font2)#(10,10,200) Blue

        BKGimg[page].save(imageAddress + 'BKG'+ str(page) +'.png')

        BKGimg[page] = ImageTk.PhotoImage(Image.open(imageAddress + 'BKG'+ str(page) +'.png'))
        canvas.itemconfig(imagesprite,image = BKGimg[page]) #New background loaded

        try:
            QueryRelayStatus()
        except:
            print( "Relay status query failed")

#---------------------Relay Page-----------------------#
class Page2(): #----------Relay page-----------#
    def __init__(self,imageAddress,canvas,imagesprite):
        global Ghomeloc
        global Relays
        global RelayID
        global RelayNames

        page = 2

        if _platform == "linux" or _platform == "linux2":
            font1 = ImageFont.truetype(linuxFont, 18)
            font2 = ImageFont.truetype(linuxFont, 12)
            buttonfont = linuxFont
            #label = Label(canvas, text="", font=(linuxFont, 12))
            imageAddress = linuxFileloc
        else:
            #label = Label(canvas, text="", font=(macFont, 12))
            imageAddress = macFileloc
            font1 = ImageFont.truetype(macFont, 18)
            font2 = ImageFont.truetype(macFont, 12)
            buttonfont = macFont

        BKGimg[page] = Image.open(imageAddress + "LayoutXLoading.png")#.convert("RGBA")
        draw = ImageDraw.Draw(BKGimg[page])
        draw.text((10, 70), "Relays:" ,(250,250,250),font=font1)#(10,10,200) Blue
        draw.text((20, 100), "" ,(250,250,250),font=font2)#(10,10,200) Blue

        BKGimg[page].save(imageAddress + 'BKG'+ str(page) +'.png')


        BKGimg[page] = ImageTk.PhotoImage(Image.open(imageAddress + 'BKG'+ str(page) +'.png'))
        canvas.itemconfig(imagesprite,image = BKGimg[page]) #New background loaded

        #try:
        #    QueryRelayStatus()
        #except:
        #    print( "Relay status query failed")



        def but1(icycle0=itertools.cycle(["ON", "OFF"])):
            global relayMSG
            global Relays
            state0 = next(icycle0)
            button1['text'] = str(state0)
            if (str(state0) == "ON"):
                print(( RelayID + ": Relay 1 ON"))
                Relays[0] = "ON"
                relayMSG = RelayID + ": R1_ON"


            if (str(state0) == "OFF"):
                print(( RelayID + ": Relay 1 OFF"))
                Relays[0] = "OFF"
                relayMSG = RelayID + ": R1_OFF"


        def but2(icycle1=itertools.cycle(["ON", "OFF"])):
            global relayMSG
            global Relays
            state1 = next(icycle1)
            button2['text'] = str(state1)
            if (str(state1) == "ON"):
                print(( RelayID + ": Relay 2 ON"))
                Relays[1] = "ON"
                relayMSG = RelayID + ": R2_ON"

            if (str(state1) == "OFF"):
                print(( RelayID + ": Relay 2 OFF"))
                Relays[1] = "OFF"
                relayMSG = RelayID + ": R2_OFF"

        def but3(icycle2=itertools.cycle(["ON", "OFF"])):
            global relayMSG
            global Relays
            state2 = next(icycle2)
            button3['text'] = str(state2)
            if (str(state2) == "ON"):
                print(( RelayID + ": Relay 3 ON"))
                Relays[2] = "ON"
                relayMSG = RelayID + ": R3_ON"

            if (str(state2) == "OFF"):
                print(( RelayID + ": Relay 3 OFF"))
                Relays[2] = "OFF"
                relayMSG = RelayID + ": R3_OFF"

        def but4(icycle3=itertools.cycle(["ON", "OFF"])):
            global relayMSG
            global Relays
            state3 = next(icycle3)
            button4['text'] = str(state3)
            if (str(state3) == "ON"):
                print(( RelayID + ": Relay 4 ON"))
                Relays[3] = "ON"
                relayMSG = RelayID + ": R4_ON"

            if (str(state3) == "OFF"):
                print(( RelayID + ": Relay 4 OFF"))
                Relays[3] = "OFF"
                relayMSG = RelayID + ": R4_OFF"

        button1 = Button(canvas, text = Relays[0], command = but1, anchor = W)
        button1.configure(width = 10, activebackground = "#33B5E5", relief = FLAT,bd = 0,highlightbackground='#4fbdeb')
        button1_window = canvas.create_window(220, 100, anchor=NW, window=button1)

        button2 = Button(canvas, text = Relays[1], command = but2, anchor = W)
        button2.configure(width = 10, activebackground = "#33B5E5", relief = FLAT,bd = 0,highlightbackground='#4fbdeb')
        button2_window = canvas.create_window(220, 140, anchor=NW, window=button2)

        button3 = Button(canvas, text = Relays[2], command = but3, anchor = W)
        button3.configure(width = 10, activebackground = "#33B5E5", relief = FLAT,bd = 0,highlightbackground='#4fbdeb')
        button3_window = canvas.create_window(220, 180, anchor=NW, window=button3)

        button4 = Button(canvas, text = Relays[3], command = but4, anchor = W)
        button4.configure(width = 10, activebackground = "#33B5E5", relief = FLAT,bd = 0,highlightbackground='#4fbdeb')
        button4_window = canvas.create_window(220, 220, anchor=NW, window=button4)

        T0 = Text(canvas, height=1, width=8,background = "#4fbdeb",font = buttonfont,fg="white",bd=0,highlightbackground='#4fbdeb')
        T0.insert(END, RelayNames[0])
        T0_window = canvas.create_window(120, 100, anchor=NW, window=T0)

        T1 = Text(canvas, height=1, width=8,background = "#4fbdeb",font = buttonfont,fg="white",bd=0,highlightbackground='#4fbdeb')
        T1.insert(END, RelayNames[1])
        T1_window = canvas.create_window(120, 140, anchor=NW, window=T1)

        T2 = Text(canvas, height=1, width=8,background = "#4fbdeb",font = buttonfont,fg="white",bd=0,highlightbackground='#4fbdeb')
        T2.insert(END, RelayNames[2])
        T2_window = canvas.create_window(120, 180, anchor=NW, window=T2)

        T3 = Text(canvas, height=1, width=8,background = "#4fbdeb",font = buttonfont,fg="white",bd=0,highlightbackground='#4fbdeb')
        T3.insert(END, RelayNames[3])
        T3_window = canvas.create_window(120, 220, anchor=NW, window=T3)

#---------------------Settings Page-----------------------#
class Page3():
    def __init__(self,imageAddress,canvas,imagesprite):
        global Ghomeloc
        global settingsFile

        #-----------Settings page variables-------#
        global Debug #= False
        global WebserverPort #= 8888
        global StreamPort #= 8889
        global ProbeList #= ["AAA1","AAA2","AAA3","AAA4"]

        global RelayID #= "RRR1"
        global RelayNames #= ["Relay 1","Relay 2","Relay 3","Relay 4"]

        global RestartDelay #= 5
        global TempOffset #= 1
        global HumOffset #= 1
        global CycleCount
        #-----------------------------------------#

        page = 3

        if _platform == "linux" or _platform == "linux2":
            font1 = ImageFont.truetype(linuxFont, 18)
            font2 = ImageFont.truetype(linuxFont, 12)
            buttonfont = linuxFont
            textBoxfont = linuxFont, 10
            #label = Label(canvas, text="", font=(linuxFont, 12))
            imageAddress = linuxFileloc
        else:
            #label = Label(canvas, text="", font=(macFont, 12))
            imageAddress = macFileloc
            font1 = ImageFont.truetype(macFont, 18)
            font2 = ImageFont.truetype(macFont, 12)
            buttonfont = macFont
            textBoxfont = macFont, 10

        BKGimg[page] = Image.open(imageAddress + "LayoutXLoading.png")#.convert("RGBA")
        draw = ImageDraw.Draw(BKGimg[page])
        draw.text((10, 70), "Settings:" ,(250,250,250),font=font1)#(10,10,200) Blue
        #----------------Settings text------------------#
        draw.text((30, 100), "WebServer Port: " ,(250,250,250),font=font2)#(10,10,200) Blue
        draw.text((30, 130), "Stream Port: " ,(250,250,250),font=font2)#(10,10,200) Blue
        draw.text((30, 160), "Probes List: " ,(250,250,250),font=font2)#(10,10,200) Blue
        draw.text((30, 190), "Relay ID: " ,(250,250,250),font=font2)#(10,10,200) Blue
        draw.text((30, 220), "Relay Channels: " ,(250,250,250),font=font2)#(10,10,200) Blue
        draw.text((30, 250), "Temp Offset: " ,(250,250,250),font=font2)#(10,10,200) Blue
        draw.text((30, 280), "Hum Offset: " ,(250,250,250),font=font2)#(10,10,200) Blue

        draw.text((265, 100), "Cycle Delay: " ,(250,250,250),font=font2)#(10,10,200) Blue

        BKGimg[page].save(imageAddress + 'BKG'+ str(page) +'.png')


        BKGimg[page] = ImageTk.PhotoImage(Image.open(imageAddress + 'BKG'+ str(page) +'.png'))
        canvas.itemconfig(imagesprite,image = BKGimg[page]) #New background loaded

        #----------------Settings input fields-------------#
        #Web Port
        T0 = Entry(canvas, width=8,background = "#ffffff",font = textBoxfont,fg="#000000",bd=0,highlightbackground='#ffffff',highlightthickness=0)
        T0.insert(END, WebserverPort)
        T0_window = canvas.create_window(160, 100, anchor=NW, window=T0)

        #Stream Port
        T1 = Entry(canvas, width=8,background = "#ffffff",font = textBoxfont,fg="#000000",bd=0,highlightbackground='#ffffff',highlightthickness=0)
        T1.insert(END, StreamPort)
        T1_window = canvas.create_window(160, 130, anchor=NW, window=T1)

        #Probes List
        T2 = Entry(canvas, width=35,background = "#ffffff",font = textBoxfont,fg="#000000",bd=0,highlightbackground='#ffffff',highlightthickness=0)
        T2.insert(END, ProbeList)
        T2_window = canvas.create_window(160, 160, anchor=NW, window=T2)

        #Relay ID
        T3 = Entry(canvas, width=8,background = "#ffffff",font = textBoxfont,fg="#000000",bd=0,highlightbackground='#ffffff',highlightthickness=0)
        T3.insert(END, RelayID)
        T3_window = canvas.create_window(160, 190, anchor=NW, window=T3)

        #Relay Channels
        T4 = Entry(canvas, width=35,background = "#ffffff",font = textBoxfont,fg="#000000",bd=0,highlightbackground='#ffffff',highlightthickness=0)
        T4.insert(END, RelayNames)
        T4_window = canvas.create_window(160, 220, anchor=NW, window=T4)

        #Temp Offset
        T5 = Entry(canvas, width=8,background = "#ffffff",font = textBoxfont,fg="#000000",bd=0,highlightbackground='#ffffff',highlightthickness=0)
        T5.insert(END, TempOffset)
        T5_window = canvas.create_window(160, 250, anchor=NW, window=T5)

        #Hum Offset
        T6 = Entry(canvas, width=8,background = "#ffffff",font = textBoxfont,fg="#000000",bd=0,highlightbackground='#ffffff',highlightthickness=0)
        T6.insert(END, HumOffset)
        T6_window = canvas.create_window(160, 280, anchor=NW, window=T6)

        #Cycle Counter
        T7 = Entry(canvas, width=8,background = "#ffffff",font = textBoxfont,fg="#000000",bd=0,highlightbackground='#ffffff',highlightthickness=0)
        T7.insert(END, CycleCount)
        T7_window = canvas.create_window(350, 100, anchor=NW, window=T7)



        def SaveInfo():
            #-----------Settings page variables-------#
            global Debug #= False
            global WebserverPort #= 8888
            global StreamPort #= 8889
            global ProbeList #= ["AAA1","AAA2","AAA3","AAA4"]
            global RelayID #= "RRR1"
            global RelayNames #= ["Relay 1","Relay 2","Relay 3","Relay 4"]
            global RestartDelay #= 5
            global TempOffset #= 1
            global HumOffset #= 1

            global CycleCount
            #-----------------------------------------#
            global defaultWebserverPort #= 8888
            global defaultStreamPort #= 8889
            global defaultTempOffset #= 0
            global defaultHumOffset #= 0
            global defaultProbeList #= ["AAA1","AAA2","AAA3","AAA4"]
            global defaultRelayID #= "RRR1"
            global defaultRelayNames #= ["Relay 1","Relay 2","Relay 3","Relay 4"]

            global defaultCycleCount
            #-----------------------------------------#


            print( "Save Settings")
            print( (T0.get() + ", " + T1.get() + ", " + T2.get() + ", " + T3.get() + ", " + T4.get() + ", " + T5.get() + ", " + T6.get() + ", " + T7.get()))
            writestring1 ="""<WebserverPort>"""+ str(T0.get()) +"""
<StreamPort>"""+ str(T1.get()) +"""
<ProbeList>"""+ str(T2.get()) +"""
<RelayID>"""+ str(T3.get()) +"""
<RelayChannels>"""+ str(T4.get()) +"""
<TempOffset>"""+ str(T5.get()) +"""
<HumOffset>"""+ str(T6.get()) +"""
<CycleCount>"""+ str(T7.get()) +"""
"""
            #----------File For Live table----------#

            f1Address = Ghomeloc + settingsFile
            f1 = open(f1Address,'w')
            f1.write(writestring1)
            f1.close()

            #---------------Webserver port---------------#
            WebserverPortInput = T0.get()
            try:
                if (WebserverPortInput.isdigit()):
                    WebserverPortInput = int(re.search(r'\d+', WebserverPortInput).group())
                    if (WebserverPortInput >0) and (WebserverPortInput <65535):
                        WebserverPort = WebserverPortInput
                        print(( "WebserverPort: " + str(WebserverPort)))

                    else:
                        WebserverPort = defaultWebserverPort
                        print( "Error with Webport assignment: Invalid input")

                else:
                    WebserverPort = defaultWebserverPort
                    print( "Error with Webport assignment: Invalid input")

            except:
                WebserverPort = defaultWebserverPort
                print( "Error with Webport assignment: Invalid input")

            #---------------Streamserver port---------------#
            StreamPortInput = T1.get()
            try:
                if (StreamPortInput.isdigit()):
                    StreamPortInput = int(re.search(r'\d+', StreamPortInput).group())
                    if (StreamPortInput >0) and (StreamPortInput <65535):
                        StreamPort = StreamPortInput
                        print(( "StreamPort: " + str(StreamPort)))

                    else:
                        StreamPort = defaultStreamPort
                        print( "Error with Streamport assignment: Invalid input")

                else:
                    StreamPort = defaultStreamPort
                    print( "Error with Streamport assignment: Invalid input")

            except:
                StreamPort = defaultStreamPort
                print( "Error with Streamport assignment: Invalid input")

            #---------------Probe List---------------#
            ProbeListInput = T2.get()
            try:
                ProbeListInput = ProbeListInput.replace(" ", "")
                ProbeListInput = ProbeListInput.replace("\n", "")
                ProbeList = ast.literal_eval(ProbeListInput)
                print(( "ProbeList: " + str(ProbeList)))

            except:
                ProbeList = defaultProbeList
                print( "Error with ProbeList assignment: Invalid input")

            #---------------Relay ID---------------#
            RelayIDInput = T3.get()
            try:
                RelayIDInput = RelayIDInput.replace(" ", "")
                RelayIDInput = RelayIDInput.upper()

                if (len(RelayIDInput) <0):
                    RelayID = defaultRelayID
                    print( "Error with RelayID: Invalid input")
                else:
                    RelayID = RelayIDInput

            except:
                RelayID = defaultRelayID
                print( "Error with RelayID assignment: Invalid input")

            #---------------Relay Channels---------------#
            RelayChannelsInput = T4.get()
            try:
                RelayChannelsInput = RelayChannelsInput.replace(" ", "")
                RelayChannelsInput = RelayChannelsInput.replace("\n", "")
                RelayChannelsInput = ast.literal_eval(RelayChannelsInput)

                RelayNames = RelayChannelsInput
                print(( "RelayChannels: " + str(RelayNames)))

            except:
                RelayNames = defaultRelayNames
                print( "Error with RelayChannels assignment: Invalid input")


            #---------------Temp Offset---------------#
            TempOffsetInput  = T5.get()
            try:
                if (TempOffsetInput.isdigit()):
                    TempOffsetInput = int(re.search(r'\d+', TempOffsetInput).group())
                    if (TempOffsetInput >0) and (TempOffsetInput <10):
                        TempOffset = TempOffsetInput
                        print(( "TempOffset: " + str(TempOffset)))

                    else:
                        TempOffset = defaultTempOffset
                        print( "Error with TempOffset assignment: Invalid input")

                else:
                    TempOffset = defaultTempOffset
                    print( "Error with TempOffset assignment: Invalid input")

            except:
                TempOffset = defaultTempOffset
                print( "Error with TempOffset assignment: Invalid input")


            #---------------Hum Offset---------------#
            HumOffsetInout = T6.get()
            try:
                if (HumOffsetInout.isdigit()):
                    HumOffsetInout = int(re.search(r'\d+', HumOffsetInout).group())
                    if (HumOffsetInout >0) and (HumOffsetInout <10):
                        HumOffset = HumOffsetInout
                        print(( "HumOffset: " + str(HumOffset)))

                    else:
                        HumOffset = defaultHumOffset
                        print( "Error with HumOffset assignment: Invalid input")

                else:
                    HumOffset = defaultHumOffset
                    print( "Error with HumOffset assignment: Invalid input")
            except:
                HumOffset = defaultHumOffset
                print( "Error with HumOffset assignment: Invalid input")

            #---------------Cycle Counter---------------#
            CycleCountinput = T7.get()
            try:
                if (CycleCountinput.isdigit()):
                    CycleCountinput = int(re.search(r'\d+', CycleCountinput).group())
                    if (CycleCountinput >0) and (CycleCountinput <1000):
                        CycleCount = CycleCountinput
                        print(( "CycleCount: " + str(CycleCount)))

                    else:
                        CycleCount = defaultCycleCount
                        print( "Error with CycleCount assignment: Invalid input")

                else:
                    CycleCount = defaultCycleCount
                    print( "Error with CycleCount assignment: Invalid input")
            except:
                CycleCount = defaultCycleCount
                print( "Error with CycleCount assignment: Invalid input")





        button1 = Button(canvas, text = "Save", command = SaveInfo, anchor = W)
        button1.configure(width = 6, activebackground = "#33B5E5", relief = FLAT,bd = 0,highlightbackground='#4fbdeb')
        button1_window = canvas.create_window(395, 275, anchor=NW, window=button1)

#---------------------Console Page-----------------------#
class Page4():
    def __init__(self,imageAddress,canvas,imagesprite):
        global Ghomeloc
        global DebugText
        global SensorCallText
        page = 4

        if _platform == "linux" or _platform == "linux2":
            font1 = ImageFont.truetype(linuxFont, 18)
            font2 = ImageFont.truetype(linuxFont, 12)
            #label = Label(self, text="", font=(linuxFont, 12))
            imageAddress = linuxFileloc
            textBoxfont = linuxFont, 10
            textBoxheight = 11
            textboxWidth = 52
        else:
            #label = Label(self, text="", font=(macFont, 12))
            imageAddress = macFileloc
            font1 = ImageFont.truetype(macFont, 18)
            font2 = ImageFont.truetype(macFont, 12)
            textBoxfont = macFont, 10
            textBoxheight = 14
            textboxWidth = 60

        BKGimg[page] = Image.open(imageAddress + "LayoutXLoading.png")#.convert("RGBA")
        draw = ImageDraw.Draw(BKGimg[page])
        draw.text((10, 70), "Console:" ,(250,250,250),font=font1)#(10,10,200) Blue

        draw.text((320, 75), "Call to sensor:" ,(250,250,250),font=font2)#(10,10,200) Blue

        BKGimg[page].save(imageAddress + 'BKG'+ str(page) +'.png')

        BKGimg[page] = ImageTk.PhotoImage(Image.open(imageAddress + 'BKG'+ str(page) +'.png'))
        canvas.itemconfig(imagesprite,image = BKGimg[page]) #New background loaded

        TextString = ""
        TextString += DebugText
        PrevDebug = DebugText

        #----------------Console Text fields-------------#
        #Console Textbox
        T0 = Text(canvas,height= textBoxheight, width=textboxWidth,background = "#ffffff",font = textBoxfont,fg="#000000",bd=0,highlightbackground='#ffffff',highlightthickness=0)
        T0.insert(END, TextString)
        T0_window = canvas.create_window(30, 102, anchor=NW, window=T0)

        #Sesnor call Textbox
        T1 = Text(canvas,height= 1, width=5,background = "#ffffff",font = textBoxfont,fg="#000000",bd=0,highlightbackground='#ffffff',highlightthickness=0)
        T1.insert(END, SensorCallText)
        T1_window = canvas.create_window(415, 75, anchor=NW, window=T1)

        #----------------Refresh Textboxes-------------#
        def refreshText(T0, TextString, PrevDebug):
            global DebugText
            global SensorCallText

            #print( DebugText)
            #print( len(T0.get('1.0', 'end')))

            if (PrevDebug != DebugText):

                T0.see(END)
                TextString = DebugText
                T0.insert(END, TextString)
                PrevDebug = DebugText
                DebugText = ""

            else:
                pass

            T1.delete('1.0', 'end')
            T1.insert(END, SensorCallText)


            if (len(T0.get('1.0', 'end'))>=5000):
                T0.delete('1.0', 'end')


            T0.after(500,refreshText, T0, TextString,PrevDebug)



        refreshText(T0, TextString, PrevDebug)

        def ClearTB():

            T0.delete('1.0', 'end')


        #----------------Clear Butotn-------------#
        button1 = Button(canvas, text = "Clear", command = ClearTB, anchor = W)
        button1.configure(width = 6, activebackground = "#33B5E5", relief = FLAT,bd = 0,highlightbackground='#4fbdeb',highlightthickness=0)
        button1_window = canvas.create_window(380, 280, anchor=NW, window=button1)

#---------------------Schedule Page-----------------------#
class Page5():
    def __init__(self,imageAddress,canvas,imagesprite):
        global Ghomeloc
        page = 5

        if _platform == "linux" or _platform == "linux2":
            font1 = ImageFont.truetype(linuxFont, 18)
            font2 = ImageFont.truetype(linuxFont, 12)
            #label = Label(self, text="", font=(linuxFont, 12))
            imageAddress = linuxFileloc
        else:
            #label = Label(self, text="", font=(macFont, 12))
            imageAddress = macFileloc
            font1 = ImageFont.truetype(macFont, 18)
            font2 = ImageFont.truetype(macFont, 12)

        BKGimg[page] = Image.open(imageAddress + "LayoutXLoading.png")#.convert("RGBA")
        draw = ImageDraw.Draw(BKGimg[page])
        draw.text((10, 70), "Schedules:" ,(250,250,250),font=font1)#(10,10,200) Blue
        draw.text((20, 90), "Content" ,(250,250,250),font=font2)#(10,10,200) Blue

        BKGimg[page].save(imageAddress + 'BKG'+ str(page) +'.png')

        BKGimg[page] = ImageTk.PhotoImage(Image.open(imageAddress + 'BKG'+ str(page) +'.png'))
        canvas.itemconfig(imagesprite,image = BKGimg[page]) #New background loaded

#---------------------Data Log Page-----------------------#
class Page6():
    def __init__(self,imageAddress,canvas,imagesprite):
        global Ghomeloc
        page = 6

        if _platform == "linux" or _platform == "linux2":
            font1 = ImageFont.truetype(linuxFont, 18)
            font2 = ImageFont.truetype(linuxFont, 12)
            #label = Label(self, text="", font=(linuxFont, 12))
            imageAddress = linuxFileloc
            textBoxfont = linuxFont, 10
            textBoxheight = 11
            textboxWidth = 52
        else:
            #label = Label(self, text="", font=(macFont, 12))
            imageAddress = macFileloc
            font1 = ImageFont.truetype(macFont, 18)
            font2 = ImageFont.truetype(macFont, 12)
            textBoxfont = macFont, 10
            textBoxheight = 14
            textboxWidth = 60


        BKGimg[page] = Image.open(imageAddress + "LayoutXLoading.png")#.convert("RGBA")
        draw = ImageDraw.Draw(BKGimg[page])
        draw.text((10, 70), "Loged Data:" ,(250,250,250),font=font1)#(10,10,200) Blue
        draw.text((20, 90), "" ,(250,250,250),font=font2)#(10,10,200) Blue

        BKGimg[page].save(imageAddress + 'BKG'+ str(page) +'.png')

        BKGimg[page] = ImageTk.PhotoImage(Image.open(imageAddress + 'BKG'+ str(page) +'.png'))
        canvas.itemconfig(imagesprite,image = BKGimg[page]) #New background loaded

        TextString = ''
        def LoadLog():
            global CSV2File
            global Ghomeloc
            TextString = "Daily Data:\n\n"
            print( "Loading Log")
            f1Address = Ghomeloc + CSV2File
            f1 = open(f1Address,'r')
            #print( f1.read())
            TextString += str(f1.read())
            f1.close()

            T0.insert(END, TextString)

        #----------------Text fields-------------#
        #Textbox
        T0 = Text(canvas,height= textBoxheight, width=textboxWidth,background = "#ffffff",font = textBoxfont,fg="#000000",bd=0,highlightbackground='#ffffff',highlightthickness=0)
        #T0.insert(END, TextString)
        T0_window = canvas.create_window(30, 102, anchor=NW, window=T0)

        #----------------Load Butotn-------------#
        button1 = Button(canvas, text = "Load Log", command = LoadLog, anchor = W)
        button1.configure(width = 6, activebackground = "#33B5E5", relief = FLAT,bd = 0,highlightbackground='#4fbdeb',highlightthickness=0)
        button1_window = canvas.create_window(380, 280, anchor=NW, window=button1)


#---------------------Start Up Classes-----------------------#
class Setup():
    def __init__(self):
        global SetupFlag
        global RelayNames
        global internetConnection
        global WANip
        global LANip

        if (SetupFlag == False):
            print( "Run Setup Functions")

            QueryRelayStatus() #Check status of relays
            Active_internet = internet_Test()
            internetConnection = Active_internet.run() #Check for internet connection
            print(( "Internet Connection = " + str(internetConnection)))

            Check_Local = LanIP()
            LANipaddress = str(Check_Local.run())
            print(( "LAN IP Address: " + LANipaddress))

            Check = WanIPCheck() #Check for WAN IP Address
            WANip =  str(Check.runCheck())
            print(( "WAN IP Address: " + WANip))






            SetupFlag = True
        else:
            pass

class Loadsetings():
    def __init__(self):
        global Ghomeloc
        global settingsFile

        global Ghomeloc
        global settingsFile

        #-----------Settings page variables-------#
        global Debug #= False
        global WebserverPort #= 8888
        global StreamPort #= 8889
        global ProbeList #= ["AAA1","AAA2","AAA3","AAA4"]
        global RelayID #= "RRR1"
        global RelayNames #= ["Relay 1","Relay 2","Relay 3","Relay 4"]
        global RestartDelay #= 5
        global TempOffset #= 1
        global HumOffset #= 1

        global CycleCount #=150
        #-----------------------------------------#
        global defaultWebserverPort #= 8888
        global defaultStreamPort #= 8889
        global defaultTempOffset #= 0
        global defaultHumOffset #= 0
        global defaultProbeList #= ["AAA1","AAA2","AAA3","AAA4"]
        global defaultRelayID #= "RRR1"
        global defaultRelayNames #= ["Relay 1","Relay 2","Relay 3","Relay 4"]

        global defaultCycleCount #=150

        print( "Loading settings:")
        f1Address = Ghomeloc + settingsFile
        f1 = open(f1Address,'r')
        #print( f1.read())
        text = str(f1.read())
        f1.close()

        text = text.split('\n')
        for x in enumerate(text):
            #print( x[1]

            #---------------Webserver port---------------#
            if ("<WebserverPort>" in x[1]):
                try:
                    StartInd = x[1].find(">") +1
                    StopInd = len(x[1])
                    Xinfo =  str(x[1][StartInd:StopInd])

                    if (Xinfo.isdigit()):
                        Xinfo = int(re.search(r'\d+', Xinfo).group())
                        if (Xinfo >0) and (Xinfo <65535):
                            WebserverPort = Xinfo
                            print(( "WebserverPort: " + str(WebserverPort)))

                        else:
                            WebserverPort = defaultWebserverPort
                            print( "Error with Webport assignment: Invalid input")

                    else:
                        WebserverPort = defaultWebserverPort
                        print( "Error with Webport assignment: Invalid input")

                except:
                    WebserverPort = defaultWebserverPort
                    print( "Error with Webport assignment: Invalid input")



            #---------------Streamserver port---------------#
            elif ("<StreamPort>" in x[1]):
                try:
                    StartInd = x[1].find(">") +1
                    StopInd = len(x[1])
                    Xinfo =  str(x[1][StartInd:StopInd])

                    if (Xinfo.isdigit()):
                        Xinfo = int(re.search(r'\d+', Xinfo).group())
                        if (Xinfo >0) and (Xinfo <65535):
                            StreamPort = Xinfo
                            print(( "StreamPort: " + str(StreamPort)))

                        else:
                            StreamPort = defaultStreamPort
                            print( "Error with Streamport assignment: Invalid input")

                    else:
                        StreamPort = defaultStreamPort
                        print( "Error with Streamport assignment: Invalid input")

                except:
                    StreamPort = defaultStreamPort
                    print( "Error with Streamport assignment: Invalid input")


            #---------------Probe List---------------#
            elif ("<ProbeList>" in x[1]):
                try:
                    StartInd = x[1].find(">") +1
                    StopInd = len(x[1])
                    Xinfo =  str(x[1][StartInd:StopInd])
                    Xinfo = Xinfo.replace(" ", "")
                    Xinfo = Xinfo.replace("\n", "")
                    ProbeList = ast.literal_eval(Xinfo)
                    #print( "ProbeList: " + str(ProbeList)

                except:
                    ProbeList = defaultProbeList
                    print( "Error with ProbeList assignment: Invalid input")


            #---------------Relay ID---------------#
            elif ("<RelayID>" in x[1]):
                try:
                    StartInd = x[1].find(">") +1
                    StopInd = len(x[1])
                    Xinfo =  str(x[1][StartInd:StopInd])
                    Xinfo = Xinfo.replace(" ", "")
                    Xinfo = Xinfo.upper()

                    if (len(Xinfo) <0):
                        RelayID = defaultRelayID
                        print( "Error with RelayID: Invalid input")
                    else:
                        RelayID = Xinfo

                except:
                    RelayID = defaultRelayID
                    print( "Error with RelayID assignment: Invalid input")

            #---------------Relay Channels---------------#
            elif ("<RelayChannels>" in x[1]):
                try:
                    StartInd = x[1].find(">") +1
                    StopInd = len(x[1])
                    Xinfo =  str(x[1][StartInd:StopInd])
                    Xinfo = Xinfo.replace(" ", "")
                    Xinfo = Xinfo.replace("\n", "")
                    Xinfo = ast.literal_eval(Xinfo)

                    RelayNames = Xinfo
                    #print( "RelayChannels: " + str(RelayNames)

                except:
                    RelayNames = defaultRelayNames
                    print( "Error with RelayChannels assignment: Invalid input")


            #---------------Temp Offset---------------#
            elif ("<TempOffset>" in x[1]):
                try:
                    StartInd = x[1].find(">") +1
                    StopInd = len(x[1])
                    Xinfo =  str(x[1][StartInd:StopInd])

                    if (Xinfo.isdigit()):
                        Xinfo = int(re.search(r'\d+', Xinfo).group())
                        if (Xinfo >0) and (Xinfo <10):
                            TempOffset = Xinfo
                            #print( "TempOffset: " + str(TempOffset)

                        else:
                            TempOffset = defaultTempOffset
                            print( "Error with TempOffset assignment: Invalid input")

                    else:
                        TempOffset = defaultTempOffset
                        print( "Error with TempOffset assignment: Invalid input")

                except:
                    TempOffset = defaultTempOffset
                    print( "Error with TempOffset assignment: Invalid input")


            #---------------Hum Offset---------------#
            elif ("<HumOffset>" in x[1]):
                try:
                    StartInd = x[1].find(">") +1
                    StopInd = len(x[1])
                    Xinfo =  str(x[1][StartInd:StopInd])

                    if (Xinfo.isdigit()):
                        Xinfo = int(re.search(r'\d+', Xinfo).group())
                        if (Xinfo >0) and (Xinfo <10):
                            HumOffset = Xinfo
                            #print( "HumOffset: " + str(HumOffset)

                        else:
                            HumOffset = defaultHumOffset
                            print( "Error with HumOffset assignment: Invalid input")

                    else:
                        HumOffset = defaultHumOffset
                        print( "Error with HumOffset assignment: Invalid input")
                except:
                    HumOffset = defaultHumOffset
                    print( "Error with HumOffset assignment: Invalid input")

                            #---------------Cycle Count---------------#
            elif ("<CycleCount>" in x[1]):
                try:
                    StartInd = x[1].find(">") +1
                    StopInd = len(x[1])
                    Xinfo =  str(x[1][StartInd:StopInd])

                    if (Xinfo.isdigit()):
                        Xinfo = int(re.search(r'\d+', Xinfo).group())
                        if (Xinfo >0) and (Xinfo <1000):
                            CycleCount = Xinfo
                            #print( "HumOffset: " + str(HumOffset)

                        else:
                            CycleCount = defaultCycleCount
                            print( "Error with CycleCount assignment: Invalid input")

                    else:
                        CycleCount = defaultCycleCount
                        print( "Error with CycleCount assignment: Invalid input")
                except:
                    CycleCount = defaultCycleCount
                    print( "Error with CycleCount assignment: Invalid input")

        print( "____________")


#---------------------Serial Classes-----------------------#
class SerialThread(threading.Thread):
    def __init__(self,root,sprite):
        threading.Thread.__init__(self)
        def Program():
            global webServerActive
            global GFont
            global Ghomeloc
            global Gfileloc
            global DebugText


            if _platform == "linux" or _platform == "linux2":
                # linux
                #Locate Serial Port to use
                USBList1 = glob.glob('/dev/*')
                matching = [s for s in USBList1 if "ACM" in s]    #32u4
                serialPort = str(matching)
                serialPort = serialPort.strip("[]'")



                imageAddress = linuxFileloc
                fontFile = linuxFont
                #---------Global set----------#
                GFont = linuxFont
                Ghomeloc = linuxHomeloc
                Gfileloc = linuxFileloc



            elif _platform == "darwin":
                # OS X
                #Locate Serial Port to use
                USBList1 = glob.glob('/dev/tty.*')
                #print( USBList1)
                #/dev/tty.wchusbserial1420

                matching = [s for s in USBList1 if "14" in s]


                #matching = [s for s in USBList1 if "usbmodem" in s]
                #print( str(matching))
                serialPort = str(matching)
                serialPort = serialPort.strip("[]'")
                print(( "Connected to: " + serialPort))
                DebugText += "Connected to: " + serialPort
                DebugText += "\n"

                imageAddress = macFileloc
                #serialPort = macSerialport #'/dev/tty.linvor-DevB', 9600
                fontFile = macFont

                #---------Global set----------#
                GFont = macFont
                Ghomeloc = macHomeloc
                Gfileloc = macFileloc



            elif _platform == "win32":
                # Windows...
                imageAddress = winFileloc
                serialPort = winSerialport


            try:
                #### RUN SETUP ONCE #####
                Setup() 

                t1 = threading.Thread(target =ReadSerial, args=(serialPort,root,sprite,imageAddress,))
                t1.daemon = True
                t1.start()


                runWeb = threading.Thread(target =webserver, args=())
                #runWeb.daemon = True
                runWeb.start()


                runstream = threading.Thread(target =simpleServer, args=())
                #runstream.daemon = True
                runstream.start()



                try:
                    url1 = 'http://www.bom.gov.au/vic/forecasts/melbourne.shtml'
                    scrape1 = DynamicScrape()
                    data = scrape1.goScrape(url1,'div','class','forecast',"\n","\n",200)
                    saveWeatherdata(data)
                    webScrape()
                    print( "New weather data files added")
                    DebugText += "New weather data files added\n"


                except:
                    now = datetime.now()
                    timestring = now.strftime("%Y-%m-%d %H:%M")
                    print(( "Unable to create new weather data files at: " + str(timestring)))
                    DebugText += "Unable to create new weather data files at: " + str(timestring)
                    DebugText += "\n"




            except RuntimeError:
                print( "Error 1, RuntimeError")
                time.sleep(RestartDelay)
                #print( "Retry")
                Program() #### Reload program ####


            except OSError:
                print( "Error 2, OSError")
                time.sleep(RestartDelay)
                #print( "Retry")
                Program() #### Reload program ####

        Program()

class ReadSerial(threading.Thread):
    def __init__(self,serialPort,root,sprite,imageAddress):
        threading.Thread.__init__(self)

        pastconfig = None
        self.serBuffer = ""
        baudRate = 115200
        self.ser = Serial(serialPort , baudRate, timeout=0, writeTimeout=0) #ensure non-blocking

        def readSerial():
            global cnt0
            global ProbeList
            global PlistIndex
            global relayMSG

            global DebugText
            global CycleCount
            global SensorCallText


            cnt0 = cnt0 + 1

            if (cnt0 == CycleCount):

                if (relayMSG != ""):
                    self.ser.write(relayMSG)
                    print(( "Msg sent: " + str(relayMSG)))
                    relayMSG = ""
                    DebugText += "Msg sent: " + str(relayMSG)
                    DebugText += "\n"
                    time.sleep(2)


                self.ser.write(ProbeList[PlistIndex])
                #print( ProbeList[PlistIndex])
                ##DebugText += str(ProbeList[PlistIndex])
                ##DebugText += "\n"
                SensorCallText = str(ProbeList[PlistIndex])
                PlistIndex = PlistIndex + 1

                if (PlistIndex >= len(ProbeList)):
                    PlistIndex = 0

                cnt0 = 0



            while True:
                c = self.ser.read() # attempt to read a character from Serial

                if len(c) == 0:
                    break

                if c == '\r':
                    c = '' # don't want returns. chuck it
                if c == '\n':

                    #print( (self.serBuffer) )    ######print( SERIAL BUFFER
                    DebugText += self.serBuffer
                    DebugText += "\n"

                    readString(self.serBuffer,root,sprite,imageAddress)  ###<<<Run Readstring class>>>###
                    self.serBuffer =""
                    #NOTHING HAPPENS AFTER HERE#


                else:
                    self.serBuffer += c # add to the buffer

            root.after(10, readSerial) # check serial again soon
            #root.update_idletasks()






        root.after(1, readSerial) # check serial again soon
        #root.update_idletasks()

class updateScreen():
    def __init__(self):
        pass


    def returnCompare(self,serBuffer,List0,List1,List2,List3,List4,List5,List6,List7,List8,List9,imageAddress):

        global Debug
        global StatusLock

        global GID
        global GTemp
        global GHum
        global GLux
        global GSMst
        global GResp
        global GBat
        global GSig

        global No_cycles

        global Ghomeloc
        global Gstreamfile

        global GFont

        with StatusLock:
            #Sensor 1 List Values#
            try:
                GID[0] = List0[0]
                GTemp[0] = List0[1]
                GHum[0] = List0[2]
                GLux[0] = List0[3]
                GSMst[0] = List0[4]
                GBat[0] = List0[5]
                GSig[0] = List0[6]
            except:
                GID[0] = 0
                GTemp[0] = 0
                GHum[0] = 0
                GLux[0] = 0
                GSMst[0] = 0
                GBat[0] = 0
                GSig[0] = 0

            #Sensor 2 List Values#
            try:
                GID[1] = List1[0]
                GTemp[1] = List1[1]
                GHum[1] = List1[2]
                GLux[1] = List1[3]
                GSMst[1] = List1[4]
                GBat[1] = List1[5]
                GSig[1] = List1[6]
            except:
                GID[1] = 0
                GTemp[1] = 0
                GHum[1] = 0
                GLux[1] = 0
                GSMst[1] = 0
                GBat[1] = 0
                GSig[1] = 0


            #Sensor 3 List Values#
            try:
                GID[2] = List2[0]
                GTemp[2] = List2[1]
                GHum[2] = List2[2]
                GLux[2] = List2[3]
                GSMst[2] = List2[4]
                GBat[2] = List2[5]
                GSig[2] = List2[6]
            except:
                GID[2] = 0
                GTemp[2] = 0
                GHum[2] = 0
                GLux[2] = 0
                GSMst[2] = 0
                GBat[2] = 0
                GSig[2] = 0


            #Sensor 4 List Values#
            try:
                GID[3] = List3[0]
                GTemp[3] = List3[1]
                GHum[3] = List3[2]
                GLux[3] = List3[3]
                GSMst[3] = List3[4]
                GBat[3] = List3[5]
                GSig[3] = List3[6]
            except:
                GID[3] = 0
                GTemp[3] = 0
                GHum[3] = 0
                GLux[3] = 0
                GSMst[3] = 0
                GBat[3] = 0
                GSig[3] = 0

            #Sensor 5 List Values#
            try:
                GID[4] = List4[0]
                GTemp[4] = List4[1]
                GHum[4] = List4[2]
                GLux[4] = List4[3]
                GSMst[4] = List4[4]
                GBat[4] = List4[5]
                GSig[4] = List4[6]
            except:
                GID[4] = 0
                GTemp[4] = 0
                GHum[4] = 0
                GLux[4] = 0
                GSMst[4] = 0
                GBat[4] = 0
                GSig[4] = 0

            #Sensor 6 List Values#
            try:
                GID[5] = List5[0]
                GTemp[5] = List5[1]
                GHum[5] = List5[2]
                GLux[5] = List5[3]
                GSMst[5] = List5[4]
                GBat[5] = List5[5]
                GSig[5] = List5[6]
            except:
                GID[5] = 0
                GTemp[5] = 0
                GHum[5] = 0
                GLux[5] = 0
                GSMst[5] = 0
                GBat[5] = 0
                GSig[5] = 0

            #Sensor 7 List Values#
            try:
                GID[6] = List6[0]
                GTemp[6] = List6[1]
                GHum[6] = List6[2]
                GLux[6] = List6[3]
                GSMst[6] = List6[4]
                GBat[6] = List6[5]
                GSig[6] = List6[6]
            except:
                GID[6] = 0
                GTemp[6] = 0
                GHum[6] = 0
                GLux[6] = 0
                GSMst[6] = 0
                GBat[6] = 0
                GSig[6] = 0


            #Sensor 8 List Values#
            try:
                GID[7] = List7[0]
                GTemp[7] = List7[1]
                GHum[7] = List7[2]
                GLux[7] = List7[3]
                GSMst[7] = List7[4]
                GBat[7] = List7[5]
                GSig[7] = List7[6]
            except:
                GID[7] = 0
                GTemp[7] = 0
                GHum[7] = 0
                GLux[7] = 0
                GSMst[7] = 0
                GBat[7] = 0
                GSig[7] = 0

            #Sensor 9 List Values#
            try:
                GID[8] = List8[0]
                GTemp[8] = List8[1]
                GHum[8] = List8[2]
                GLux[8] = List8[3]
                GSMst[8] = List8[4]
                GBat[8] = List8[5]
                GSig[8] = List8[6]
            except:
                GID[8] = 0
                GTemp[8] = 0
                GHum[8] = 0
                GLux[8] = 0
                GSMst[8] = 0
                GBat[8] = 0
                GSig[8] = 0

            #Sensor 10 List Values#
            try:
                GID[9] = List9[0]
                GTemp[9] = List9[1]
                GHum[9] = List9[2]
                GLux[9] = List9[3]
                GSMst[9] = List9[4]
                GBat[9] = List9[5]
                GSig[9] = List9[6]
            except:
                GID[9] = 0
                GTemp[9] = 0
                GHum[9] = 0
                GLux[9] = 0
                GSMst[9] = 0
                GBat[9] = 0
                GSig[9] = 0


        #Respiration Calculation
        for x in enumerate(GLux):

            Rlux = GLux[x[0]]
            Rtemp = GTemp[x[0]]
            Rmoist = GSMst[x[0]]
            try:
                Rlux = float(Rlux) * .5
                Rtemp = float(Rtemp) * .2
                Rmoist = float(Rmoist) * .3
            except:
                #print( "Value error in Update screen: No float read")
                Rlux = 0
                Rtemp = 0
                Rmoist = 0

            GResp[x[0]] = int(Rlux+Rtemp+Rmoist)

            if (Rlux <=5):
                GResp[x[0]] = 0
            if (Rmoist <=1):
                GResp[x[0]] = 0







        #Load background image ready for editing#
        img = Image.open(imageAddress + "LayoutX.png")
        #img = Image.open(imageAddress + "layout_Readings.png")

        draw = ImageDraw.Draw(img)


        #Place text on image#
        if _platform == "linux" or _platform == "linux2":
            font = ImageFont.truetype(linuxFont, 16)
            debugfont = ImageFont.truetype(linuxFont, 12)

        else:
            font = ImageFont.truetype(macFont, 16)
            debugfont = ImageFont.truetype(macFont, 12)



        writestring1 = ""
        writestring2 = ""
        statsString = ""

        ColourX = ["00ff99","ffff00","ff6600","0099ff","ff3399","cc00ff","3333cc","339933","996633","993366","808080","000000","ccccff","ccffcc","ffffcc","ffcc99","ffcccc","ccffff","663300","993333"]

        for x in range  (0 , (No_cycles)):
        #Text line 1:
            if (GID[x] == "1"):   #And if i = 1 then:
                draw.text((20, 90),str(GID[x]),(255,255,255),font=font)        #ID (153,204,102)green
                draw.text((70, 90),str(GLux[x])+ "%",(254,241,95),font=font)   #LUX
                draw.text((135, 90),str(GTemp[x])+ "c",(191,103,16),font=font) #TEMP
                draw.text((190, 90),str(GHum[x])+ "%",(229,180,73),font=font) #HUMUDITY
                draw.text((250, 90),str(GSMst[x])+ "%",(204,153,204),font=font)#SOIL MOIST
                draw.text((310, 90),str(GResp[x])+ "%",(113,64,140),font=font) #RESPIRATION
                draw.text((370, 90),str(GSig[x])+ "%",(00,154,218),font=font)  #SIGNAL
                draw.text((425, 90),str(GBat[x])+ "%",(153,153,153),font=font) #BATTERY


        #Text line 2:
            if (GID[x] == "2"):
                draw.text((20, 115),str(GID[x]),(255,255,255),font=font)        #ID
                draw.text((70, 115),str(GLux[x])+ "%",(254,241,95),font=font)   #LUX
                draw.text((135, 115),str(GTemp[x])+ "c",(191,103,16),font=font) #TEMP
                draw.text((190, 115),str(GHum[x])+ "%",(229,180,73),font=font) #HUMUDITY
                draw.text((250, 115),str(GSMst[x])+ "%",(204,153,204),font=font)#SOIL MOIST
                draw.text((310, 115),str(GResp[x])+ "%",(113,64,140),font=font) #RESPIRATION
                draw.text((370, 115),str(GSig[x])+ "%",(00,154,218),font=font)  #SIGNAL
                draw.text((425, 115),str(GBat[x])+ "%",(153,153,153),font=font) #BATTERY


        #Text line 3:
            if (GID[x] == "3"):
                draw.text((20, 140),str(GID[x]),(255,255,255),font=font)        #ID
                draw.text((70, 140),str(GLux[x])+ "%",(254,241,95),font=font)   #LUX
                draw.text((135, 140),str(GTemp[x])+ "c",(191,103,16),font=font) #TEMP
                draw.text((190, 140),str(GHum[x])+ "%",(229,180,73),font=font) #HUMUDITY
                draw.text((250, 140),str(GSMst[x])+ "%",(204,153,204),font=font)#SOIL MOIST
                draw.text((310, 140),str(GResp[x])+ "%",(113,64,140),font=font) #RESPIRATION
                draw.text((370, 140),str(GSig[x])+ "%",(00,154,218),font=font)  #SIGNAL
                draw.text((425, 140),str(GBat[x])+ "%",(153,153,153),font=font) #BATTERY


        #Text line 4:
            if (GID[x] == "4"):
                draw.text((20, 165),str(GID[x]),(255,255,255),font=font)        #ID
                draw.text((70, 165),str(GLux[x])+ "%",(254,241,95),font=font)   #LUX
                draw.text((135, 165),str(GTemp[x])+ "c",(191,103,16),font=font) #TEMP
                draw.text((190, 165),str(GHum[x])+ "%",(229,180,73),font=font) #HUMUDITY
                draw.text((250, 165),str(GSMst[x])+ "%",(204,153,204),font=font)#SOIL MOIST
                draw.text((310, 165),str(GResp[x])+ "%",(113,64,140),font=font) #RESPIRATION
                draw.text((370, 165),str(GSig[x])+ "%",(00,154,218),font=font)  #SIGNAL
                draw.text((425, 165),str(GBat[x])+ "%",(153,153,153),font=font) #BATTERY



        #Text line 5:
            if (GID[x] == "5"):
                draw.text((20, 190),str(GID[x]),(255,255,255),font=font)        #ID
                draw.text((70, 190),str(GLux[x])+ "%",(254,241,95),font=font)   #LUX
                draw.text((135, 190),str(GTemp[x])+ "c",(191,103,16),font=font) #TEMP
                draw.text((190, 190),str(GHum[x])+ "%",(229,180,73),font=font) #HUMUDITY
                draw.text((250, 190),str(GSMst[x])+ "%",(204,153,204),font=font)#SOIL MOIST
                draw.text((310, 190),str(GResp[x])+ "%",(113,64,140),font=font) #RESPIRATION
                draw.text((370, 190),str(GSig[x])+ "%",(00,154,218),font=font)  #SIGNAL
                draw.text((425, 190),str(GBat[x])+ "%",(153,153,153),font=font) #BATTERY

        #Text line 6:
            if (GID[x] == "6"):
                draw.text((20, 225),str(GID[x]),(255,255,255),font=font)        #ID
                draw.text((70, 225),str(GLux[x])+ "%",(254,241,95),font=font)   #LUX
                draw.text((135, 225),str(GTemp[x])+ "c",(191,103,16),font=font) #TEMP
                draw.text((190, 225),str(GHum[x])+ "%",(229,180,73),font=font) #HUMUDITY
                draw.text((250, 225),str(GSMst[x])+ "%",(204,153,204),font=font)#SOIL MOIST
                draw.text((310, 225),str(GResp[x])+ "%",(113,64,140),font=font) #RESPIRATION
                draw.text((370, 225),str(GSig[x])+ "%",(00,154,218),font=font)  #SIGNAL
                draw.text((425, 225),str(GBat[x])+ "%",(153,153,153),font=font) #BATTERY

        #Text line 7:
            if (GID[x] == "7"):
                draw.text((20, 260),str(GID[x]),(255,255,255),font=font)        #ID
                draw.text((70, 260),str(GLux[x])+ "%",(254,241,95),font=font)   #LUX
                draw.text((135, 260),str(GTemp[x])+ "c",(191,103,16),font=font) #TEMP
                draw.text((190, 260),str(GHum[x])+ "%",(229,180,73),font=font) #HUMUDITY
                draw.text((250, 260),str(GSMst[x])+ "%",(204,153,204),font=font)#SOIL MOIST
                draw.text((310, 260),str(GResp[x])+ "%",(113,64,140),font=font) #RESPIRATION
                draw.text((370, 260),str(GSig[x])+ "%",(00,154,218),font=font)  #SIGNAL
                draw.text((425, 260),str(GBat[x])+ "%",(153,153,153),font=font) #BATTERY

        #Text line 8:
            if (GID[x] == "8"):
                draw.text((20, 295),str(GID[x]),(255,255,255),font=font)        #ID
                draw.text((70, 295),str(GLux[x])+ "%",(254,241,95),font=font)   #LUX
                draw.text((135, 295),str(GTemp[x])+ "c",(191,103,16),font=font) #TEMP
                draw.text((190, 295),str(GHum[x])+ "%",(229,180,73),font=font) #HUMUDITY
                draw.text((250, 295),str(GSMst[x])+ "%",(204,153,204),font=font)#SOIL MOIST
                draw.text((310, 295),str(GResp[x])+ "%",(113,64,140),font=font) #RESPIRATION
                draw.text((370, 295),str(GSig[x])+ "%",(00,154,218),font=font)  #SIGNAL
                draw.text((425, 295),str(GBat[x])+ "%",(153,153,153),font=font) #BATTERY

        #Text line 9:
            if (GID[x] == "9"):
                draw.text((20, 320),str(GID[x]),(255,255,255),font=font)        #ID
                draw.text((70, 320),str(GLux[x])+ "%",(254,241,95),font=font)   #LUX
                draw.text((135, 320),str(GTemp[x])+ "c",(191,103,16),font=font) #TEMP
                draw.text((190, 320),str(GHum[x])+ "%",(229,180,73),font=font) #HUMUDITY
                draw.text((250, 320),str(GSMst[x])+ "%",(204,153,204),font=font)#SOIL MOIST
                draw.text((310, 320),str(GResp[x])+ "%",(113,64,140),font=font) #RESPIRATION
                draw.text((370, 320),str(GSig[x])+ "%",(00,154,218),font=font)  #SIGNAL
                draw.text((425, 320),str(GBat[x])+ "%",(153,153,153),font=font) #BATTERY

        #Text line 10:
            if (GID[x] == "10"):
                draw.text((20, 355),str(GID[x]),(255,255,255),font=font)        #ID
                draw.text((70, 355),str(GLux[x])+ "%",(254,241,95),font=font)   #LUX
                draw.text((135, 355),str(GTemp[x])+ "c",(191,103,16),font=font) #TEMP
                draw.text((190, 355),str(GHum[x])+ "%",(229,180,73),font=font) #HUMUDITY
                draw.text((250, 355),str(GSMst[x])+ "%",(204,153,204),font=font)#SOIL MOIST
                draw.text((310, 355),str(GResp[x])+ "%",(113,64,140),font=font) #RESPIRATION
                draw.text((370, 355),str(GSig[x])+ "%",(00,154,218),font=font)  #SIGNAL
                draw.text((425, 355),str(GBat[x])+ "%",(153,153,153),font=font) #BATTERY


            #<td style="color:#"""+ColourX[x]+"""">"""+ str(GID[x]) + """</td>
            #""+ColourX[x]+""


            #           min="0" low="10" high="10" max="100" value=
            #           min="0" max="100" value=
            #----------String For Live table----------#
            writestring1 +="""
                    <tr>
                    <td>"""+ str(GID[x]) + """</td>
                    <td>"""+ str(GLux[x]) + """% <meter min="0" low="10" high="10" max="100" value="""+ str(GLux[x]) + """></meter></td>
                    <td>"""+ str(GTemp[x]) + """% <meter min="0" low="10" high="10" max="100" value="""+ str(GTemp[x]) + """></meter></td>
                    <td>"""+ str(GHum[x]) + """% <meter min="0" low="10" high="10" max="100" value="""+ str(GHum[x]) + """></meter></td>
                    <td>"""+ str(GSMst[x]) + """% <meter min="0" low="10" high="10" max="100" value="""+ str(GSMst[x]) + """></meter></td>
                    <td>"""+ str(GBat[x]) + """% <meter min="0" low="10" high="10" max="100" value="""+ str(GBat[x]) + """></meter></td>
                    <td>"""+ str(GSig[x]) + """% <meter min="0" low="10" high="10" max="100" value="""+ str(GSig[x]) + """></meter></td>
                    </tr>
                    """

            #writestring2 +="Test" + str(GID[x])  #----------String For Graphing----------#




            #----------String For Logging----------#
            statsString += "U:" + str(GID[x]) + "," + str(GLux[x]) + "," + str(GTemp[x]) + "," + str(GHum[x]) + "," + str(GSMst[x]) + "," + str(GBat[x]) + "," + str(GSig[x]) +"*"

        statsString += "\n"
        #-----------------Run Class for saving data to CSV--------------------------#
        hourDataSet(statsString) ###<<<Run hourDataset for saving CSV data>>>
        #--------^--------Run Class for saving data to CSV--------------^-----------#


        #----------File For Live table----------#
        f1Address = Ghomeloc + Gstreamfile
        f1 = open(f1Address,'w')
        f1.write(writestring1)
        f1.close()


        #----------File For Graphing----------#
        #f2Address = Ghomeloc + Ggraphfile
        #f2 = open(f2Address,'w')
        #f2.write(writestring2)
        #f2.close()


        #draw serial debug info to screen:

        if (Debug == True):
            draw.rectangle(((295, 305), (480, 320)), fill="white")
            draw.text((300, 305),str(serBuffer),(0,0,0),font=debugfont) #Serial string. (153,153,153) = grey


        img.save(imageAddress + 'BKG1.png')
        return 'BKG1.png'

class readString():

    def __init__(self,serBuffer,root,sprite,imageAddress):
        self.ATemp = ""
        self.AHum = ""
        self.Lux = ""
        self.SMst = ""
        self.Bat = ""
        self.ID = ""
        self.Sig = ""

        global StList

        global cnt1
        global No_cycles
        global pageNo
        global RelayNames
        global Relays
        global DebugText


        def map(x, in_min, in_max, out_min, out_max):
            return int((x-in_min) * (out_max-out_min) / (in_max-in_min) + out_min)



        try:
            if ("<" in serBuffer):

                ItrL = serBuffer.split(',')


                #ID:
                IDindex1 = (ItrL[0].index("A"))
                IDindex2 = (ItrL[0].index("<"))
                try:
                    self.ID =  str(ItrL[0][(IDindex1) : (IDindex2)])
                    #Identify ID and remove any letters in ID number#
                    try:
                        all=string.maketrans('','')
                        nodigs=all.translate(all, string.digits)
                        self.ID =  self.ID.translate(all, nodigs)

                    except:
                        pass

                except ValueError:
                    self.ID = "XXXX"


                #TEMPERATURE#
                ATindex1 = (ItrL[0].index("<") + 1)
                ATindex2 = len(ItrL[0])
                try:
                    self.ATemp = float (ItrL[0][(ATindex1) : (ATindex2)])
                    self.ATemp = self.ATemp - TempOffset
                    self.ATemp = int(round(self.ATemp))

                    if (self.ATemp > 100):
                        self.ATemp = 100
                        print( "Temp val error")
                    if (self.ATemp < 0):
                        self.ATemp = 0
                        print( "Temp val error")

                except ValueError:
                    print( "Invalid float")
                    #pass
                    self.ATemp = 00

                #HUMIDITY#
                try:
                    self.AHum = float(ItrL[1])
                    self.AHum = self.AHum - HumOffset
                    self.AHum = int(round(self.AHum))

                    if (self.AHum > 100):
                        self.AHum = 100
                        print( "Hum val error")
                    if (self.AHum < 0):
                        self.AHum = 0
                        print( "Hum val error")
                except ValueError:
                    print( "Invalid float")
                    #pass
                    self.AHum = 00

                #LUX#
                try:
                    self.Lux = float(ItrL[2])
                    self.Lux = int(round(self.Lux))

                    if (self.Lux > 100):
                        self.Lux = 100
                        print( "Lux val error")
                    if (self.Lux < 0):
                        self.Lux = 0
                        print( "Lux val error")

                except ValueError:
                    print( "Invalid float")
                    #pass
                    self.Lux = 00

                #SOIL MOISTURE#
                try:
                    self.SMst = float(ItrL[3])
                    self.SMst = int(round(self.SMst))

                    if (self.SMst > 100):
                        self.SMst = 100
                        print( "SMst val error")
                    if (self.SMst < 0):
                        self.SMst = 0
                        print( "SMst val error")
                except ValueError:
                    print( "Invalid float")
                    self.SMst = 00

                #BATTERY CHARGE#
                try:
                    self.Bat = float(ItrL[4])
                    self.Bat = int(round(self.Bat))
                    if (self.Bat > 100):
                        self.Bat = 100
                        #print( "Bat val error")
                    if (self.Bat < 0):
                        self.Bat = 0
                        #print( "Bat val error")

                except ValueError:
                    print( "Invalid float")
                    self.Bat = 00


                try:
                    #SIGNAL STRENGTH#
                    ASindex1 = (0)
                    ASindex2 = (ItrL[5].index(">"))
                    try:
                        self.Sig = str(ItrL[5][(ASindex1) +0 : (ASindex2)])
                        self.Sig = list(map(int(self.Sig),-127,-20,0,100))

                    except ValueError:
                        print( "Invalid float")
                        self.Sig = 00

                except IndexError:
                    print( "Bad signal read")
                    self.Sig = 00

                #cnt1 = 0

                #if (cnt1 == 0):
                #    StList[0] = [self.ID, self.ATemp, self.AHum, self.Lux, self.SMst, self.Bat, self.Sig]

                if (self.ID == "1"):
                    StList[0] = [self.ID, self.ATemp, self.AHum, self.Lux, self.SMst, self.Bat, self.Sig]


                if (self.ID == "2"):
                    StList[1] = [self.ID, self.ATemp, self.AHum, self.Lux, self.SMst, self.Bat, self.Sig]

                if (self.ID == "3"):
                    StList[2] = [self.ID, self.ATemp, self.AHum, self.Lux, self.SMst, self.Bat, self.Sig]

                if (self.ID == "4"):
                    StList[3] = [self.ID, self.ATemp, self.AHum, self.Lux, self.SMst, self.Bat, self.Sig]

                if (self.ID == "5"):
                    StList[4] = [self.ID, self.ATemp, self.AHum, self.Lux, self.SMst, self.Bat, self.Sig]
                    #print( StList[4])

                if (self.ID == "6"):
                    StList[5] = [self.ID, self.ATemp, self.AHum, self.Lux, self.SMst, self.Bat, self.Sig]

                if (self.ID == "7"):
                    StList[6] = [self.ID, self.ATemp, self.AHum, self.Lux, self.SMst, self.Bat, self.Sig]

                if (self.ID == "8"):
                    StList[7] = [self.ID, self.ATemp, self.AHum, self.Lux, self.SMst, self.Bat, self.Sig]

                if (self.ID == "9"):
                    StList[8] = [self.ID, self.ATemp, self.AHum, self.Lux, self.SMst, self.Bat, self.Sig]

                if (self.ID == "10"):
                    StList[9] = [self.ID, self.ATemp, self.AHum, self.Lux, self.SMst, self.Bat, self.Sig]

                cnt1 = cnt1 +1
                #print( cnt1)

                if (cnt1 >= No_cycles):


                    comparison1 = updateScreen() ###<<<new instance of Updtae screen>>>###
                    newScreen = comparison1.returnCompare(serBuffer,StList[0],StList[1],StList[2],StList[3],StList[4],StList[5],StList[6],StList[7],StList[8],StList[9], imageAddress)
                    BKGimg[0] = ImageTk.PhotoImage(Image.open(imageAddress + newScreen))###<<<Update Background>>>###
                    if (pageNo == 0):
                        root.itemconfig(sprite,image = BKGimg[0]) #New background loaded
                        #pageNo = 0
                    cnt1 = 0



            if ("*S?:" in serBuffer):
                #print( "Relay Query")
                RStatString = serBuffer[4:len(serBuffer)]

                ItrQ = RStatString.split(',')
                for x in enumerate(ItrQ):

                    if (x[0] >= len(RelayNames)):
                        del ItrQ[x[0]]
                    #print( "R"+ str(x[0]+ 1)+": " + str(x[1]))

                #print( ItrQ)
                #print( Relays)
                try:
                    Relays = ItrQ
                    print(( "Relay Status: " + str(Relays) + "\n"))
                    DebugText +="Relay Status: " + str(Relays) + "\n"


                except:
                    print( "Relay assigment error")



        except ValueError:
            print( "Value Error in Serial Response")
            pass


#---------------------Data Recording Classes-----------------------#
class hourDataSet():
    def __init__(self, SBasicStats):

        global Boolchecktime
        global hourIteration
        global DebugText

        if (datetime.now().time().minute ==00): #once every hour
            if (Boolchecktime == False): #Check to write only once
                #-------------\/-EVENTS TO OCCUR EVERY HOUR-\/------------------#
                EveryHour()
                #--------------^EVENTS TO OCCUR EVERY HOUR^-------------------#


                try:
                    url1 = 'http://www.bom.gov.au/vic/forecasts/melbourne.shtml'
                    scrape1 = DynamicScrape()
                    data = scrape1.goScrape(url1,'div','class','forecast',"","\n",200)
                    saveWeatherdata(data)
                    print( "New weather data files added")
                    DebugText += "New weather data files added\n"

                except:
                    now = datetime.now()
                    timestring = now.strftime("%Y-%m-%d %H:%M")
                    print(( "Unable to create new weather data files at: " + str(timestring)))
                    DebugText += "Unable to create new weather data files at: " + str(timestring)
                    DebugText += "\n"



                fx = open(CSV1File, 'r')       #Open file, remove first line and save
                content= fx.read()
                dataList = content.split('\n')
                fx.close

                hourIteration = len(dataList)-1 #Remove last '\n'
                #print( hourIteration)

                if (hourIteration >= 24):
                    ind2 = content.index('\n')+1
                    ind3 = len(content)
                    adjcontent = content[ind2 : ind3]

                    fx = open(CSV1File, 'w')  #If already 24 recordings, remove recording from line 1 and save
                    fx.write(adjcontent)
                    fx.close

                    fx = open(CSV1File, 'a')  #Open fileand append new reading at bottom of list
                    fx.write(SBasicStats)
                    fx.close


                else:   #List does not yet contain 24 recordings
                    fx = open(CSV1File, 'a')
                    fx.write(SBasicStats)
                    fx.close



                dayDataSet() ## <<<Run Daily operation>>>
                Boolchecktime = True



            else: #Has already been written once wthin this munite so do nothing
                pass



        else: # Not the right minute to write values so ensure Boolchecktime is reset to false
            Boolchecktime = False

class dayDataSet():
    def __init__(self):
        #global Boolchecktime2
        global dayIteration
        global dayIteration2

        #At every new hour: get min, max and average of past hour from CSV1File
        if (datetime.now().time().hour ==00): #Change to hour
            dayIteration = dayIteration + 1
            dayIteration2 = dayIteration2 + 1


            ##print( "dayIteration: " + str(dayIteration))
            #if (Boolchecktime2 == False): #not needed
            #------------------------------------------#
            now = datetime.now()
            timestring = now.strftime("%Y-%m-%d")

            savedata = ''
            savedata += str(timestring)
            savedata += "\n"

            IDxList = [] #List allocation for Sensor ID's
            a1List = [] #List allocation for Temp
            b1List = [] #List allocation for Hum
            c1List = [] #List allocation for Lux
            d1List = [] #List allocation for SMst

            sensorList = [[],[],[],[],[],[],[],[],[],[],[]]

            pullData = open(CSV1File,"r").read()
            dataList = pullData.split('\n')

            for eachLine in dataList:
                if len(eachLine) > 1:
                    recording = eachLine.split('*')
                    #print( recording)

                    for x in enumerate(recording):
                        #print( x)
                        if (x[1] != ''):
                            IDx, a1, b1, c1, d1,e1,f1 = x[1].split(',')
                            IDx = IDx[2:len(IDx)] #remove 'U:' form ID string to get actual unit number
                            if (int(IDx)!=0):IDxList.append(int(IDx)) #ID
                            if (int(a1)!=0):a1List.append(int(a1)) #temp
                            if (int(b1)!=0):b1List.append(int(b1)) #hum
                            if (int(c1)!=0):c1List.append(int(c1)) #lux
                            if (int(d1)!=0):d1List.append(int(d1)) #smst

                            #if(int(IDx)!=0): print( IDx,a1,b1,c1,d1
                            if(int(IDx)!=0):sensorList[int(IDx)].append([a1,b1,c1,d1])


            Templist = [[],[],[],[],[],[],[],[],[],[]]
            Humlist = [[],[],[],[],[],[],[],[],[],[]]
            Luxlist = [[],[],[],[],[],[],[],[],[],[]]
            Smstlist = [[],[],[],[],[],[],[],[],[],[]]

            #print( sensorList)
            for y in range (0,len(sensorList)):  #For each sensor in the list
                #print( sensorList[y])
                if sensorList[y]: #Check if list segment is empty
                    ##print( "Sensor " + str(y) + ":" + str(sensorList[y])v
                    readings = sensorList[y]
                    for x in range (0,len(readings)): #For each reading per sensor
                        Templist[y].append(sensorList[y][x][0])
                        Humlist[y].append(sensorList[y][x][1])
                        Luxlist[y].append(sensorList[y][x][2])
                        Smstlist[y].append(sensorList[y][x][3])

            #-----------------------------------------------------------#
            # #Temp
            for i in range (0,len(Templist)):
                if Templist[i]:
                    ##print( Templist[i])
                    TempAve = 0
                    TempMin = 99
                    TempMax = 0

                    for e in enumerate(Templist[i]):
                        #print( e)
                        TempAve += int(e[1])
                        if(TempMax<int(e[1])):TempMax = int(e[1])
                        if(TempMin>int(e[1])):TempMin = int(e[1])


                    #print( len(Templist[i]))
                    TempAve = TempAve/len(Templist[i])
                    ##print( "--------")
                    savedata += "S("+ str(i)+ ") Temp, Ave:" +str(TempAve)
                    savedata += ", Max:" +str(TempMax)
                    savedata += ", Min:" +str(TempMin)
                    savedata += "\n"
                    #print( "----------------------")

            #-----------------------------------------------------------#
            # #Hum
            savedata += "\n"
            for i in range (0,len(Humlist)):
                if Humlist[i]:
                    #print( Humlist[i])
                    HumAve = 0
                    HumMin = 99
                    HumMax = 0

                    for e in enumerate(Humlist[i]):
                        #print( e)
                        HumAve += int(e[1])
                        if(HumMax<int(e[1])):HumMax = int(e[1])
                        if(HumMin>int(e[1])):HumMin = int(e[1])


                    #print( len(Humlist[i])v
                    HumAve = HumAve/len(Humlist[i])
                    ##print( "--------")
                    savedata +=  "S("+ str(i)+ ") Hum, Ave:" +str(HumAve)
                    savedata += ", Max:" +str(HumMax)
                    savedata += ", Min:" +str(HumMin)
                    savedata += "\n"
                    #print( "----------------------")


            #-----------------------------------------------------------#
            # #Lux
            savedata += "\n"
            for i in range (0,len(Luxlist)):
                if Luxlist[i]:
                    ##print( Luxlist[i])
                    LuxAve = 0
                    LuxMin = 99
                    LuxMax = 0

                    for e in enumerate(Luxlist[i]):
                        #print( e)
                        LuxAve += int(e[1])
                        if(LuxMax<int(e[1])):LuxMax = int(e[1])
                        if(LuxMin>int(e[1])):LuxMin = int(e[1])


                    #print( len(Luxlist[i]))
                    LuxAve = LuxAve/len(Luxlist[i])
                    ##print( "--------")
                    savedata +=  "S("+ str(i)+ ") Lux, Ave:" +str(LuxAve)
                    savedata += ", Max:" +str(LuxMax)
                    savedata += ", Min:" +str(LuxMin)
                    savedata += "\n"
                    #print( "----------------------")



            #-----------------------------------------------------------#
            # #Smst
            savedata += "\n"
            for i in range (0,len(Smstlist)):
                if Smstlist[i]:
                    ##print( Smstlist[i])
                    SmstAve = 0
                    SmstMin = 99
                    SmstMax = 0

                    for e in enumerate(Smstlist[i]):
                        #print( e)
                        SmstAve += int(e[1])
                        if(SmstMax<int(e[1])):SmstMax = int(e[1])
                        if(SmstMin>int(e[1])):SmstMin = int(e[1])


                    #print( len(Smstlist[i]))
                    SmstAve = SmstAve/len(Smstlist[i])
                    ##print( "--------")
                    savedata += "S("+ str(i)+ ") Smst, Ave:" +str(SmstAve)
                    savedata += ", Max:" +str(SmstMax)
                    savedata += ", Min:" +str(SmstMin)
                    savedata += "\n"
                    #print( "----------------------")
            savedata += "#----------------------------------#"
            savedata += "\n"
            #-----------------------------------------------------------#
            #print( savedata)
            if (dayIteration >= 7):
                pass
                    # ind2 = content.index('\n')+1
                    # ind3 = len(content)
                    # adjcontent = content[ind2 : ind3]

                    # fx = open(CSV1File, 'w')  #If already 24 recordings, remove recording from line 1 and save
                    # fx.write(adjcontent)
                    # fx.close
                    #
                    # fx = open(CSV1File, 'a')  #Open fileand append new reading at bottom of list
                    # fx.write(SBasicStats)
                    # fx.close


            else:   #List does not yet contain 24 recordings
                fx = open(CSV2File, 'a')
                fx.write(savedata)
                fx.close
            

        else:
            pass

class weekDataSet():
    #after 7 iteratitons start overwritng from the start again
    #at midninght on 7th iteration tranfer / apend pastweek.csv to pastmonth.csv
    def __init__(self):
        #global Boolchecktime2
        global weekIteration
        global weekIteration2

        weekIteration = weekIteration + 1
        weekIteration2 = weekIteration2 + 1

        pullData = open(CSV2File,"r").read()
        dataList = pullData.split('\n')

        a1List = []
        b1List = []
        c1List = []
        d1List = []
        e1List = []
        f1List = []
        g1List = []
        h1List = []
        i1List = []
        j1List = []
        k1List = []
        l1List = []
        for eachLine in dataList:
            if len(eachLine) > 1:
                a1, b1, c1, d1, e1, f1, g1, h1, i1, j1, k1, l1 = eachLine.split(',')
                a1List.append(int(a1)) #Temp Average
                b1List.append(int(b1)) #Temp min
                c1List.append(int(c1)) #Temp max
                d1List.append(int(d1)) #Hum average
                e1List.append(int(e1)) #Hum min
                f1List.append(int(f1)) #Hum max
                g1List.append(int(g1)) #Lux average
                h1List.append(int(h1)) #Lux min
                i1List.append(int(i1)) #Lux max
                j1List.append(int(j1)) #SMst average
                k1List.append(int(k1)) #SMst min
                l1List.append(int(l1)) #SMst max



        a1LAv = int(round(sum(a1List)/int(len(a1List))))
        b1LAv = int(round(min(b1List)/int(len(b1List))))
        c1LAv = int(round(max(c1List)/int(len(c1List))))
        d1LAv = int(round(sum(d1List)/int(len(d1List))))
        e1LAv = int(round(min(e1List)/int(len(e1List))))
        f1LAv = int(round(max(f1List)/int(len(f1List))))
        g1LAv = int(round(sum(g1List)/int(len(g1List))))
        h1LAv = int(round(min(h1List)/int(len(h1List))))
        i1LAv = int(round(max(i1List)/int(len(i1List))))
        j1LAv = int(round(sum(j1List)/int(len(j1List))))
        k1LAv = int(round(min(k1List)/int(len(k1List))))
        l1LAv = int(round(max(l1List)/int(len(l1List))))



        stats = a1LAv, b1LAv, c1LAv, d1LAv, e1LAv, f1LAv, g1LAv, h1LAv, i1LAv, j1LAv, k1LAv, l1LAv

        #Its been 4 weeks so transferr days to month
        if (weekIteration > 4):
            with open(CSV3File, 'r') as f1:
                #print( "*Read only")
                content = f1.read()
                #print( content)
                f1.close()

                with open(CSV3File, 'w') as f1:
                    #ind1 = content.index(0)
                    ind2 = content.index('\n') + 1
                    ind3 = len(content)
                    adjcontent = content[ind2 : ind3]
                    #print( adjcontent)
                    f1.write(adjcontent)
                    f1.close()


                with open(CSV3File, 'a') as f3:
                    #print( "*Append")

                    CSVwriter1 = csv.writer(f3, delimiter=',',
                                            quotechar=',', quoting=csv.QUOTE_MINIMAL)
                    CSVwriter1.writerow(stats)
                    f3.close()

                #If 7th of sevenb days pass all of CSV2 to CSV3
                if (weekIteration2 == 4):
                    monthDataSet()
                    weekIteration2 = 4




        else:
            #Past 7 days hrs
            with open(CSV3File, 'a') as csv3file:
                CSVwriter1 = csv.writer(csv3file, delimiter=',',
                                        quotechar=',', quoting=csv.QUOTE_MINIMAL)
                CSVwriter1.writerow(stats)
                csv3file.close()

class monthDataSet():
    #after 30 iteratitons start overwritng from the start again
    #at midninght on 30th iteration tranfer / apend pastmonth.csv to pastyear.csv
    def __init__(self):
        #global Boolchecktime2
        global monthIteration
        global monthIteration2

        monthIteration = monthIteration + 1
        monthIteration2 = monthIteration2 + 1

        pullData = open(CSV3File,"r").read()
        dataList = pullData.split('\n')

        a1List = []
        b1List = []
        c1List = []
        d1List = []
        e1List = []
        f1List = []
        g1List = []
        h1List = []
        i1List = []
        j1List = []
        k1List = []
        l1List = []
        for eachLine in dataList:
            if len(eachLine) > 1:
                a1, b1, c1, d1, e1, f1, g1, h1, i1, j1, k1, l1 = eachLine.split(',')
                a1List.append(int(a1)) #Temp Average
                b1List.append(int(b1)) #Temp min
                c1List.append(int(c1)) #Temp max
                d1List.append(int(d1)) #Hum average
                e1List.append(int(e1)) #Hum min
                f1List.append(int(f1)) #Hum max
                g1List.append(int(g1)) #Lux average
                h1List.append(int(h1)) #Lux min
                i1List.append(int(i1)) #Lux max
                j1List.append(int(j1)) #SMst average
                k1List.append(int(k1)) #SMst min
                l1List.append(int(l1)) #SMst max



        a1LAv = int(round(sum(a1List)/int(len(a1List))))
        b1LAv = int(round(min(b1List)/int(len(b1List))))
        c1LAv = int(round(max(c1List)/int(len(c1List))))
        d1LAv = int(round(sum(d1List)/int(len(d1List))))
        e1LAv = int(round(min(e1List)/int(len(e1List))))
        f1LAv = int(round(max(f1List)/int(len(f1List))))
        g1LAv = int(round(sum(g1List)/int(len(g1List))))
        h1LAv = int(round(min(h1List)/int(len(h1List))))
        i1LAv = int(round(max(i1List)/int(len(i1List))))
        j1LAv = int(round(sum(j1List)/int(len(j1List))))
        k1LAv = int(round(min(k1List)/int(len(k1List))))
        l1LAv = int(round(max(l1List)/int(len(l1List))))



        stats = a1LAv, b1LAv, c1LAv, d1LAv, e1LAv, f1LAv, g1LAv, h1LAv, i1LAv, j1LAv, k1LAv, l1LAv

        #Its been 12 months so transferr months to year
        if (monthIteration > 12):
            with open(CSV4File, 'r') as f1:
                #print( "*Read only")
                content = f1.read()
                #print( content)
                f1.close()

                with open(CSV4File, 'w') as f1:
                    #ind1 = content.index(0)
                    ind2 = content.index('\n') + 1
                    ind3 = len(content)
                    adjcontent = content[ind2 : ind3]
                    #print( adjcontent)
                    f1.write(adjcontent)
                    f1.close()


                with open(CSV4File, 'a') as f3:
                    #print( "*Append")

                    CSVwriter1 = csv.writer(f3, delimiter=',',
                                            quotechar=',', quoting=csv.QUOTE_MINIMAL)
                    CSVwriter1.writerow(stats)
                    f3.close()

                #If 7th of sevenb days pass all of CSV2 to CSV3
                if (monthIteration2 == 12):
                    #yearDataSet()
                    monthIteration2 = 12




        else:
            #Past 7 days hrs
            with open(CSV4File, 'a') as csv4file:
                CSVwriter1 = csv.writer(csv4file, delimiter=',',
                                        quotechar=',', quoting=csv.QUOTE_MINIMAL)
                CSVwriter1.writerow(stats)
                csv4file.close()



class makeGraphData():
    def __init__(self):

        global CSV1File

        global LuxFile
        global TempFile
        global HumFile
        global SmstFile

        print( "Making JSON Graph Data")

        pullData = open(CSV1File,"r").read()
        ind1 = pullData.find("\n")
        adjcontent = pullData[0 : ind1]
        probesCount = [m.start() for m in re.finditer("U:", adjcontent)]
        probesCount =  len(probesCount)


        dataList = pullData.split('\n')

        #Create matrixes#
        #w, h = len(dataList)-1, probesCount;
        w, h = len(dataList), probesCount;
        LuxMatrix = [[0 for x in range(w)] for y in range(h)]
        TempMatrix = [[0 for x in range(w)] for y in range(h)]
        HumMatrix = [[0 for x in range(w)] for y in range(h)]
        SmstMatrix = [[0 for x in range(w)] for y in range(h)]


        LineIndex = 0

        for eachLine in dataList:
            if len(eachLine) > 1:

                Uindex = pullData.find("U:")
                for x in range(0, probesCount):

                    Uindex = eachLine.find("U:", Uindex + x)  #set Line index

                    #Find Lux value
                    index1 = eachLine.find(",", Uindex)
                    index2 = eachLine.find(",", index1 +1)
                    newdata = eachLine[(index1 + 1):index2]
                    #LuxMatrix[x].pop(x)
                    if (len(LuxMatrix[x]) >24):
                        while(len(LuxMatrix[x]) >24):
                            del LuxMatrix[x][0]
                    del LuxMatrix[x][0]
                    LuxMatrix[x].append(newdata) #List of Lux data of all Lux readings

                    #print( newdata)

                    #Find Temp value
                    index1 = eachLine.find(",",index1 +1)
                    index2 = eachLine.find(",",index1 +2)
                    newdata = eachLine[(index1 + 1):index2]
                    #TempMatrix[x].pop(x)
                    if (len(TempMatrix[x]) >24):
                        while(len(TempMatrix[x]) >24):
                            del TempMatrix[x][0]
                    del TempMatrix[x][0]
                    TempMatrix[x].append(newdata) #List of Temp data of all Temp readings
                    #print( newdata)


                    #Find Hum value
                    index1 = eachLine.find(",",index1 +2) #2   ,2
                    index2 = eachLine.find(",",index1 +1) #1   ,3
                    newdata = eachLine[(index1 + 1):index2]
                    #HumMatrix[x].pop(x)
                    if (len(HumMatrix[x]) >24):
                        while(len(HumMatrix[x]) >24):
                            del HumMatrix[x][0]
                    del HumMatrix[x][0]
                    HumMatrix[x].append(newdata)
                    #print( newdata)

                    #Find Smst value
                    index1 = eachLine.find(",",index1 +3)
                    index2 = eachLine.find(",",index1 +2)
                    newdata = eachLine[(index1 + 1):index2]
                    #SmstMatrix[x].pop(x)
                    if (len(SmstMatrix[x]) >24):
                        while(len(SmstMatrix[x]) >24):
                            del SmstMatrix[x][0]
                    del SmstMatrix[x][0]
                    SmstMatrix[x].append(newdata)
                    #print( newdata)

        luxString = ""
        tempString = ""
        humString = ""
        SmstString = ""
        ColourX = ["0099ff","00ff99","ffff00","ff6600","0099ff","ff3399","cc00ff","3333cc","339933","996633","993366","808080","000000","ccccff","ccffcc","ffffcc","ffcc99","ffcccc","ccffff","663300","993333"]

        xxx = 1
        for eachLine in LuxMatrix:
            #print( eachLine)
            writestring = str(eachLine)
            writestring = re.sub('[\' ]', '', writestring)
            #print( writestring)
            writestring = "{\"data\":" + writestring + ",\"label\":\"Probe" + str(xxx) + "\",\"borderColor\":\"#"+ColourX[xxx]+"\",\"fill\":false}"
            if (xxx < probesCount):
                writestring += ',\n'
            else: writestring += ']'
            luxString += writestring
            xxx = xxx + 1
        luxString = "[" + luxString

        # Write Lux list file
        fxAddress = Ghomeloc + LuxFile
        fx = open(fxAddress,'w')
        fx.write(luxString)
        fx.close()


        #---------------------------------------#
        xxx = 1
        for eachLine in TempMatrix:
            writestring = str(eachLine)
            writestring = re.sub('[\' ]', '', writestring)
            writestring = "{\"data\":" + writestring + ",\"label\":\"Probe" + str(xxx) + "\",\"borderColor\":\"#"+ColourX[xxx]+"\",\"fill\":false}"

            if (xxx < probesCount):
                writestring += ',\n'
            else: writestring += ']'
            tempString += writestring
            xxx = xxx + 1
        tempString  = "[" + tempString

        # Write Temp list file
        fx1Address = Ghomeloc + TempFile
        fx1 = open(fx1Address,'w')
        fx1.write(tempString)
        fx1.close()


        #---------------------------------------#
        xxx = 1
        for eachLine in HumMatrix:
            writestring = str(eachLine)
            writestring = re.sub('[\' ]', '', writestring)
            writestring = "{\"data\":" + writestring + ",\"label\":\"Probe" + str(xxx) + "\",\"borderColor\":\"#"+ColourX[xxx]+"\",\"fill\":false}"

            if (xxx < probesCount):
                writestring += ',\n'
            else: writestring += ']'
            humString += writestring
            xxx = xxx + 1
        humString = "[" + humString

        # Write Hum list file
        fx1Address = Ghomeloc + HumFile
        fx1 = open(fx1Address,'w')
        fx1.write(humString)
        fx1.close()


        #---------------------------------------#
        xxx = 1
        for eachLine in SmstMatrix:
            writestring = str(eachLine)
            writestring = re.sub('[\' ]', '', writestring)
            writestring = "{\"data\":" + writestring + ",\"label\":\"Probe" + str(xxx) + "\",\"borderColor\":\"#"+ColourX[xxx]+"\",\"fill\":false}"

            if (xxx < probesCount):
                writestring += ',\n'
            else: writestring += ']'
            SmstString += writestring
            xxx = xxx + 1
        SmstString = "[" + SmstString

        # Write Smst list file
        fx1Address = Ghomeloc + SmstFile
        fx1 = open(fx1Address,'w')
        fx1.write(SmstString)
        fx1.close()

        #---------------------------------------#

#---------------------Weather Details (for GUI and webpage)-----------------------#
class DynamicScrape():

    def __init__(self):
        pass

    def goScrape(self,url,component,attType,attName,startindex,stopindex,allowance):

        def removeBlankLines(txt):  #remove blank lines#
            return '\n'.join([x for x in txt.split("\n") if x.strip()!=''])

        pageData = url
        page = urllib.request.urlopen(pageData)
        soup = BeautifulSoup(page, 'html.parser')

        #name_box = soup.find('div', attrs={'id': 'content'})
        name_box = soup.find(component, attrs={attType : attName})
        content = name_box.text.strip()

        content = removeBlankLines(content)

        ind1 = content.find(startindex)
        ind2 = content.find(stopindex,ind1+allowance)

        adjcontent = content[ind1 : ind2]
        adjcontent = adjcontent.replace(".", ".\n")

        #print( adjcontent)
        return adjcontent

        #print( (removeBlankLines(content)))

class saveWeatherdata():

    def __init__(self,datastring):

        global weatherfile1
        global weatherfile2
        global Ghomeloc


        ind1 = datastring.find("")
        ind2 = datastring.find("%")

        adjcontent1 = datastring[ind1:ind2+1]
        adjcontent2 = datastring[ind2+2:]


        adjcontent1 = adjcontent1.replace("\n ","\n")
        adjcontent2 = adjcontent2.replace("\n ","\n")

        #print( adjcontent1)
        #print( "###############")
        #print( adjcontent2)

        #----------File For weather data 1----------#
        fAddress = Ghomeloc + weatherfile1
        f = open(fAddress,'w')
        f.write(str(adjcontent1))
        f.close()

        #----------File For weather data 2----------#
        fAddress = Ghomeloc + weatherfile2
        f = open(fAddress,'w')
        f.write(str(adjcontent2))
        f.close()

#---------------------7 Day Weather forcast (for webpage)-----------------------#
class webScrape():
    def __init__(self):
        global weatherfile3
        global Ghomeloc
        global DebugText

        pageData = 'http://www.bom.gov.au/vic/forecasts/melbourne.shtml'
        page = urllib.request.urlopen(pageData)
        # parse the html using beautiful soup and store in variable `soup`
        soup = BeautifulSoup(page, 'html.parser')
        # Take out the <div> of name and get its value
        name_box = soup.find('div', attrs={'id': 'content'})
        #print( name_box.prettify())

        #textfind = soup.find('class', attrs={'id': 'max'})

        #textfind = soup.select("div em")
        textfind = str(soup.select("div em"))
        textfind = textfind.split(',')

        minlist =  [x for x in textfind if 'min' in x]
        maxlist =  [x for x in textfind if 'max' in x]

        try:
            adjustedMinList =[]
            for x in enumerate(minlist):
                entry=  str(re.findall(r'\d+', x[1]))
                entry = entry.translate(None, '[]\'')
                #entry = entry.replace(']', ' ')
                adjustedMinList.append (entry)

            adjustedMaxList = []
            for x in enumerate(maxlist):
                entry=  str(re.findall(r'\d+', x[1]))
                entry = entry.translate(None, '[]\'')
                #entry = entry.replace(']', ' ')
                adjustedMaxList.append (entry)

            #print( adjustedMinList)
            #print( adjustedMaxList)


            images = []
            for img in name_box.findAll('img'):
                images.append(img.get('src'))



            for x in enumerate (images):
                if "u" in images[x[0]]:
                    #print( "Got u")
                    pass
                if "rain_" in images[x[0]]:
                    images.pop(x[0])
                    #print( x[0])

            startUrl = "http://www.bom.gov.au/"

            day0 = startUrl + str(images[0])
            day1 = startUrl + str(images[10])
            day2 = startUrl + str(images[11])
            day3 = startUrl + str(images[12])
            day4 = startUrl + str(images[13])
            day5 = startUrl + str(images[14])
            day6 = startUrl + str(images[15])

            dayString = []

            def weekday():
                now = datetime.now()
                check = calendar.weekday(now.year, now.month, now.day)
                if check == 0:
                    return ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
                elif check == 1:
                    return ["Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday","Monday"]
                elif check == 2:
                    return ["Wednesday","Thursday","Friday","Saturday","Sunday","Monday","Tuesday"]
                elif check == 3:
                    return ["Thursday","Friday","Saturday","Sunday","Monday","Tuesday","Wednesday"]
                elif check == 4:
                    return ["Friday","Saturday","Sunday","Monday","Tuesday","Wednesday","Thursday"]
                elif check == 5:
                    return ["Saturday","Sunday","Monday","Tuesday","Wednesday","Thursday","Friday"]
                elif check == 6:
                    return ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
                else:
                    return "Error"

            dayString = weekday()


            #test = "Today"

            forcaststring = """
            <table width="50" border="0">
              <tr>
                <td><font size="2">"""+ "Today" + """</td>
                <td><center><img src="""+ day0 + """ width="35" height="35"></center></td>
                <td align="right"><font size="1">"""+ "Max: "+ adjustedMaxList[0] +"""</td>
                <td align="right"><font size="1">"""+ "Min: "+ adjustedMinList[0] +"""</td>
              </tr>
              <tr>
                <td><font size="2">"""+ str(dayString[1]) + """</td>
                <td><center><img src="""+ day1 + """ width="35" height="35"></center></td>
                <td align="right"><font size="1">"""+ "Max: "+ adjustedMaxList[1] +"""</td>
                <td align="right"><font size="1">"""+ "Min: "+ adjustedMinList[1] +"""</td>
              </tr>
              <tr>
                <td><font size="2">"""+ str(dayString[2]) + """</td>
                <td><center><img src="""+ day2 + """ width="35" height="35"></center></td>
                <td align="right"><font size="1">"""+ "Max: "+ adjustedMaxList[2] +"""</td>
                <td align="right"><font size="1">"""+ "Min: "+ adjustedMinList[2] +"""</td>
              </tr>
              <tr>
                <td><font size="2">"""+ str(dayString[3]) + """</td>
                <td><center><img src="""+ day3 + """ width="35" height="35"></center></td>
                <td align="right"><font size="1">"""+ "Max: "+ adjustedMaxList[3] +"""</td>
                <td align="right"><font size="1">"""+ "Min: "+ adjustedMinList[3] +"""</td>
              </tr>
              <tr>
                <td><font size="2">"""+ str(dayString[4]) + """</td>
                <td><center><img src="""+ day4 + """ width="35" height="35"></center></td>
                <td align="right"><font size="1">"""+ "Max: "+ adjustedMaxList[4] +"""</td>
                <td align="right"><font size="1">"""+ "Min: "+ adjustedMinList[4] +"""</td>
              </tr>
              <tr>
                <td><font size="2">"""+ str(dayString[5]) + """</td>
                <td><center><img src="""+ day5 + """ width="35" height="35"></center></td>
                <td align="right"><font size="1">"""+ "Max: "+ adjustedMaxList[5] +"""</td>
                <td align="right"><font size="1">"""+ "Min: "+ adjustedMinList[5] +"""</td>
              </tr>
              <tr>
                <td><font size="2">"""+ str(dayString[6]) + """</td>
                <td><center><img src="""+ day6 + """ width="35" height="35"></center></td>
                <td align="right"><font size="1">"""+ "Max: "+ adjustedMaxList[6] +"""</td>
                <td align="right"><font size="1">"""+ "Min: "+ adjustedMinList[6] +"""</td>
              </tr>
            </table>
            """

            #print( forcaststring)

            #----------File For Live table----------#
            f1Address = Ghomeloc + weatherfile3
            f1 = open(f1Address,'w')
            f1.write(forcaststring)
            f1.close()

        except:
            now = datetime.now()
            timestring = now.strftime("%Y-%m-%d %H:%M")
            print(( "Error with webscrape at: " + str(timestring)))
            DebugText += "Error with webscrape at: " + str(timestring)
            DebugText += "\n"


class getTime():
    def __init__(self):

        global datefile
        global Ghomeloc
        global hourIteration
        global DebugText

        print( "Time stamp recorded")
        DebugText += "Time stamp recorded\n"

        now = datetime.now()
        timestring = now.strftime("%Y-%m-%d %H:%M")


        fxAddress = Ghomeloc + datefile
        try:
            fx = open(fxAddress, 'r')
            content= fx.read()
            fx.close
            #hourIteration = len(dataList)-1

        except:
            print( "File has not yet been created")
            fx = open(fxAddress, 'w')
            fx.write("")
            fx.close
            content="\n"


        if (hourIteration >= 24):
            ind2 = content.index('\n')+1     #Open file, remove first line and save
            ind3 = len(content)
            adjcontent = content[ind2 : ind3]
            fx = open(fxAddress, 'w')
            fx.write(adjcontent)
            fx.close

            fx = open(fxAddress, 'a')       #Open file and append new reading
            fx.write(timestring)
            fx.write('\n')
            fx.close


        else:
            fx = open(fxAddress, 'a')
            fx.write(timestring)
            fx.write('\n')
            fx.close
            #Past 24 hrs append to file which will remain 24 iterations


#---------------------Webserver Classes-----------------------#
class webserver(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        global WebserverPort
        global DebugText
        global internetConnection

        while not internetConnection:
            print( "Webserver detected no internet")
            Webserver_internet = internet_Test()
            internetConnection = Webserver_internet.run()
            time.sleep(10)

        #    print( "Internet Connection = " + str(internetConnection))


        print(( 'Serving Http on port %s ...' % WebserverPort))
        DebugText += 'Serving Http on port %s ...' % WebserverPort
        DebugText += "\n"

        server = http.server.HTTPServer
        handler = http.server.CGIHTTPRequestHandler
        server_address = ("", WebserverPort)
        #handler.cgi_directories = ["/"]

        httpd = server(server_address, handler)
        httpd.serve_forever()

class simpleServer(threading.Thread): #Not in use
    def __init__(self):
        threading.Thread.__init__(self)

        class SimpleEcho(WebSocket):
           global StreamPort
           global internetConnection

           while not internetConnection:
                print( "Socketserver detected no internet")
                Socketserver_internet = internet_Test()
                internetConnection = Socketserver_internet.run()
                time.sleep(10)

           print(( 'Serving Socket on port %s ...' % StreamPort))

           def handleMessage(self):
              self.sendMessage(self.data)
              print( (self.data))



           def handleConnected(self):
              pass

           def handleClose(self):
              pass

        clients = []
        class SimpleChat(WebSocket):

           def handleMessage(self):
                global relayMSG
                global Relays
                global RelayID

                for client in clients:
                    #if client != self:
                    #   client.sendMessage(self.address[0] + u' - ' + self.data)
                    client.sendMessage(self.address[0] + ' - ' + self.data)
                print(( "Received: " + str(self.data)))

              #----------------------------------#
                if (str(self.data) == "RX_?"):

                    relaystatus = ""
                    for x in enumerate (Relays):
                        relaystatus += "R" + str(x[0]+1) + "_" + str(x[1] + ",")

                    #print( Relays)
                    #print( relaystatus)

                    for client in clients:
                        client.sendMessage(self.address[0] + ' - ' + relaystatus)

                #----------------------------------#
                if (str(self.data) == "R1_ON"):
                    relayMSG = RelayID + ": R1_ON"
                    Relays[0] = "ON"

                if (str(self.data) == "R1_OFF"):
                    relayMSG = RelayID + ": R1_OFF"
                    Relays[0] = "OFF"
                #----------------------------------#
                if (str(self.data) == "R2_ON"):
                    relayMSG += RelayID + ": R2_ON"
                    Relays[1] = "ON"

                if (str(self.data) == "R2_OFF"):
                    relayMSG = RelayID + ": R2_OFF"
                    Relays[1] = "OFF"
                #----------------------------------#
                if (str(self.data) == "R3_ON"):
                    relayMSG = RelayID + ": R3_ON"
                    Relays[2] = "ON"

                if (str(self.data) == "R3_OFF"):
                    relayMSG = RelayID + ": R3_OFF"
                    Relays[2] = "OFF"
                #----------------------------------#
                if (str(self.data) == "R4_ON"):
                    relayMSG = RelayID + ": R4_ON"
                    Relays[3] = "ON"

                if (str(self.data) == "R4_OFF"):
                    relayMSG = RelayID + ": R4_OFF"
                    Relays[3] = "OFF"
                #----------------------------------#

                #relayMSG = RelayID + ": STATUS?"






           def handleConnected(self):
              print( (self.address, 'connected'))
              for client in clients:
                 client.sendMessage(self.address[0] + ' - connected')
                 print( (self.address[0] + ' - connected'))
              clients.append(self)

           def handleClose(self):
              clients.remove(self)
              print( (self.address, 'closed'))
              for client in clients:
                 client.sendMessage(self.address[0] + ' - disconnected')




        parser = OptionParser(usage="usage: %prog [options]", version="%prog 1.0")
        parser.add_option("--host", default='', type='string', action="store", dest="host", help="hostname (localhost)")
        parser.add_option("--port", default=StreamPort, type='int', action="store", dest="port", help="port (8889)")
        parser.add_option("--example", default='chat', type='string', action="store", dest="example", help="echo, chat")
        parser.add_option("--ssl", default=0, type='int', action="store", dest="ssl", help="ssl (1: on, 0: off (default))")
        parser.add_option("--cert", default='./cert.pem', type='string', action="store", dest="cert", help="cert (./cert.pem)")
        parser.add_option("--key", default='./key.pem', type='string', action="store", dest="key", help="key (./key.pem)")
        #parser.add_option("--ver", default=ssl.PROTOCOL_TLSv1, type=int, action="store", dest="ver", help="ssl version")

        (options, args) = parser.parse_args()

        cls = SimpleEcho
        if options.example == 'chat':
          cls = SimpleChat

        if options.ssl == 1:
           server = SimpleSSLWebSocketServer(options.host, options.port, cls, options.cert, options.key, version=options.ver)
        else:
           server = SimpleWebSocketServer(options.host, options.port, cls)

        def close_sig_handler(signal, frame):
           server.close()
           sys.exit()

        #signal.signal(signal.SIGINT, close_sig_handler)

        server.serveforever()

class internet_Test():
    def __init__(self):
        pass

    def run(self):
        try:
            urllib.request.urlopen('http://216.58.192.142', timeout=1)
            #print( "True")
            return True
        except urllib.error.URLError as err:
            #print( "False")
            return False

class WanIPCheck():
    def __init__(self):
        pass
    def runCheck(self):
        #Check for WAN IP address
        url = "http://checkip.dyndns.org"
        #print( url)
        request = urllib.request.urlopen(url).read()
        #print( request)

        # theIP = re.findall(r'[0-9]+(?:\.[0-9]+){3}', request)
        # theIP = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', request)
        theIP = [[],[]];
        print( "your IP Address is: ",  theIP)

        return theIP[0]

class LanIP():
    def __init__(self):
        pass

    def run(self):
        Ip = ""
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        Ip = (s.getsockname()[0])
        s.close()
        return  Ip


#---------------------Repeated Classes-----------------------#
class QueryRelayStatus():
    def __init__(self):
        global relayMSG
        global Relays
        global RelayID
        global RelayNames

        #relayMSG = RelayID + ": STATUS?"

        if (len(RelayNames) >= 1):
                relayMSG = RelayID + ": STATUS?" #Check status of relays

class EveryHour():
    def __init__(self):
        global DebugText

        #---------------EVENTS TO OCCUR EVERY HOUR--------------------#
        print( "Hour recording to file")
        DebugText += "Hour recording to file \n"
        makeGraphData()   #Run class to parse data for website graphing files
        webScrape()       #Run class to parse data for 7 day forcast
        getTime()         #Run class for time stamping
        QueryRelayStatus()#Query relay status
        #---------------EVENTS TO OCCUR EVERY HOUR--------------------#






app = GUI()
app.mainloop()



