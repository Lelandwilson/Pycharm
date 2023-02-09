Version =  "2.2"
print("Version: "+ Version)
import serial
import sys
import time
from sys import platform as _platform
import threading
import glob
import re
import datetime
from datetime import timedelta
import os
from decimal import *
import json
from ast import literal_eval
from flask import Flask, render_template, jsonify, request, flash, redirect, url_for, session
import socket
import random
# from flask_wtf import FlaskForm
# from wtforms import StringField, PasswordField, BooleanField, SubmitField
# from wtforms.validators import DataRequired, Email
# from wtforms import validators, ValidationError

from settings_form import SettingsForm1, SettingsForm2, SettingsForm3, SettingsForm4, SettingsForm5, SettingsForm6,\
    SettingsForm7, SettingsForm8, SettingsForm9, SettingsForm10, NetworkForm


 # Test settings #
Local = False    #only true for testing
Test = False      #only true for testing
if Local == True:
    print("<Hosting Local Server: 127.0.0.1>")

if Test == True:
    print("<Test Data Activated>")
 #---------------#

LoadData = False
Debug = False
Debug_computeVals = False

Voltage = 240
PowerFactor = 1

Interface = ''
IPaddress = ""
Port = 5000
Router = ''
DNS = ''
SSID = ''
Password = ''


Settings_File = 'Settings.txt'
UserList = []
UsersFile = "setup/Users.txt"
FaildLogins = []

displayMax_Sensors = 14
# Boolchecktime = False
# Boolcheckhour = False

Tsec = 0
pastsec = 0

Thour = 0
pasthour = Thour

Tday = ''
pastday = Tday

Tweek = ''
pastweek = Tweek

TdayofWeek = ''
pastDayofWeek = TdayofWeek

Tmonth = ''
pastmonth = Tmonth

Tseason = ''
pastseason = Tseason

Tyear = ''
pastyear = Tyear


ParallelThread = False
Tminute = 0
pastminute = Tminute

UnitNo = 0  #DO NOT CHANGE, this will auto update to the correct no of units

baudRate = 115200



Ufile_list = ["","U1_data.txt","U2_data.txt","U3_data.txt","U4_data.txt","U5_data.txt","U6_data.txt","U7_data.txt",
              "U8_data.txt","U9_data.txt","U10_data.txt"]


UnitValues = []

UnitVal_1 = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
UnitVal_2 = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
UnitVal_3 = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
UnitVal_4 = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
UnitVal_5 = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
UnitVal_6 = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
UnitVal_7 = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
UnitVal_8 = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
UnitVal_9 = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
UnitVal_10 = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]

HrAve_U1 = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
HrAve_U2 = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
HrAve_U3 = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
HrAve_U4 = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
HrAve_U5 = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
HrAve_U6 = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
HrAve_U7 = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
HrAve_U8 = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
HrAve_U9 = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
HrAve_U10 = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]

DayAve_U1 = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
DayAve_U2 = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
DayAve_U3 = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
DayAve_U4 = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
DayAve_U5 = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
DayAve_U6 = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
DayAve_U7 = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
DayAve_U8 = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
DayAve_U9 = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
DayAve_U10 = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]

WeekAve_U1 = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
WeekAve_U2 = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
WeekAve_U3 = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
WeekAve_U4 = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
WeekAve_U5 = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
WeekAve_U6 = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
WeekAve_U7 = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
WeekAve_U8 = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
WeekAve_U9 = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
WeekAve_U10 = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]

MonthAve_U1 = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
MonthAve_U2 = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
MonthAve_U3 = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
MonthAve_U4 = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
MonthAve_U5 = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
MonthAve_U6 = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
MonthAve_U7 = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
MonthAve_U8 = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
MonthAve_U9 = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
MonthAve_U10 = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]

SeasonAve_U1 = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
SeasonAve_U2 = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
SeasonAve_U3 = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
SeasonAve_U4 = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
SeasonAve_U5 = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
SeasonAve_U6 = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
SeasonAve_U7 = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
SeasonAve_U8 = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
SeasonAve_U9 = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
SeasonAve_U10 = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]

YearAve_U1 = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
YearAve_U2 = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
YearAve_U3 = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
YearAve_U4 = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
YearAve_U5 = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
YearAve_U6 = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
YearAve_U7 = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
YearAve_U8 = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
YearAve_U9 = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
YearAve_U10 = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]

unit_hour_WriteVals =[[False,False,False,False,False,False,False,False,False,False,False,False,False,False,False],
                      [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False],
                      [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False],
                      [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False],
                      [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False],
                      [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False],
                      [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False],
                      [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False],
                      [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False],
                      [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]]

unit_day_WriteVals =[[False,False,False,False,False,False,False,False,False,False,False,False,False,False,False],
                      [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False],
                      [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False],
                      [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False],
                      [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False],
                      [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False],
                      [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False],
                      [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False],
                      [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False],
                      [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]]

unit_week_WriteVals =[[False,False,False,False,False,False,False,False,False,False,False,False,False,False,False],
                      [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False],
                      [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False],
                      [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False],
                      [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False],
                      [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False],
                      [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False],
                      [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False],
                      [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False],
                      [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]]

unit_month_WriteVals =[[False,False,False,False,False,False,False,False,False,False,False,False,False,False,False],
                      [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False],
                      [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False],
                      [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False],
                      [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False],
                      [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False],
                      [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False],
                      [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False],
                      [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False],
                      [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]]

unit_year_WriteVals =[[False,False,False,False,False,False,False,False,False,False,False,False,False,False,False],
                      [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False],
                      [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False],
                      [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False],
                      [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False],
                      [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False],
                      [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False],
                      [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False],
                      [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False],
                      [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]]


G_Units = [1,2,3,4,5,6,7,8,9,10]
U1_SaveFlag = False
U2_SaveFlag = False
U3_SaveFlag = False
U4_SaveFlag = False
U5_SaveFlag = False
U6_SaveFlag = False
U7_SaveFlag = False
U8_SaveFlag = False
U9_SaveFlag = False
U10_SaveFlag = False


 #----------***!!!Adjust below for new models!!!***--------------#
ActiveSensor = [
    [],   #Zero
    [True,True,False,True,True,True,True,True,True,True,True,True,True,True],     #Unit 1
    [True,True,True,True,True,True,True,True,False,True,True,True,True,True],     #Unit 2
    [True,True,True,True,True,True,True,True,True,True,True,True,True,True],      #Unit 3
    [False,True,True,True,True,False,True,True,True,True,True,True,True,True],    #Unit 4
    [False,False,True,True,True,True,True,False,True,True,True,True,True,False],  #Unit 5
    [True,True,True,True,True,True,True,True,True,True,True,True,True,True],      #Unit 6
    [True,True,True,True,True,True,True,True,True,True,True,True,True,True],      #Unit 7
    [True,True,True,True,True,True,True,True,True,True,True,True,True,True],      #Unit 8
    [True,True,True,True,True,True,True,True,True,True,True,True,True,True],      #Unit 9
    [True,True,True,True,True,True,True,True,True,True,True,True,True,True],      #Unit 10
]

SensorLabels = [
    [],   #Zero
    ['','U1S1','U1S2','U1S3','U1S4','U1S5','U1S6','U1S7','U1S8','U1S9','U1S10','U1S11','U1S12','U1S13','U1S14',],   #Unit 1
    ['','U2S1','U2S2','U2S3','U2S4','U2S5','U2S6','U2S7','U2S8','U2S9','U2S10','U2S11','U2S12','U2S13','U2S14',],   #Unit 2
    ['','U3S1','U3S2','U3S3','U3S4','U3S5','U3S6','U3S7','U3S8','U3S9','U3S10','U3S11','U3S12','U3S13','U3S14',],   #Unit 3
    ['','U4S1','U4S2','U4S3','U4S4','U4S5','U4S6','U4S7','U4S8','U4S9','U4S10','U4S11','U4S12','U4S13','U4S14',],   #Unit 4
    ['','U5S1','U5S2','U5S3','U5S4','U5S5','U5S6','U5S7','U5S8','U5S9','U5S10','U5S11','U5S12','U5S13','U5S14',],   #Unit 5
    ['','U6S1','U6S2','U6S3','U6S4','U6S5','U6S6','U6S7','U6S8','U6S9','U6S10','U6S11','U6S12','U6S13','U6S14',],   #Unit 6
    ['','U7S1','U7S2','U7S3','U7S4','U7S5','U7S6','U7S7','U7S8','U7S9','U7S10','U7S11','U7S12','U7S13','U7S14',],   #Unit 7
    ['','U8S1','U8S2','U8S3','U8S4','U8S5','U8S6','U8S7','U8S8','U8S9','U8S10','U8S11','U8S12','U8S13','U8S14',],   #Unit 8
    ['','U9S1','U9S2','U9S3','U9S4','U9S5','U9S6','U9S7','U9S8','U9S9','U9S10','U9S11','U9S12','U9S13','U9S14',],   #Unit 9
    ['','U10S1','U10S2','U10S3','U10S4','U10S5','U10S6','U10S7','U10S8','U10S9','U10S10','U10S11','U10S12','U10S13','U10S14',],   #Unit 10
]


# ["hourReadig"["UnitX"["SensorX"["SXreading1","S1reading2","S1reading3","S1reading4","S1reading5"]
HourReading = [[[[]]]] # [[[["S1reading1","S1reading2","S1reading3","S1reading4","S1reading5"]]]]


averageReadings = 0

class serach4serial(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        #print ("<Search4serial Init>")
        serialPort = ''
        if _platform == "linux" or _platform == "linux2":
            # linux
            #Locate Serial Port to use
            USBList1 = glob.glob('/dev/*')

            for matching in [s for s in USBList1 if "ACM" in s or "USB" in s]:   #32u4
                # if (len(matching)) <1:
                #     matching = [s for s in USBList1 if "USB0" in s]
                serialPort = str(matching)
                serialPort = serialPort.strip("[]'")
                print ("-------->"+serialPort)
                try:
                    t1 = threading.Thread(target =ReadSerial, args=(serialPort,))
                    # t1.daemon = True
                    t1.start()


                except:
                    print ("<Error starting serial thread>")


                else:
                    pass


        elif _platform == "darwin":
            # OS X
            #Locate Serial Port to use
            USBList1 = glob.glob('/dev/cu.*')
            print("USB Devices: "+ str(USBList1))
            #/dev/tty.wchusbserial1420

            for matching in [s for s in USBList1 if "usbmodem" in s or "usbserial1420" in s]:

            #matching = [s for s in USBList1 if "usbmodem" in s]

                serialPort = str(matching)
                serialPort = serialPort.strip("[]'")
                print ("-------->"+serialPort)
                try:
                    t1 = threading.Thread(target =ReadSerial, args=(serialPort,))
                    # t1.daemon = True
                    t1.start()


                except:
                    print ("<Error starting serial thread>")


                else:
                    pass


class ReadSerial(threading.Thread):
    def __init__(self,serialPort):
        threading.Thread.__init__(self)
        global baudRate
        global UnitValues
        global UnitNo
        global Debug
        global pasthour
        global Thour
        #lel# pasthour = Thour
        with serial.Serial(serialPort, baudRate, timeout=1) as ser:
            Sdevice = str(serialPort)
            ondex1 = Sdevice.find('.')+1
            device = Sdevice[ondex1:]
            output = ''
            if Debug == True:
                print ("<ReadSerial Init["+ device +"]>")

            UnitValues.insert(UnitNo,[])
            if Debug == True:
                print("UnitValues "+str(UnitNo)+": "+str(UnitValues))
            self.thisUnit = UnitNo
            UnitNo += 1


            while True:
                line = ser.readline()
                if len(line) >0:
                    output += str(line)
                    if '\\n' in output:
                        output = output.strip("b")
                        output = re.sub("\'b", '', output)
                        output = re.sub("'", '', output)
                        output = re.sub("\\\\", '', output)
                        output = re.sub("rn", '', output)
                        # output = device + ": "+ output

                        #print("<input>" + output)
                        computeVals(self.thisUnit,output,device)
                        output = ''


class computeVals():

    def __init__(self,UnitNo,Instring,device):
        global Thour
        global pasthour
        global Tminute
        global pastminute
        global Tsec

        global UnitValues
        global UnitVal_1
        global UnitVal_2
        global UnitVal_3
        global UnitVal_4
        global UnitVal_5
        global UnitVal_6
        global UnitVal_7
        global UnitVal_8
        global UnitVal_9
        global UnitVal_10

        global HrAve_U1
        global HrAve_U2
        global HrAve_U3
        global HrAve_U4
        global HrAve_U5
        global HrAve_U6
        global HrAve_U7
        global HrAve_U8
        global HrAve_U9
        global HrAve_U10

        global DayAve_U1
        global DayAve_U2
        global DayAve_U3
        global DayAve_U4
        global DayAve_U5
        global DayAve_U6
        global DayAve_U7
        global DayAve_U8
        global DayAve_U9
        global DayAve_U10

        global WeekAve_U1
        global WeekAve_U2
        global WeekAve_U3
        global WeekAve_U4
        global WeekAve_U5
        global WeekAve_U6
        global WeekAve_U7
        global WeekAve_U8
        global WeekAve_U9
        global WeekAve_U10

        global MonthAve_U1
        global MonthAve_U2
        global MonthAve_U3
        global MonthAve_U4
        global MonthAve_U5
        global MonthAve_U6
        global MonthAve_U7
        global MonthAve_U8
        global MonthAve_U9
        global MonthAve_U10

        global SeasonAve_U1
        global SeasonAve_U2
        global SeasonAve_U3
        global SeasonAve_U4
        global SeasonAve_U5
        global SeasonAve_U6
        global SeasonAve_U7
        global SeasonAve_U8
        global SeasonAve_U9
        global SeasonAve_U10

        global YearAve_U1
        global YearAve_U2
        global YearAve_U3
        global YearAve_U4
        global YearAve_U5
        global YearAve_U6
        global YearAve_U7
        global YearAve_U8
        global YearAve_U9
        global YearAve_U10

        global unit_hour_WriteVals
        global unit_day_WriteVals
        global unit_week_WriteVals
        global unit_month_WriteVals
        global unit_year_WriteVals

        global Debug
        global Debug_computeVals
        global HourReading



        def everyminute(Unit_no,Sensor_no,UnitVal_X,HrAve_X,DayAve_X,WeekAve_X,MonthAve_X,SeasonAve_X,YearAve_X):

            global Tsec
            global Tminute
            global pastminute
            global Thour
            global pasthour
            global Tweek
            global pastweek
            global Tmonth
            global pastmonth
            global Tyear
            global pastyear

            global Debug

            global U1_SaveFlag
            global U2_SaveFlag
            global U3_SaveFlag
            global U4_SaveFlag
            global U5_SaveFlag
            global U6_SaveFlag
            global U7_SaveFlag
            global U8_SaveFlag
            global U9_SaveFlag
            global U10_SaveFlag

            global Ufile_list
            # print(Unit_no, Sensor_no, UnitVal_X)

            #---- Intra minute readings averaged to average minute readings per unit, per sensor ----#
            if pastminute != Tminute:   # Minute to hour average convsion
                # print(str(Unit_no),str(Sensor_no), str(UnitVal_X))
                x = 0
                total = 0
                for n in UnitVal_X:
                    if (len(n)>0):
                        try:
                            x += float(n)
                        except:
                            x += 0
                        total += 1

                if (total>0.1):
                    val = round(x / total,2) # Get sensor average minute value and append to hour
                    HrAve_X.append(val)
                    # print(str(Unit_no),str(Sensor_no),str(HrAve_X))

                else:
                    HrAve_X.append(0)

                if len(HrAve_X) >60:
                    HrAve_X.pop(0)

                UnitVal_X.clear()   #clear 5 second readings
                # print ("Clear: " +str(HrAve_X[0]))

            #---- Intra hour readings to averaged hour readings ----#
            if pasthour != Thour: # Hour to day sum total convsion
            # if averageReadings == 2:
                if (unit_hour_WriteVals[Unit_no][Sensor_no] == False): #once per hour
                    # print(str(Unit_no) + ": Intra hour(5)" )
                    x = 0
                    total = 0
                    for n in HrAve_X:
                        if (isinstance(n, (int, float))):
                            x += n
                            total +=1
                    if (total>0):                   #----- We want average hour value -----#
                        val = round(x / total,2)# Get sensor average hour value and append to day
                        DayAve_X.append(val)
                        if (Debug_computeVals == True):
                            print("intra day: "+str(Unit_no)+","+str(Sensor_no) +" : "+ str(DayAve_X))

                    else:
                        DayAve_X.append(0)

                    if len(DayAve_X)>24:
                        DayAve_X.pop(0)

                    unit_hour_WriteVals[Unit_no][Sensor_no] = True


                    # print(unit_hour_WriteVals[Unit_no][Sensor_no])

            # #---- Collect hour readings and sum total for day total readings ----#
            if pastday != Tday:   # Day to week sum total convsion
            # if averageReadings == 3:
                if (unit_day_WriteVals[Unit_no][Sensor_no] == False):
                    # print(str(Unit_no) + ": Intra day(10)" )
                    val = 0
                    for x ,y in enumerate(DayAve_X):
                        if (isinstance(y, (int, float))):
                            # val = round(x / len(DayAve_X),2) #----- We want sum total day value -----#
                            val += y   #get sensor day value add up total and and append to week
                            val = round(val,2)

                        else:
                            val += 0

                    #WeekAve_X.insert(0,val)
                    WeekAve_X.append(val)
                    if (Debug_computeVals == True):
                        print("intra week: "+str(Unit_no) +" : "+ str(WeekAve_X))
                    if len(WeekAve_X)>7:
                        WeekAve_X.pop(0)

                    unit_day_WriteVals[Unit_no][Sensor_no] = True

            # print(Unit_no,Sensor_no,WeekAve_X)

            #- Collect day readings and sum total for week total readings -#

            if pastweek != Tweek:  # Week to month sum total convsion
            # if averageReadings == 4:
                if (unit_week_WriteVals[Unit_no][Sensor_no] == False):
                    # print(str(Unit_no) + ": Week to month(15)" )
                    val = 0
                    for x ,y in enumerate(WeekAve_X):
                        if (isinstance(y, (int, float))):
                            # val = round(x / len(DayAve_X),2)   #----- We want sum total week value -----#
                            val += y   #get sensor day value add up total and and append to week
                            val = round(val,2)

                        else:
                            val += 0

                    #MonthAve_X.insert(0,val)
                    MonthAve_X.append(val)
                    if (Debug_computeVals == True):
                        print("intra month: "+str(Unit_no) +" : "+ str(MonthAve_X))

                    if len(MonthAve_X)>4:
                        MonthAve_X.pop(0)

                    unit_week_WriteVals[Unit_no][Sensor_no] = True


            #- Collect month readings and sum total for year total readings -#
            if pastmonth != Tmonth:  # Month to year sum total convsion
            # if averageReadings == 5:
                if (unit_month_WriteVals[Unit_no][Sensor_no] == False):
                    # print(str(Unit_no) + ": Month to year(20)" )
                    val = 0
                    for x ,y in enumerate(MonthAve_X):
                        if (isinstance(y, (int, float))):
                            # val = round(x / len(DayAve_X),2)   #----- We want sum total month value -----#
                            val += y   #get sensor day value add up total and and append to week
                            val = round(val,2)

                        else:
                            val += 0

                    # print(val)
                    #YearAve_X.insert(0,val)
                    YearAve_X.append(val)
                    if (Debug_computeVals == True):
                        print("intra year: "+str(Unit_no) +" : "+ str(YearAve_X))
                    if len(YearAve_X)>4:
                        YearAve_X.pop(0)

                    unit_month_WriteVals[Unit_no][Sensor_no] = True


            #---\/-----for year to year comparrison----\/------#

            # if pastyear != Tyear:  # Month to year sum total convsion
            # # if averageReadings == 6:
            #     if (unit_year_WriteVals[Unit_no][Sensor_no] == False):
            #         # print(str(Unit_no) + ": year to year(20)" )
            #         val = 0
            #         for x ,y in enumerate(YearAve_X):
            #             if (isinstance(y, (int, float))):
            #                 # val = round(x / len(DayAve_X),2)
            #                 val += y   #get sensor day value add up total and and append to week
            #                 val = round(val,2)
            #
            #             else:
            #                 val += 0
            #
            #         # print(val)
            #         #YearAve_X.insert(0,val)
            #         Past_YearAve_X.append(val)
            #         if (Debug_computeVals == True):
            #             print("Past year: "+str(Unit_no) +" : "+ str(Past_YearAve_X))
            #         if len(YearAve_X)>12:
            #             Past_YearAve_X.pop(0)
            #
            #         unit_year_WriteVals[Unit_no][Sensor_no] = True


          # unitCheck(1,x,UnitVal_1,y,HrAve_U1,DayAve_U1,WeekAve_U1,MonthAve_U1,SeasonAve_U1,YearAve_U1)
        def unitCheck(Unit_no,Sensor_no,Uval,reading,HrAv_X,DayAV_X,WeekAve_X,MonthAve_X,SeasonAve_X,YearAve_X):
            global SensorLabels
            if (SensorLabels[Unit_no][Sensor_no]) != "unused" or  SensorLabels[Unit_no][Sensor_no] != "Unused":
                Uval[Sensor_no].append(reading)

            else:
                Uval[Sensor_no].append("0")

            # print(Unit_no, Sensor_no, Uval[Sensor_no])

            everyminute(Unit_no,Sensor_no,Uval[Sensor_no],HrAv_X[Sensor_no],DayAV_X[Sensor_no],
                        WeekAve_X[Sensor_no],MonthAve_X[Sensor_no],SeasonAve_X[Sensor_no],YearAve_X[Sensor_no])


        self.output = ''
        self.splitData = Instring.split(',')
        for n,i in enumerate(self.splitData):
            if n!=1:
                self.output += i +','


        UnitValues[UnitNo] = self.output
        index1 = self.output.find(",")
        unitRef = self.output[:index1]


        if unitRef == "U1":
            self.currentVals = self.output
            self.currentVals = self.currentVals.split(',')
            for x, y in enumerate(self.currentVals):
                y = y.replace(" ", "")
                if(x >0 and x <15):
                    # print(x)
                    unitCheck(1,x,UnitVal_1,y,HrAve_U1,DayAve_U1,WeekAve_U1,MonthAve_U1,SeasonAve_U1,YearAve_U1)


        elif unitRef == "U2":
            self.currentVals = self.output
            self.currentVals = self.currentVals.split(',')
            for x, y in enumerate(self.currentVals):
                y = y.replace(" ", "")
                if(x >0 and x <15):
                    unitCheck(2,x,UnitVal_2,y,HrAve_U2,DayAve_U2,WeekAve_U2,MonthAve_U2,SeasonAve_U2,YearAve_U2)

        elif unitRef == "U3":
            self.currentVals = self.output
            self.currentVals = self.currentVals.split(',')
            for x, y in enumerate(self.currentVals):
                y = y.replace(" ", "")
                if(x >0 and x <15):
                     unitCheck(3,x,UnitVal_3,y,HrAve_U3,DayAve_U3,WeekAve_U3,MonthAve_U3,SeasonAve_U3,YearAve_U3)

        elif unitRef == "U4":
            self.currentVals = self.output
            self.currentVals = self.currentVals.split(',')
            for x, y in enumerate(self.currentVals):
                y = y.replace(" ", "")
                if(x >0 and x <15):
                     unitCheck(4,x,UnitVal_4,y,HrAve_U4,DayAve_U4,WeekAve_U4,MonthAve_U4,SeasonAve_U4,YearAve_U4)

        elif unitRef == "U5":
            self.currentVals = self.output
            self.currentVals = self.currentVals.split(',')
            for x, y in enumerate(self.currentVals):
                y = y.replace(" ", "")
                if(x >0 and x <15):
                     unitCheck(5,x,UnitVal_5,y,HrAve_U5,DayAve_U5,WeekAve_U5,MonthAve_U5,SeasonAve_U5,YearAve_U5)

        elif unitRef == "U6":
            self.currentVals = self.output
            self.currentVals = self.currentVals.split(',')
            for x, y in enumerate(self.currentVals):
                y = y.replace(" ", "")
                if(x >0 and x <15):
                     unitCheck(6,x,UnitVal_6,y,HrAve_U6,DayAve_U6,WeekAve_U6,MonthAve_U6,SeasonAve_U6,YearAve_U6)

        elif unitRef == "U7":
            self.currentVals = self.output
            self.currentVals = self.currentVals.split(',')
            for x, y in enumerate(self.currentVals):
                y = y.replace(" ", "")
                if(x >0 and x <15):
                     unitCheck(7,x,UnitVal_7,y,HrAve_U7,DayAve_U7,WeekAve_U7,MonthAve_U7,SeasonAve_U7,YearAve_U7)

        elif unitRef == "U8":
            self.currentVals = self.output
            self.currentVals = self.currentVals.split(',')
            for x, y in enumerate(self.currentVals):
                y = y.replace(" ", "")
                if(x >0 and x <15):
                     unitCheck(8,x,UnitVal_8,y,HrAve_U8,DayAve_U8,WeekAve_U8,MonthAve_U8,SeasonAve_U8,YearAve_U8)

        elif unitRef == "U9":
            self.currentVals = self.output
            self.currentVals = self.currentVals.split(',')
            for x, y in enumerate(self.currentVals):
                y = y.replace(" ", "")
                if(x >0 and x <15):
                     unitCheck(9,x,UnitVal_9,y,HrAve_U9,DayAve_U9,WeekAve_U9,MonthAve_U9,SeasonAve_U9,YearAve_U9)

        elif unitRef == "U10":
            self.currentVals = self.output
            self.currentVals = self.currentVals.split(',')
            for x, y in enumerate(self.currentVals):
                y = y.replace(" ", "")
                if(x >0 and x <15):
                     unitCheck(10,x,UnitVal_10,y,HrAve_U10,DayAve_U10,WeekAve_U10,MonthAve_U10,SeasonAve_U10,YearAve_U10)

        if Debug == True:
            print("Data Stream: " + str(UnitValues))   #------------------------Data Stream values printout------------------------#
        if (pastminute != Tminute):

            def tallyListTotal(listX):
                t = 0
                for x,y in enumerate(listX):
                    for i in listX[x]:
                        t +=1

                t = t/14

                return(str(t))

            if Debug == True:
                printString = ("---------------------------\n")

                testX = round(float(tallyListTotal(HrAve_U1)),0)
                if (testX > 0):
                    printString += "|-Unit 1 Hour Readings: " + str(testX) +"\n"
                testX = round(float(tallyListTotal(HrAve_U2)),0)
                if (testX > 0):
                    printString += "|-Unit 2 Hour Readings: " + str(testX)+"\n"
                testX = round(float(tallyListTotal(HrAve_U3)),0)
                if (testX > 0):
                    printString += "|-Unit 3 Hour Readings: " + str(testX) +"\n"
                testX = round(float(tallyListTotal(HrAve_U4)),0)
                if (testX > 0):
                    printString += "|-Unit 4 Hour Readings: " + str(testX) +"\n"
                testX = round(float(tallyListTotal(HrAve_U5)),0)
                if (testX > 0):
                    printString += "|-Unit 5 Hour Readings: " + str(testX) +"\n"
                testX = round(float(tallyListTotal(HrAve_U6)),0)
                if (testX > 0):
                    printString += "|-Unit 6 Hour Readings: " + str(testX) +"\n"
                testX = round(float(tallyListTotal(HrAve_U7)),0)
                if (testX > 0):
                    printString += "|-Unit 7 Hour Readings: " + str(testX) +"\n"
                testX = round(float(tallyListTotal(HrAve_U8)),0)
                if (testX > 0):
                    printString += "|-Unit 8 Hour Readings: " + str(testX) +"\n"
                testX = round(float(tallyListTotal(HrAve_U9)),0)
                if (testX > 0):
                    printString += "|-Unit 9 Hour Readings: " + str(testX) +"\n"
                testX = round(float(tallyListTotal(HrAve_U10)),0)
                if (testX > 0):
                    printString += "|-Unit 10 Hour Readings: " + str(testX) +"\n"
                printString += ("---------------------------")

                print(printString)


        # pastminute = Tminute
        # pasthour = Thour


class parallel(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        print("<Timer Init>")

        global Thour
        global pasthour
        global Tminute

        global Tsec

        global Tday
        global Tmonth
        global Tyear

        global TdayofWeek

        global U1_SaveFlag
        global U2_SaveFlag
        global U3_SaveFlag
        global U4_SaveFlag
        global U5_SaveFlag
        global U6_SaveFlag
        global U7_SaveFlag
        global U8_SaveFlag
        global U9_SaveFlag
        global U10_SaveFlag

        X_dayPast = ''


        initialLoop = True
        while True:
            d = datetime.datetime.today()
            # print(str(d.day)+"/"+str(d.month)+"/"+str(d.year))
            Tsec = d.second
            Tminute = d.minute
            Thour = d.hour
            Tday = str(d.day)+"/"+str(d.month)+"/"+str(d.year)

            if X_dayPast != Tday:
                Tmonth = str(d.month)+"/"+str(d.year)
                Tyear = d.year

                Cday =d.weekday()
                if Cday == 0:
                    TdayofWeek = 'Mon'
                elif Cday == 1:
                    TdayofWeek = 'Tues'
                elif Cday == 2:
                    TdayofWeek = 'Wed'
                elif Cday == 3:
                    TdayofWeek = 'Thur'
                elif Cday == 4:
                    TdayofWeek = 'Fri'
                elif Cday == 5:
                    TdayofWeek = 'Sat'
                elif Cday == 6:
                    TdayofWeek = 'Sun'
                #print ("Hrave5["+str(Tsec)+"]"+str(HrAve_U5))

            if Tminute == 59:
                U1_SaveFlag = False
                U2_SaveFlag = False
                U3_SaveFlag = False
                U4_SaveFlag = False
                U5_SaveFlag = False
                U6_SaveFlag = False
                U7_SaveFlag = False
                U8_SaveFlag = False
                U9_SaveFlag = False
                U10_SaveFlag = False



            if (Thour != pasthour):
                if initialLoop == True:
                    pass
                else:

                    saveFunction()


            time.sleep(1)

            initialLoop = False
            # X_dayPast = Tday
            pasthour = Thour


class saveFunction():
    def __init__(self):
        global U1_SaveFlag
        global U2_SaveFlag
        global U3_SaveFlag
        global U4_SaveFlag
        global U5_SaveFlag
        global U6_SaveFlag
        global U7_SaveFlag
        global U8_SaveFlag
        global U9_SaveFlag
        global U10_SaveFlag

        global Ufile_list

        global HrAve_U1
        global HrAve_U2
        global HrAve_U3
        global HrAve_U4
        global HrAve_U5
        global HrAve_U6
        global HrAve_U7
        global HrAve_U8
        global HrAve_U9
        global HrAve_U10

        global DayAve_U1
        global DayAve_U2
        global DayAve_U3
        global DayAve_U4
        global DayAve_U5
        global DayAve_U6
        global DayAve_U7
        global DayAve_U8
        global DayAve_U9
        global DayAve_U10

        global WeekAve_U1
        global WeekAve_U2
        global WeekAve_U3
        global WeekAve_U4
        global WeekAve_U5
        global WeekAve_U6
        global WeekAve_U7
        global WeekAve_U8
        global WeekAve_U9
        global WeekAve_U10

        global MonthAve_U1
        global MonthAve_U2
        global MonthAve_U3
        global MonthAve_U4
        global MonthAve_U5
        global MonthAve_U6
        global MonthAve_U7
        global MonthAve_U8
        global MonthAve_U9
        global MonthAve_U10

        global SeasonAve_U1
        global SeasonAve_U2
        global SeasonAve_U3
        global SeasonAve_U4
        global SeasonAve_U5
        global SeasonAve_U6
        global SeasonAve_U7
        global SeasonAve_U8
        global SeasonAve_U9
        global SeasonAve_U10

        global YearAve_U1
        global YearAve_U2
        global YearAve_U3
        global YearAve_U4
        global YearAve_U5
        global YearAve_U6
        global YearAve_U7
        global YearAve_U8
        global YearAve_U9
        global YearAve_U10

        global G_units

        global Debug

        print("SaveFunction: Saving Data")
        for Unit_no in G_Units:
            if Unit_no == 1:
                if U1_SaveFlag == False:
                    listFile = Ufile_list[1]
                    X_List = "U1_HrAve = [" + str(HrAve_U1) + "]\n\n"
                    X_List += "U1_DayAve = [" + str(DayAve_U1) + "]\n\n"
                    X_List += "U1_WeekAve = [" + str(WeekAve_U1) + "]\n\n"
                    X_List += "U1_MonthAve = [" + str(MonthAve_U1) + "]\n\n"
                    X_List += "U1_YearAve = [" + str(YearAve_U1) + "]\n\n"

                    Xsave = threading.Thread(target=saveLists, args=(listFile,X_List))
                    Xsave.start()
                    U1_SaveFlag = True
                    # if (Debug == True):
                    print("Saved U1 data")
                    print(X_List)

            elif Unit_no == 2:
                if U2_SaveFlag == False:
                    listFile = Ufile_list[2]
                    X_List = "U2_HrAve = [" + str(HrAve_U2) + "]\n\n"
                    X_List += "U2_DayAve = [" + str(DayAve_U2) + "]\n\n"
                    X_List += "U2_WeekAve = [" + str(WeekAve_U2) + "]\n\n"
                    X_List += "U2_MonthAve = [" + str(MonthAve_U2) + "]\n\n"
                    X_List += "U2_YearAve = [" + str(YearAve_U2) + "]\n\n"

                    Xsave = threading.Thread(target=saveLists, args=(listFile,X_List))
                    Xsave.start()
                    U2_SaveFlag = True
                    if (Debug == True):
                        print("Saved U2 data")

            elif Unit_no == 3:
                if U3_SaveFlag == False:
                    listFile = Ufile_list[3]
                    X_List = "U3_HrAve = [" + str(HrAve_U3) + "]\n\n"
                    X_List += "U3_DayAve = [" + str(DayAve_U3) + "]\n\n"
                    X_List += "U3_WeekAve = [" + str(WeekAve_U3) + "]\n\n"
                    X_List += "U3_MonthAve = [" + str(MonthAve_U3) + "]\n\n"
                    X_List += "U3_YearAve = [" + str(YearAve_U3) + "]\n\n"

                    Xsave = threading.Thread(target=saveLists, args=(listFile,X_List))
                    Xsave.start()
                    U3_SaveFlag = True
                    if (Debug == True):
                        print("Saved U3 data")

            elif Unit_no == 4:
                if U4_SaveFlag == False:
                    listFile = Ufile_list[4]
                    X_List = "U4_HrAve = [" + str(HrAve_U4) + "]\n\n"
                    X_List += "U4_DayAve = [" + str(DayAve_U4) + "]\n\n"
                    X_List += "U4_WeekAve = [" + str(WeekAve_U4) + "]\n\n"
                    X_List += "U4_MonthAve = [" + str(MonthAve_U4) + "]\n\n"
                    X_List += "U4_YearAve = [" + str(YearAve_U4) + "]\n\n"

                    Xsave = threading.Thread(target=saveLists, args=(listFile,X_List))
                    Xsave.start()
                    U4_SaveFlag = True
                    if (Debug == True):
                        print("Saved U4 data")

            elif Unit_no == 5:
                if U5_SaveFlag == False:
                    listFile = Ufile_list[5]
                    X_List = "U5_HrAve = [" + str(HrAve_U5) + "]\n\n"
                    X_List += "U5_DayAve = [" + str(DayAve_U5) + "]\n\n"
                    X_List += "U5_WeekAve = [" + str(WeekAve_U5) + "]\n\n"
                    X_List += "U5_MonthAve = [" + str(MonthAve_U5) + "]\n\n"
                    X_List += "U5_YearAve = [" + str(YearAve_U5) + "]\n\n"

                    Xsave = threading.Thread(target=saveLists, args=(listFile,X_List))
                    Xsave.start()
                    U5_SaveFlag = True
                    if (Debug == True):
                        print("Saved U5 data")

            elif Unit_no == 6:
                if U6_SaveFlag == False:
                    listFile = Ufile_list[6]
                    X_List = "U6_HrAve = [" + str(HrAve_U6) + "]\n\n"
                    X_List += "U6_DayAve = [" + str(DayAve_U6) + "]\n\n"
                    X_List += "U6_WeekAve = [" + str(WeekAve_U6) + "]\n\n"
                    X_List += "U6_MonthAve = [" + str(MonthAve_U6) + "]\n\n"
                    X_List += "U6_YearAve = [" + str(YearAve_U6) + "]\n\n"

                    Xsave = threading.Thread(target=saveLists, args=(listFile,X_List))
                    Xsave.start()
                    U6_SaveFlag = True
                    if (Debug == True):
                        print("Saved U6 data")

            elif Unit_no == 7:
                if U7_SaveFlag == False:
                    listFile = Ufile_list[7]
                    X_List = "U7_HrAve = [" + str(HrAve_U7) + "]\n\n"
                    X_List += "U7_DayAve = [" + str(DayAve_U7) + "]\n\n"
                    X_List += "U7_WeekAve = [" + str(WeekAve_U7) + "]\n\n"
                    X_List += "U7_MonthAve = [" + str(MonthAve_U7) + "]\n\n"
                    X_List += "U7_YearAve = [" + str(YearAve_U7) + "]\n\n"

                    Xsave = threading.Thread(target=saveLists, args=(listFile,X_List))
                    Xsave.start()
                    U7_SaveFlag = True
                    if (Debug == True):
                        print("Saved U7 data")

            elif Unit_no == 8:
                if U8_SaveFlag == False:
                    listFile = Ufile_list[8]
                    X_List = "U8_HrAve = [" + str(HrAve_U8) + "]\n\n"
                    X_List += "U8_DayAve = [" + str(DayAve_U8) + "]\n\n"
                    X_List += "U8_WeekAve = [" + str(WeekAve_U8) + "]\n\n"
                    X_List += "U8_MonthAve = [" + str(MonthAve_U8) + "]\n\n"
                    X_List += "U8_YearAve = [" + str(YearAve_U8) + "]\n\n"

                    Xsave = threading.Thread(target=saveLists, args=(listFile,X_List))
                    Xsave.start()
                    U8_SaveFlag = True
                    if (Debug == True):
                        print("Saved U8 data")

            elif Unit_no == 9:
                if U9_SaveFlag == False:
                    listFile = Ufile_list[9]
                    X_List = "U9_HrAve = [" + str(HrAve_U9) + "]\n\n"
                    X_List += "U9_DayAve = [" + str(DayAve_U9) + "]\n\n"
                    X_List += "U9_WeekAve = [" + str(WeekAve_U9) + "]\n\n"
                    X_List += "U9_MonthAve = [" + str(MonthAve_U9) + "]\n\n"
                    X_List += "U9_YearAve = [" + str(YearAve_U9) + "]\n\n"

                    Xsave = threading.Thread(target=saveLists, args=(listFile,X_List))
                    Xsave.start()
                    U9_SaveFlag = True
                    if (Debug == True):
                        print("Saved U9 data")

            elif Unit_no == 10:
                if U10_SaveFlag == False:
                    listFile = Ufile_list[10]
                    X_List = "U10_HrAve = [" + str(HrAve_U10) + "]\n\n"
                    X_List += "U10_DayAve = [" + str(DayAve_U10) + "]\n\n"
                    X_List += "U10_WeekAve = [" + str(WeekAve_U10) + "]\n\n"
                    X_List += "U10_MonthAve = [" + str(MonthAve_U10) + "]\n\n"
                    X_List += "U10_YearAve = [" + str(YearAve_U10) + "]\n\n"

                    Xsave = threading.Thread(target=saveLists, args=(listFile,X_List))
                    Xsave.start()
                    U10_SaveFlag = True
                    if (Debug == True):
                        print("Saved U10 data")


class webserver():

    def __init__(self):

        app = Flask(__name__)
        # app.secret_key = 'development key'
        app.config['SECRET_KEY'] = '7cce7410e80ce3f326f2b00e7edffee8'

        @app.route('/')
        def home():
            global Test
            if not session.get('logged_in'):
                return render_template('login.html')
            else:
                Msg = ''
                if Test == True:
                    Msg = "Please Note: Test mode active. Values are not real"

                return render_template('main.html',sys_MSG=Msg)


        @app.route('/login', methods=['POST'])
        def do_admin_login():
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


        @app.route('/hour_data')
        def hour_data():
            global Debug
            global SensorLabels
            global Tminute
            global Thour
            global Tday
            global IPaddress
            global Port

            #####----------------Hr Line & Pie Graph Data---------------#####

            HrCompareList=[[],HrAve_U1,HrAve_U2,HrAve_U3,HrAve_U4,HrAve_U5,
               HrAve_U6,HrAve_U7,HrAve_U8,HrAve_U9,HrAve_U10,]
            # print("------------------Hr compare list------------------")
            # print(HrCompareList)

            #Create list of individual Sensors with highest 14 readings:
            runCompare = findHighestReadings()
            orderedList = runCompare.run(HrCompareList) # Returns Ordered List [[Unit,Sensor,AverageReading], ]
            # print(orderedList)
            if Debug == True:
                print("------------------Hr Ordered List------------------")
                print(orderedList)

            #Generate Legend Lables and readngs for top 14 ------------------#
            HrAveLegend_Lables = []
            displayData = []
            pieLables = []
            pieData = []
            pieData.clear()
            pieLables.clear()
            for i in orderedList:
                UnitX = i[0]   # Unit
                SensorX = i[1]  # Sensor
                ReadX = i[2]    #Reading

                if (str(SensorLabels[UnitX][SensorX]) == 'unused' or str(SensorLabels[UnitX][SensorX]) == 'Unused'):
                    pass

                else:
                    pieLables.append(SensorLabels[UnitX][SensorX])
                    pieData.append(ReadX)

                    HrAveLegend_Lables.append(SensorLabels[UnitX][SensorX])
                    displayData.append(HrCompareList[UnitX][SensorX])
                    while(len(HrCompareList[UnitX][SensorX])<60):
                        # HrCompareList[UnitX][SensorX].append('0')       #Append to end
                        HrCompareList[UnitX][SensorX].insert(0,'0')   #Append to start

                    if len(HrCompareList[UnitX][SensorX])>60:
                        HrCompareList[UnitX][SensorX].pop(0)

            #Generate X axis lables in time strings ---------------------#
            try:
                xLength = len(displayData[0])
            except:
                xLength = 1
            PastMinutesList = []


            for i in range(xLength):
                pastHour = Thour

                pastMin = Tminute-i
                if pastMin < 0:
                    pastMin+=60

                    pastHour -= 1
                    if pastHour < 1:
                        pastHour+=12

                if pastMin == 0 or pastMin == 10 or pastMin == 20 or pastMin == 30 or pastMin == 40 or pastMin == 50:
                    PastMinutesList.append(str(pastHour)+":"+str(pastMin))
                else:
                    PastMinutesList.append("  ")


                if (len(PastMinutesList)>60):
                    # print("Pop[" + str(PastMinutesList[0] + "]"))
                    PastMinutesList.pop(0)
            #print (PastMinutesList)
            Xlabels = PastMinutesList[::-1]  #reverse the list
            #####-------^--------Hr Line & Pie Graph Data---------^-----#####


            return jsonify({'data' : displayData, 'names' : HrAveLegend_Lables, 'Xlabels': Xlabels,
                            'pieData':pieData, 'pieLables': pieLables})


        @app.route('/day_data')
        def day_data():
            global SensorLabels
            global Tminute
            global Thour
            global Tday
            # global IPaddress
            # global Port

                        #####----------------Day Line & Pie Graph Data---------------#####

            DayCompareList=[[],DayAve_U1,DayAve_U2,DayAve_U3,DayAve_U4,DayAve_U5,
               DayAve_U6,DayAve_U7,DayAve_U8,DayAve_U9,DayAve_U10,]

            # print(DayCompareList)

            #Create list of individual Sensors with highest 14 readings:
            runCompare_Day = findHighestReadings()
            Day_orderedList = runCompare_Day.run(DayCompareList) # Returns Ordered List [[Unit,Sensor,AverageReading], ]
            if Debug == True:
                print("------------------Day Ordered List------------------")
                print(Day_orderedList)

            #Generate Legend Lables and readngs for top 14
            Day_AveLegend_Lables = []
            Day_displayData = []
            Day_pieLables = []
            Day_pieData = []
            Day_pieData.clear()
            Day_pieLables.clear()
            for i in Day_orderedList:
                # print (i)
                Day_UnitX = i[0]   # Unit
                Day_SensorX = i[1]  # Sensor
                Day_ReadX = i[2]

                if (str(SensorLabels[Day_UnitX][Day_SensorX]) == 'unused' or str(SensorLabels[Day_UnitX][Day_SensorX]) == 'Unused'):
                    pass

                else:
                    Day_pieLables.append(SensorLabels[Day_UnitX][Day_SensorX])
                    Day_pieData.append(Day_ReadX)

                    Day_AveLegend_Lables.append(SensorLabels[Day_UnitX][Day_SensorX])
                    Day_displayData.append(DayCompareList[Day_UnitX][Day_SensorX])

                    while(len(DayCompareList[Day_UnitX][Day_SensorX])<24):
                        DayCompareList[Day_UnitX][Day_SensorX].insert(0,'0')   #Append to start

                    if len(DayCompareList[Day_UnitX][Day_SensorX])>24:
                        DayCompareList[Day_UnitX][Day_SensorX].pop(0)

            #Generate X axis lables in time strings
            try:
                xLength = len(Day_displayData[0])
            except:
                xLength = 1
            PastDayList = []

            for i in range(xLength):
                pastHour = Thour-i
                if pastHour < 0:
                    pastHour = 24 + pastHour

                # pastHour -= 1
                # if pastHour < 1:
                #     pastHour+=12

                PastDayList.append(str(pastHour)+":00")

                if (len(PastDayList)>24):
                    PastDayList.pop(0)

            Day_Xlabels = PastDayList[::-1]  #reverse the list

            return jsonify({'Day_data' : Day_displayData, 'Day_names' : Day_AveLegend_Lables, 'Day_Xlabels': Day_Xlabels,
                            'Day_pieData':Day_pieData, 'Day_pieLables': Day_pieLables})


        @app.route('/week_data')
        def week_data():
            global SensorLabels
            global Tminute
            global Thour
            global Tday

                        #####----------------Week Line & Pie Graph Data---------------#####

            WeekCompareList=[[],WeekAve_U1,WeekAve_U2,WeekAve_U3,WeekAve_U4,WeekAve_U5,
               WeekAve_U6,WeekAve_U7,WeekAve_U8,WeekAve_U9,WeekAve_U10,]

            # print(DayCompareList)

            #Create list of individual Sensors with highest 14 readings:
            runCompare_Week = findHighestReadings()
            Week_orderedList = runCompare_Week.run(WeekCompareList) # Returns Ordered List [[Unit,Sensor,AverageReading], ]
            if Debug == True:
                print("------------------Week Ordered List------------------")
                print(Week_orderedList)


            #Generate Legend Lables and readngs for top 14
            Week_AveLegend_Lables = []
            Week_displayData = []
            Week_pieLables = []
            Week_pieData = []
            Week_pieData.clear()
            Week_pieLables.clear()
            for i in Week_orderedList:
                # print (i)
                Week_UnitX = i[0]   # Unit
                Week_SensorX = i[1]  # Sensor
                Week_ReadX = i[2]

                if (str(SensorLabels[Week_UnitX][Week_SensorX]) == 'unused' or str(SensorLabels[Week_UnitX][Week_SensorX]) == 'Unused'):
                    pass

                else:
                    Week_pieLables.append(SensorLabels[Week_UnitX][Week_SensorX])
                    Week_pieData.append(Week_ReadX)

                    Week_AveLegend_Lables.append(SensorLabels[Week_UnitX][Week_SensorX])
                    Week_displayData.append(WeekCompareList[Week_UnitX][Week_SensorX])

                    while(len(WeekCompareList[Week_UnitX][Week_SensorX])<7):
                        WeekCompareList[Week_UnitX][Week_SensorX].insert(0,'0')   #Append to start

                    if len(WeekCompareList[Week_UnitX][Week_SensorX])>7:
                        WeekCompareList[Week_UnitX][Week_SensorX].pop(0)


            #Generate X axis lables in time strings
            try:
                xLength = len(Week_displayData[0])
            except:
                xLength = 1
            PastWeekList = []


            for i in range(xLength):
                d = datetime.datetime.today()
                Xday = d - timedelta(days=(i))
                # print(Xday.day, Xday.month)
                pastweek = str(Xday.day) +"/"+ str(Xday.month)

                PastWeekList.append(pastweek)
            #print (PastMinutesList)
            Week_Xlabels = PastWeekList[::-1]  #reverse the list

            return jsonify({'Week_data' : Week_displayData, 'Week_names' : Week_AveLegend_Lables, 'Week_Xlabels': Week_Xlabels,
                'Week_pieData':Week_pieData, 'Week_pieLables': Week_pieLables})


        @app.route('/month_data')
        def month_data():
            global SensorLabels
            global Tminute
            global Thour
            global Tday

                        #####----------------Month Line & Pie Graph Data---------------#####

            MonthCompareList=[[],MonthAve_U1,MonthAve_U2,MonthAve_U3,MonthAve_U4,MonthAve_U5,
               MonthAve_U6,MonthAve_U7,MonthAve_U8,MonthAve_U9,MonthAve_U10,]

            # print(DayCompareList)

            #Create list of individual Sensors with highest 14 readings:
            runCompare_Month = findHighestReadings()
            Month_orderedList = runCompare_Month.run(MonthCompareList) # Returns Ordered List [[Unit,Sensor,AverageReading], ]
            # if Debug == True:
            #     print("------------------Month Ordered List------------------")
            #     print(Month_orderedList)


            #Generate Legend Lables and readngs for top 14
            Month_AveLegend_Lables = []
            Month_displayData = []
            Month_pieLables = []
            Month_pieData = []
            Month_pieData.clear()
            Month_pieLables.clear()
            for i in Month_orderedList:
                # print (i)
                Month_UnitX = i[0]   # Unit
                Month_SensorX = i[1]  # Sensor
                Month_ReadX = i[2]

                if (str(SensorLabels[Month_UnitX][Month_SensorX]) == 'unused' or str(SensorLabels[Month_UnitX][Month_SensorX]) == 'Unused'):
                    pass

                else:
                    Month_pieLables.append(SensorLabels[Month_UnitX][Month_SensorX])
                    Month_pieData.append(Month_ReadX)

                    Month_AveLegend_Lables.append(SensorLabels[Month_UnitX][Month_SensorX])
                    Month_displayData.append(MonthCompareList[Month_UnitX][Month_SensorX])

                    while(len(MonthCompareList[Month_UnitX][Month_SensorX])<4):
                        MonthCompareList[Month_UnitX][Month_SensorX].insert(0,'0')   #Append to start

                    if len(MonthCompareList[Month_UnitX][Month_SensorX])>4:
                        MonthCompareList[Month_UnitX][Month_SensorX].pop(0)


            #Generate X axis lables in time strings
            try:
                xLength = len(Month_displayData[0])
            except:
                xLength = 1
            PastMonthList = []

            for i in range(xLength):
                d = datetime.datetime.today()
                Xday = d - timedelta(days=(i*30))
                # print(Xday.day, Xday.month)
                pastmonth = str(Xday.day) +"/"+ str(Xday.month)

                PastMonthList.append(pastmonth)
            #print (PastMinutesList)
            Month_Xlabels = PastMonthList[::-1]  #reverse the list

            return jsonify({'Month_data' : Month_displayData, 'Month_names' : Month_AveLegend_Lables, 'Month_Xlabels': Month_Xlabels,
                'Month_pieData':Month_pieData, 'Month_pieLables': Month_pieLables})


        @app.route('/year_data')
        def year_data():
            global SensorLabels
            global Tminute
            global Thour
            global Tday

                        #####----------------Year Line & Pie Graph Data---------------#####

            YearCompareList=[[],YearAve_U1,YearAve_U2,YearAve_U3,YearAve_U4,YearAve_U5,
               YearAve_U6,YearAve_U7,YearAve_U8,YearAve_U9,YearAve_U10,]

            # print(DayCompareList)

            #Create list of individual Sensors with highest 14 readings:
            runCompare_Year = findHighestReadings()
            Year_orderedList = runCompare_Year.run(YearCompareList) # Returns Ordered List [[Unit,Sensor,AverageReading], ]
            # if Debug == True:
            #     print("------------------Year Ordered List------------------")
            #     print(Year_orderedList)


            #Generate Legend Lables and readngs for top 14
            Year_AveLegend_Lables = []
            Year_displayData = []
            Year_pieLables = []
            Year_pieData = []
            Year_pieData.clear()
            Year_pieLables.clear()
            for i in Year_orderedList:
                # print (i)
                Year_UnitX = i[0]   # Unit
                Year_SensorX = i[1]  # Sensor
                Year_ReadX = i[2]

                if (str(SensorLabels[Year_UnitX][Year_SensorX]) == 'unused' or str(SensorLabels[Year_UnitX][Year_SensorX]) == 'Unused'):
                    pass

                else:
                    Year_pieLables.append(SensorLabels[Year_UnitX][Year_SensorX])
                    Year_pieData.append(Year_ReadX)

                    Year_AveLegend_Lables.append(SensorLabels[Year_UnitX][Year_SensorX])
                    Year_displayData.append(YearCompareList[Year_UnitX][Year_SensorX])

                    while(len(YearCompareList[Year_UnitX][Year_SensorX])<4):
                        YearCompareList[Year_UnitX][Year_SensorX].insert(0,'0')   #Append to start

                    if len(YearCompareList[Year_UnitX][Year_SensorX])>12:
                        YearCompareList[Year_UnitX][Year_SensorX].pop(0)


            #Generate X axis lables in time strings
            try:
                xLength = len(Year_displayData[0])
            except:
                xLength = 1
            PastYearList = []

            for i in range(xLength):
                d = datetime.datetime.today()
                Xday = d - timedelta(days=(i*365))
                # print(Xday.day, Xday.year)
                pastyear = str(Xday.year)

                PastYearList.append(pastyear)
            #print (PastMinutesList)
            Year_Xlabels = PastYearList[::-1]  #reverse the list

            return jsonify({'Year_data' : Year_displayData, 'Year_names' : Year_AveLegend_Lables, 'Year_Xlabels': Year_Xlabels,
                'Year_pieData':Year_pieData, 'Year_pieLables': Year_pieLables})







        @app.route('/settings', methods = ['GET', 'POST'])
        def settings():
            global SensorLabels
            global Interface
            global IPaddress
            global Port
            global Router
            global DNS
            global SSID
            global Password


            form1 = SettingsForm1()
            form2 = SettingsForm2()
            form3 = SettingsForm3()
            form4 = SettingsForm4()
            form5 = SettingsForm5()
            form6 = SettingsForm6()
            form7 = SettingsForm7()
            form8 = SettingsForm8()
            form9 = SettingsForm9()
            form10 = SettingsForm10()
            form_Nw = NetworkForm()

            if request.method == 'POST':
                if form1.U1_S1.data == '': form1.U1_S1.data =  SensorLabels[1][1 ]
                if form1.U1_S2.data == '': form1.U1_S2.data =  SensorLabels[1][2 ]
                if form1.U1_S3.data == '': form1.U1_S3.data =  SensorLabels[1][3 ]
                if form1.U1_S4.data == '': form1.U1_S4.data =  SensorLabels[1][4 ]
                if form1.U1_S5.data == '': form1.U1_S5.data =  SensorLabels[1][5 ]
                if form1.U1_S6.data == '': form1.U1_S6.data =  SensorLabels[1][6 ]
                if form1.U1_S7.data == '': form1.U1_S7.data =  SensorLabels[1][7 ]
                if form1.U1_S8.data == '': form1.U1_S8.data =  SensorLabels[1][8 ]
                if form1.U1_S9.data == '': form1.U1_S9.data =  SensorLabels[1][9 ]
                if form1.U1_S10.data == '': form1.U1_S10.data =  SensorLabels[1][10 ]
                if form1.U1_S11.data == '': form1.U1_S11.data =  SensorLabels[1][11 ]
                if form1.U1_S12.data == '': form1.U1_S12.data =  SensorLabels[1][12 ]
                if form1.U1_S13.data == '': form1.U1_S13.data =  SensorLabels[1][13 ]
                if form1.U1_S14.data == '': form1.U1_S14.data =  SensorLabels[1][14 ]


                if form2.U2_S1.data == '': form2.U2_S1.data =  SensorLabels[2][1 ]
                if form2.U2_S2.data == '': form2.U2_S2.data =  SensorLabels[2][2 ]
                if form2.U2_S3.data == '': form2.U2_S3.data =  SensorLabels[2][3 ]
                if form2.U2_S4.data == '': form2.U2_S4.data =  SensorLabels[2][4 ]
                if form2.U2_S5.data == '': form2.U2_S5.data =  SensorLabels[2][5 ]
                if form2.U2_S6.data == '': form2.U2_S6.data =  SensorLabels[2][6 ]
                if form2.U2_S7.data == '': form2.U2_S7.data =  SensorLabels[2][7 ]
                if form2.U2_S8.data == '': form2.U2_S8.data =  SensorLabels[2][8 ]
                if form2.U2_S9.data == '': form2.U2_S9.data =  SensorLabels[2][9 ]
                if form2.U2_S10.data == '': form2.U2_S10.data =  SensorLabels[2][10 ]
                if form2.U2_S11.data == '': form2.U2_S11.data =  SensorLabels[2][11 ]
                if form2.U2_S12.data == '': form2.U2_S12.data =  SensorLabels[2][12 ]
                if form2.U2_S13.data == '': form2.U2_S13.data =  SensorLabels[2][13 ]
                if form2.U2_S14.data == '': form2.U2_S14.data =  SensorLabels[2][14 ]


                if form3.U3_S1.data == '': form3.U3_S1.data =  SensorLabels[3][1 ]
                if form3.U3_S2.data == '': form3.U3_S2.data =  SensorLabels[3][2 ]
                if form3.U3_S3.data == '': form3.U3_S3.data =  SensorLabels[3][3 ]
                if form3.U3_S4.data == '': form3.U3_S4.data =  SensorLabels[3][4 ]
                if form3.U3_S5.data == '': form3.U3_S5.data =  SensorLabels[3][5 ]
                if form3.U3_S6.data == '': form3.U3_S6.data =  SensorLabels[3][6 ]
                if form3.U3_S7.data == '': form3.U3_S7.data =  SensorLabels[3][7 ]
                if form3.U3_S8.data == '': form3.U3_S8.data =  SensorLabels[3][8 ]
                if form3.U3_S9.data == '':  form3.U3_S9.data =  SensorLabels[3][9 ]
                if form3.U3_S10.data == '': form3.U3_S10.data =  SensorLabels[3][10 ]
                if form3.U3_S11.data == '': form3.U3_S11.data =  SensorLabels[3][11 ]
                if form3.U3_S12.data == '': form3.U3_S12.data =  SensorLabels[3][12 ]
                if form3.U3_S13.data == '': form3.U3_S13.data =  SensorLabels[3][13 ]
                if form3.U3_S14.data == '': form3.U3_S14.data =  SensorLabels[3][14 ]


                if form4.U4_S1.data == '': form4.U4_S1.data =  SensorLabels[4][1 ]
                if form4.U4_S2.data == '': form4.U4_S2.data =  SensorLabels[4][2 ]
                if form4.U4_S3.data == '': form4.U4_S3.data =  SensorLabels[4][3 ]
                if form4.U4_S4.data == '': form4.U4_S4.data =  SensorLabels[4][4 ]
                if form4.U4_S5.data == '': form4.U4_S5.data =  SensorLabels[4][5 ]
                if form4.U4_S6.data == '': form4.U4_S6.data =  SensorLabels[4][6 ]
                if form4.U4_S7.data == '': form4.U4_S7.data =  SensorLabels[4][7 ]
                if form4.U4_S8.data == '': form4.U4_S8.data =  SensorLabels[4][8 ]
                if form4.U4_S9.data == '': form4.U4_S9.data =  SensorLabels[4][9 ]
                if form4.U4_S10.data == '': form4.U4_S10.data =  SensorLabels[4][10 ]
                if form4.U4_S11.data == '': form4.U4_S11.data =  SensorLabels[4][11 ]
                if form4.U4_S12.data == '': form4.U4_S12.data =  SensorLabels[4][12 ]
                if form4.U4_S13.data == '': form4.U4_S13.data =  SensorLabels[4][13 ]
                if form4.U4_S14.data == '': form4.U4_S14.data =  SensorLabels[4][14 ]

                if form5.U5_S1.data  == '': form5.U5_S1.data =    SensorLabels[5][1 ]
                if form5.U5_S2.data  == '': form5.U5_S2.data =    SensorLabels[5][2 ]
                if form5.U5_S3.data  == '': form5.U5_S3.data =    SensorLabels[5][3 ]
                if form5.U5_S4.data  == '': form5.U5_S4.data =    SensorLabels[5][4 ]
                if form5.U5_S5.data  == '': form5.U5_S5.data =    SensorLabels[5][5 ]
                if form5.U5_S6.data  == '': form5.U5_S6.data =    SensorLabels[5][6 ]
                if form5.U5_S7.data  == '': form5.U5_S7.data =    SensorLabels[5][7 ]
                if form5.U5_S8.data  == '': form5.U5_S8.data =    SensorLabels[5][8 ]
                if form5.U5_S9.data  == '': form5.U5_S9.data =    SensorLabels[5][9 ]
                if form5.U5_S10.data == '': form5.U5_S10.data =  SensorLabels[5][10 ]
                if form5.U5_S11.data == '': form5.U5_S11.data =  SensorLabels[5][11 ]
                if form5.U5_S12.data == '': form5.U5_S12.data =  SensorLabels[5][12 ]
                if form5.U5_S13.data == '': form5.U5_S13.data =  SensorLabels[5][13 ]
                if form5.U5_S14.data == '': form5.U5_S14.data =  SensorLabels[5][14 ]

                if form6.U6_S1.data  == '': form6.U6_S1.data =    SensorLabels[6][1 ]
                if form6.U6_S2.data  == '': form6.U6_S2.data =    SensorLabels[6][2 ]
                if form6.U6_S3.data  == '': form6.U6_S3.data =    SensorLabels[6][3 ]
                if form6.U6_S4.data  == '': form6.U6_S4.data =    SensorLabels[6][4 ]
                if form6.U6_S5.data  == '': form6.U6_S5.data =    SensorLabels[6][5 ]
                if form6.U6_S6.data  == '': form6.U6_S6.data =    SensorLabels[6][6 ]
                if form6.U6_S7.data  == '': form6.U6_S7.data =    SensorLabels[6][7 ]
                if form6.U6_S8.data  == '': form6.U6_S8.data =    SensorLabels[6][8 ]
                if form6.U6_S9.data  == '': form6.U6_S9.data =    SensorLabels[6][9 ]
                if form6.U6_S10.data == '': form6.U6_S10.data =   SensorLabels[6][10 ]
                if form6.U6_S11.data == '': form6.U6_S11.data =   SensorLabels[6][11 ]
                if form6.U6_S12.data == '': form6.U6_S12.data =   SensorLabels[6][12 ]
                if form6.U6_S13.data == '': form6.U6_S13.data =   SensorLabels[6][13 ]
                if form6.U6_S14.data == '': form6.U6_S14.data =   SensorLabels[6][14 ]

                if form7.U7_S1.data  == '': form7.U7_S1.data =    SensorLabels[7][1 ]
                if form7.U7_S2.data  == '': form7.U7_S2.data =    SensorLabels[7][2 ]
                if form7.U7_S3.data  == '': form7.U7_S3.data =    SensorLabels[7][3 ]
                if form7.U7_S4.data  == '': form7.U7_S4.data =    SensorLabels[7][4 ]
                if form7.U7_S5.data  == '': form7.U7_S5.data =    SensorLabels[7][5 ]
                if form7.U7_S6.data  == '': form7.U7_S6.data =    SensorLabels[7][6 ]
                if form7.U7_S7.data  == '': form7.U7_S7.data =    SensorLabels[7][7 ]
                if form7.U7_S8.data  == '': form7.U7_S8.data =    SensorLabels[7][8 ]
                if form7.U7_S9.data  == '': form7.U7_S9.data =    SensorLabels[7][9 ]
                if form7.U7_S10.data == '': form7.U7_S10.data =   SensorLabels[7][10 ]
                if form7.U7_S11.data == '': form7.U7_S11.data =   SensorLabels[7][11 ]
                if form7.U7_S12.data == '': form7.U7_S12.data =   SensorLabels[7][12 ]
                if form7.U7_S13.data == '': form7.U7_S13.data =   SensorLabels[7][13 ]
                if form7.U7_S14.data == '': form7.U7_S14.data =   SensorLabels[7][14 ]

                if form8.U8_S1.data  == '': form8.U8_S1.data =    SensorLabels[8][1 ]
                if form8.U8_S2.data  == '': form8.U8_S2.data =    SensorLabels[8][2 ]
                if form8.U8_S3.data  == '': form8.U8_S3.data =    SensorLabels[8][3 ]
                if form8.U8_S4.data  == '': form8.U8_S4.data =    SensorLabels[8][4 ]
                if form8.U8_S5.data  == '': form8.U8_S5.data =    SensorLabels[8][5 ]
                if form8.U8_S6.data  == '': form8.U8_S6.data =    SensorLabels[8][6 ]
                if form8.U8_S7.data  == '': form8.U8_S7.data =    SensorLabels[8][7 ]
                if form8.U8_S8.data  == '': form8.U8_S8.data =    SensorLabels[8][8 ]
                if form8.U8_S9.data  == '': form8.U8_S9.data =    SensorLabels[8][9 ]
                if form8.U8_S10.data == '': form8.U8_S10.data =   SensorLabels[8][10 ]
                if form8.U8_S11.data == '': form8.U8_S11.data =   SensorLabels[8][11 ]
                if form8.U8_S12.data == '': form8.U8_S12.data =   SensorLabels[8][12 ]
                if form8.U8_S13.data == '': form8.U8_S13.data =   SensorLabels[8][13 ]
                if form8.U8_S14.data == '': form8.U8_S14.data =   SensorLabels[8][14 ]

                if form9.U9_S1.data  == '': form9.U9_S1.data =    SensorLabels[9][1 ]
                if form9.U9_S2.data  == '': form9.U9_S2.data =    SensorLabels[9][2 ]
                if form9.U9_S3.data  == '': form9.U9_S3.data =    SensorLabels[9][3 ]
                if form9.U9_S4.data  == '': form9.U9_S4.data =    SensorLabels[9][4 ]
                if form9.U9_S5.data  == '': form9.U9_S5.data =    SensorLabels[9][5 ]
                if form9.U9_S6.data  == '': form9.U9_S6.data =    SensorLabels[9][6 ]
                if form9.U9_S7.data  == '': form9.U9_S7.data =    SensorLabels[9][7 ]
                if form9.U9_S8.data  == '': form9.U9_S8.data =    SensorLabels[9][8 ]
                if form9.U9_S9.data  == '': form9.U9_S9.data =    SensorLabels[9][9 ]
                if form9.U9_S10.data == '': form9.U9_S10.data =   SensorLabels[9][10 ]
                if form9.U9_S11.data == '': form9.U9_S11.data =   SensorLabels[9][11 ]
                if form9.U9_S12.data == '': form9.U9_S12.data =   SensorLabels[9][12 ]
                if form9.U9_S13.data == '': form9.U9_S13.data =   SensorLabels[9][13 ]
                if form9.U9_S14.data == '': form9.U9_S14.data =   SensorLabels[9][14 ]

                if form10.U10_S1.data  == '': form10.U10_S1.data =    SensorLabels[10][1 ]
                if form10.U10_S2.data  == '': form10.U10_S2.data =    SensorLabels[10][2 ]
                if form10.U10_S3.data  == '': form10.U10_S3.data =    SensorLabels[10][3 ]
                if form10.U10_S4.data  == '': form10.U10_S4.data =    SensorLabels[10][4 ]
                if form10.U10_S5.data  == '': form10.U10_S5.data =    SensorLabels[10][5 ]
                if form10.U10_S6.data  == '': form10.U10_S6.data =    SensorLabels[10][6 ]
                if form10.U10_S7.data  == '': form10.U10_S7.data =    SensorLabels[10][7 ]
                if form10.U10_S8.data  == '': form10.U10_S8.data =    SensorLabels[10][8 ]
                if form10.U10_S9.data  == '': form10.U10_S9.data =    SensorLabels[10][9 ]
                if form10.U10_S10.data == '': form10.U10_S10.data =   SensorLabels[10][10 ]
                if form10.U10_S11.data == '': form10.U10_S11.data =   SensorLabels[10][11 ]
                if form10.U10_S12.data == '': form10.U10_S12.data =   SensorLabels[10][12 ]
                if form10.U10_S13.data == '': form10.U10_S13.data =   SensorLabels[10][13 ]
                if form10.U10_S14.data == '': form10.U10_S14.data =   SensorLabels[10][14 ]


                if form_Nw.interface == '': form_Nw.interface.data = Interface
                if form_Nw.ip == '': form_Nw.ip.data = IPaddress
                if form_Nw.port == '': form_Nw.port.data = str(Port)
                if form_Nw.router == '': form_Nw.router.data = Router
                if form_Nw.DNS == '': form_Nw.DNS.data = DNS
                if form_Nw.SSID == '': form_Nw.SSID.data = SSID
                if form_Nw.password == '': form_Nw.password.data = Password



                if form1.validate() == False or form2.validate() == False or form3.validate() == False or form4.validate() == False or  form5.validate() == False or\
                        form6.validate() == False or form7.validate() == False or form8.validate() == False or form9.validate() == False or form10.validate() == False:
                    flash('All fields are required.', 'danger')
                    return render_template('settings.html', form_1 = form1, form_2 = form2, form_3 = form3, form_4 = form4, form_5 = form5,
                                       form_6 = form6, form_7 = form7, form_8 = form8, form_9 = form9, form_10 = form10, form_Nw = form_Nw)

                else:
                    #if form completed correctly:
                    SensorLabels[1][1 ] =  str(form1.U1_S1.data)
                    SensorLabels[1][2 ] =  str(form1.U1_S2.data)
                    SensorLabels[1][3 ] =  str(form1.U1_S3.data)
                    SensorLabels[1][4 ] =  str(form1.U1_S4.data)
                    SensorLabels[1][5 ] =  str(form1.U1_S5.data)
                    SensorLabels[1][6 ] =  str(form1.U1_S6.data)
                    SensorLabels[1][7 ] =  str(form1.U1_S7.data)
                    SensorLabels[1][8 ] =  str(form1.U1_S8.data)
                    SensorLabels[1][9 ] =  str(form1.U1_S9.data)
                    SensorLabels[1][10] =  str(form1.U1_S10.data)
                    SensorLabels[1][11] =  str(form1.U1_S11.data)
                    SensorLabels[1][12] =  str(form1.U1_S12.data)
                    SensorLabels[1][13] =  str(form1.U1_S13.data)
                    SensorLabels[1][14] =  str(form1.U1_S14.data)

                    SensorLabels[2][1 ] =  str(form2.U2_S1.data)
                    SensorLabels[2][2 ] =  str(form2.U2_S2.data)
                    SensorLabels[2][3 ] =  str(form2.U2_S3.data)
                    SensorLabels[2][4 ] =  str(form2.U2_S4.data)
                    SensorLabels[2][5 ] =  str(form2.U2_S5.data)
                    SensorLabels[2][6 ] =  str(form2.U2_S6.data)
                    SensorLabels[2][7 ] =  str(form2.U2_S7.data)
                    SensorLabels[2][8 ] =  str(form2.U2_S8.data)
                    SensorLabels[2][9 ] =  str(form2.U2_S9.data)
                    SensorLabels[2][10] =  str(form2.U2_S10.data)
                    SensorLabels[2][11] =  str(form2.U2_S11.data)
                    SensorLabels[2][12] =  str(form2.U2_S12.data)
                    SensorLabels[2][13] =  str(form2.U2_S13.data)
                    SensorLabels[2][14] =  str(form2.U2_S14.data)

                    SensorLabels[3][1 ] =  str(form3.U3_S1.data)
                    SensorLabels[3][2 ] =  str(form3.U3_S2.data)
                    SensorLabels[3][3 ] =  str(form3.U3_S3.data)
                    SensorLabels[3][4 ] =  str(form3.U3_S4.data)
                    SensorLabels[3][5 ] =  str(form3.U3_S5.data)
                    SensorLabels[3][6 ] =  str(form3.U3_S6.data)
                    SensorLabels[3][7 ] =  str(form3.U3_S7.data)
                    SensorLabels[3][8 ] =  str(form3.U3_S8.data)
                    SensorLabels[3][9 ] =  str(form3.U3_S9.data)
                    SensorLabels[3][10] =  str(form3.U3_S10.data)
                    SensorLabels[3][11] =  str(form3.U3_S11.data)
                    SensorLabels[3][12] =  str(form3.U3_S12.data)
                    SensorLabels[3][13] =  str(form3.U3_S13.data)
                    SensorLabels[3][14] =  str(form3.U3_S14.data)

                    SensorLabels[4][1 ] =  str(form4.U4_S1.data)
                    SensorLabels[4][2 ] =  str(form4.U4_S2.data)
                    SensorLabels[4][3 ] =  str(form4.U4_S3.data)
                    SensorLabels[4][4 ] =  str(form4.U4_S4.data)
                    SensorLabels[4][5 ] =  str(form4.U4_S5.data)
                    SensorLabels[4][6 ] =  str(form4.U4_S6.data)
                    SensorLabels[4][7 ] =  str(form4.U4_S7.data)
                    SensorLabels[4][8 ] =  str(form4.U4_S8.data)
                    SensorLabels[4][9 ] =  str(form4.U4_S9.data)
                    SensorLabels[4][10] =  str(form4.U4_S10.data)
                    SensorLabels[4][11] =  str(form4.U4_S11.data)
                    SensorLabels[4][12] =  str(form4.U4_S12.data)
                    SensorLabels[4][13] =  str(form4.U4_S13.data)
                    SensorLabels[4][14] =  str(form4.U4_S14.data)

                    SensorLabels[5][1 ] =  str(form5.U5_S1.data)
                    SensorLabels[5][2 ] =  str(form5.U5_S2.data)
                    SensorLabels[5][3 ] =  str(form5.U5_S3.data)
                    SensorLabels[5][4 ] =  str(form5.U5_S4.data)
                    SensorLabels[5][5 ] =  str(form5.U5_S5.data)
                    SensorLabels[5][6 ] =  str(form5.U5_S6.data)
                    SensorLabels[5][7 ] =  str(form5.U5_S7.data)
                    SensorLabels[5][8 ] =  str(form5.U5_S8.data)
                    SensorLabels[5][9 ] =  str(form5.U5_S9.data)
                    SensorLabels[5][10] =  str(form5.U5_S10.data)
                    SensorLabels[5][11] =  str(form5.U5_S11.data)
                    SensorLabels[5][12] =  str(form5.U5_S12.data)
                    SensorLabels[5][13] =  str(form5.U5_S13.data)
                    SensorLabels[5][14] =  str(form5.U5_S14.data)

                    SensorLabels[6][1 ] =  str(form6.U6_S1.data)
                    SensorLabels[6][2 ] =  str(form6.U6_S2.data)
                    SensorLabels[6][3 ] =  str(form6.U6_S3.data)
                    SensorLabels[6][4 ] =  str(form6.U6_S4.data)
                    SensorLabels[6][5 ] =  str(form6.U6_S5.data)
                    SensorLabels[6][6 ] =  str(form6.U6_S6.data)
                    SensorLabels[6][7 ] =  str(form6.U6_S7.data)
                    SensorLabels[6][8 ] =  str(form6.U6_S8.data)
                    SensorLabels[6][9 ] =  str(form6.U6_S9.data)
                    SensorLabels[6][10] =  str(form6.U6_S10.data)
                    SensorLabels[6][11] =  str(form6.U6_S11.data)
                    SensorLabels[6][12] =  str(form6.U6_S12.data)
                    SensorLabels[6][13] =  str(form6.U6_S13.data)
                    SensorLabels[6][14] =  str(form6.U6_S14.data)

                    SensorLabels[7][1 ] =  str(form7.U7_S1.data)
                    SensorLabels[7][2 ] =  str(form7.U7_S2.data)
                    SensorLabels[7][3 ] =  str(form7.U7_S3.data)
                    SensorLabels[7][4 ] =  str(form7.U7_S4.data)
                    SensorLabels[7][5 ] =  str(form7.U7_S5.data)
                    SensorLabels[7][6 ] =  str(form7.U7_S6.data)
                    SensorLabels[7][7 ] =  str(form7.U7_S7.data)
                    SensorLabels[7][8 ] =  str(form7.U7_S8.data)
                    SensorLabels[7][9 ] =  str(form7.U7_S9.data)
                    SensorLabels[7][10] =  str(form7.U7_S10.data)
                    SensorLabels[7][11] =  str(form7.U7_S11.data)
                    SensorLabels[7][12] =  str(form7.U7_S12.data)
                    SensorLabels[7][13] =  str(form7.U7_S13.data)
                    SensorLabels[7][14] =  str(form7.U7_S14.data)

                    SensorLabels[8][1 ] =  str(form8.U8_S1.data)
                    SensorLabels[8][2 ] =  str(form8.U8_S2.data)
                    SensorLabels[8][3 ] =  str(form8.U8_S3.data)
                    SensorLabels[8][4 ] =  str(form8.U8_S4.data)
                    SensorLabels[8][5 ] =  str(form8.U8_S5.data)
                    SensorLabels[8][6 ] =  str(form8.U8_S6.data)
                    SensorLabels[8][7 ] =  str(form8.U8_S7.data)
                    SensorLabels[8][8 ] =  str(form8.U8_S8.data)
                    SensorLabels[8][9 ] =  str(form8.U8_S9.data)
                    SensorLabels[8][10] =  str(form8.U8_S10.data)
                    SensorLabels[8][11] =  str(form8.U8_S11.data)
                    SensorLabels[8][12] =  str(form8.U8_S12.data)
                    SensorLabels[8][13] =  str(form8.U8_S13.data)
                    SensorLabels[8][14] =  str(form8.U8_S14.data)

                    SensorLabels[9][1 ] =  str(form9.U9_S1.data)
                    SensorLabels[9][2 ] =  str(form9.U9_S2.data)
                    SensorLabels[9][3 ] =  str(form9.U9_S3.data)
                    SensorLabels[9][4 ] =  str(form9.U9_S4.data)
                    SensorLabels[9][5 ] =  str(form9.U9_S5.data)
                    SensorLabels[9][6 ] =  str(form9.U9_S6.data)
                    SensorLabels[9][7 ] =  str(form9.U9_S7.data)
                    SensorLabels[9][8 ] =  str(form9.U9_S8.data)
                    SensorLabels[9][9 ] =  str(form9.U9_S9.data)
                    SensorLabels[9][10] =  str(form9.U9_S10.data)
                    SensorLabels[9][11] =  str(form9.U9_S11.data)
                    SensorLabels[9][12] =  str(form9.U9_S12.data)
                    SensorLabels[9][13] =  str(form9.U9_S13.data)
                    SensorLabels[9][14] =  str(form9.U9_S14.data)

                    SensorLabels[10][1 ] =  str(form10.U10_S1.data)
                    SensorLabels[10][2 ] =  str(form10.U10_S2.data)
                    SensorLabels[10][3 ] =  str(form10.U10_S3.data)
                    SensorLabels[10][4 ] =  str(form10.U10_S4.data)
                    SensorLabels[10][5 ] =  str(form10.U10_S5.data)
                    SensorLabels[10][6 ] =  str(form10.U10_S6.data)
                    SensorLabels[10][7 ] =  str(form10.U10_S7.data)
                    SensorLabels[10][8 ] =  str(form10.U10_S8.data)
                    SensorLabels[10][9 ] =  str(form10.U10_S9.data)
                    SensorLabels[10][10] =  str(form10.U10_S10.data)
                    SensorLabels[10][11] =  str(form10.U10_S11.data)
                    SensorLabels[10][12] =  str(form10.U10_S12.data)
                    SensorLabels[10][13] =  str(form10.U10_S13.data)
                    SensorLabels[10][14] =  str(form10.U10_S14.data)

                    # Interface = str(form_Nw.interface.data)
                    # IPaddress = str(form_Nw.ip.data)
                    # Port = int(form_Nw.port.data)
                    # Router = str(form_Nw.router.data)
                    # DNS = str(form_Nw.DNS.data)
                    # SSID = str(form_Nw.SSID.data)
                    # Password =  str(form_Nw.password.data)


                    # print(SensorLabels)
                    #return render_template('main.html')

                    # return redirect(url_for('index'))
                    flash('Unit Names- Saved','success')
                    saveLables()
                    return render_template('settings.html', form_1 = form1, form_2 = form2, form_3 = form3, form_4 = form4, form_5 = form5,
                                       form_6 = form6, form_7 = form7, form_8 = form8, form_9 = form9, form_10 = form10, form_Nw = form_Nw)
                    # return redirect(url_for('index'))
            elif request.method == 'GET':

                form1.U1_S1.data =  SensorLabels[1][1 ]
                form1.U1_S2.data =  SensorLabels[1][2 ]
                form1.U1_S3.data =  SensorLabels[1][3 ]
                form1.U1_S4.data =  SensorLabels[1][4 ]
                form1.U1_S5.data =  SensorLabels[1][5 ]
                form1.U1_S6.data =  SensorLabels[1][6 ]
                form1.U1_S7.data =  SensorLabels[1][7 ]
                form1.U1_S8.data =  SensorLabels[1][8 ]
                form1.U1_S9.data =  SensorLabels[1][9 ]
                form1.U1_S10.data = SensorLabels[1][10]
                form1.U1_S11.data = SensorLabels[1][11]
                form1.U1_S12.data = SensorLabels[1][12]
                form1.U1_S13.data = SensorLabels[1][13]
                form1.U1_S14.data = SensorLabels[1][14]

                form2.U2_S1.data =  SensorLabels[2][1 ]
                form2.U2_S2.data =  SensorLabels[2][2 ]
                form2.U2_S3.data =  SensorLabels[2][3 ]
                form2.U2_S4.data =  SensorLabels[2][4 ]
                form2.U2_S5.data =  SensorLabels[2][5 ]
                form2.U2_S6.data =  SensorLabels[2][6 ]
                form2.U2_S7.data =  SensorLabels[2][7 ]
                form2.U2_S8.data =  SensorLabels[2][8 ]
                form2.U2_S9.data =  SensorLabels[2][9 ]
                form2.U2_S10.data = SensorLabels[2][10]
                form2.U2_S11.data = SensorLabels[2][11]
                form2.U2_S12.data = SensorLabels[2][12]
                form2.U2_S13.data = SensorLabels[2][13]
                form2.U2_S14.data = SensorLabels[2][14]

                form3.U3_S1.data =  SensorLabels[3][1 ]
                form3.U3_S2.data =  SensorLabels[3][2 ]
                form3.U3_S3.data =  SensorLabels[3][3 ]
                form3.U3_S4.data =  SensorLabels[3][4 ]
                form3.U3_S5.data =  SensorLabels[3][5 ]
                form3.U3_S6.data =  SensorLabels[3][6 ]
                form3.U3_S7.data =  SensorLabels[3][7 ]
                form3.U3_S8.data =  SensorLabels[3][8 ]
                form3.U3_S9.data =  SensorLabels[3][9 ]
                form3.U3_S10.data = SensorLabels[3][10]
                form3.U3_S11.data = SensorLabels[3][11]
                form3.U3_S12.data = SensorLabels[3][12]
                form3.U3_S13.data = SensorLabels[3][13]
                form3.U3_S14.data = SensorLabels[3][14]

                form4.U4_S1.data =  SensorLabels[4][1 ]
                form4.U4_S2.data =  SensorLabels[4][2 ]
                form4.U4_S3.data =  SensorLabels[4][3 ]
                form4.U4_S4.data =  SensorLabels[4][4 ]
                form4.U4_S5.data =  SensorLabels[4][5 ]
                form4.U4_S6.data =  SensorLabels[4][6 ]
                form4.U4_S7.data =  SensorLabels[4][7 ]
                form4.U4_S8.data =  SensorLabels[4][8 ]
                form4.U4_S9.data =  SensorLabels[4][9 ]
                form4.U4_S10.data = SensorLabels[4][10]
                form4.U4_S11.data = SensorLabels[4][11]
                form4.U4_S12.data = SensorLabels[4][12]
                form4.U4_S13.data = SensorLabels[4][13]
                form4.U4_S14.data = SensorLabels[4][14]

                form5.U5_S1.data =  SensorLabels[5][1 ]
                form5.U5_S2.data =  SensorLabels[5][2 ]
                form5.U5_S3.data =  SensorLabels[5][3 ]
                form5.U5_S4.data =  SensorLabels[5][4 ]
                form5.U5_S5.data =  SensorLabels[5][5 ]
                form5.U5_S6.data =  SensorLabels[5][6 ]
                form5.U5_S7.data =  SensorLabels[5][7 ]
                form5.U5_S8.data =  SensorLabels[5][8 ]
                form5.U5_S9.data =  SensorLabels[5][9 ]
                form5.U5_S10.data = SensorLabels[5][10]
                form5.U5_S11.data = SensorLabels[5][11]
                form5.U5_S12.data = SensorLabels[5][12]
                form5.U5_S13.data = SensorLabels[5][13]
                form5.U5_S14.data = SensorLabels[5][14]

                form6.U6_S1.data =  SensorLabels[6][1 ]
                form6.U6_S2.data =  SensorLabels[6][2 ]
                form6.U6_S3.data =  SensorLabels[6][3 ]
                form6.U6_S4.data =  SensorLabels[6][4 ]
                form6.U6_S5.data =  SensorLabels[6][5 ]
                form6.U6_S6.data =  SensorLabels[6][6 ]
                form6.U6_S7.data =  SensorLabels[6][7 ]
                form6.U6_S8.data =  SensorLabels[6][8 ]
                form6.U6_S9.data =  SensorLabels[6][9 ]
                form6.U6_S10.data = SensorLabels[6][10]
                form6.U6_S11.data = SensorLabels[6][11]
                form6.U6_S12.data = SensorLabels[6][12]
                form6.U6_S13.data = SensorLabels[6][13]
                form6.U6_S14.data = SensorLabels[6][14]

                form7.U7_S1.data =  SensorLabels[7][1 ]
                form7.U7_S2.data =  SensorLabels[7][2 ]
                form7.U7_S3.data =  SensorLabels[7][3 ]
                form7.U7_S4.data =  SensorLabels[7][4 ]
                form7.U7_S5.data =  SensorLabels[7][5 ]
                form7.U7_S6.data =  SensorLabels[7][6 ]
                form7.U7_S7.data =  SensorLabels[7][7 ]
                form7.U7_S8.data =  SensorLabels[7][8 ]
                form7.U7_S9.data =  SensorLabels[7][9 ]
                form7.U7_S10.data = SensorLabels[7][10]
                form7.U7_S11.data = SensorLabels[7][11]
                form7.U7_S12.data = SensorLabels[7][12]
                form7.U7_S13.data = SensorLabels[7][13]
                form7.U7_S14.data = SensorLabels[7][14]

                form8.U8_S1.data =  SensorLabels[8][1 ]
                form8.U8_S2.data =  SensorLabels[8][2 ]
                form8.U8_S3.data =  SensorLabels[8][3 ]
                form8.U8_S4.data =  SensorLabels[8][4 ]
                form8.U8_S5.data =  SensorLabels[8][5 ]
                form8.U8_S6.data =  SensorLabels[8][6 ]
                form8.U8_S7.data =  SensorLabels[8][7 ]
                form8.U8_S8.data =  SensorLabels[8][8 ]
                form8.U8_S9.data =  SensorLabels[8][9 ]
                form8.U8_S10.data = SensorLabels[8][10]
                form8.U8_S11.data = SensorLabels[8][11]
                form8.U8_S12.data = SensorLabels[8][12]
                form8.U8_S13.data = SensorLabels[8][13]
                form8.U8_S14.data = SensorLabels[8][14]

                form9.U9_S1.data =  SensorLabels[9][1 ]
                form9.U9_S2.data =  SensorLabels[9][2 ]
                form9.U9_S3.data =  SensorLabels[9][3 ]
                form9.U9_S4.data =  SensorLabels[9][4 ]
                form9.U9_S5.data =  SensorLabels[9][5 ]
                form9.U9_S6.data =  SensorLabels[9][6 ]
                form9.U9_S7.data =  SensorLabels[9][7 ]
                form9.U9_S8.data =  SensorLabels[9][8 ]
                form9.U9_S9.data =  SensorLabels[9][9 ]
                form9.U9_S10.data = SensorLabels[9][10]
                form9.U9_S11.data = SensorLabels[9][11]
                form9.U9_S12.data = SensorLabels[9][12]
                form9.U9_S13.data = SensorLabels[9][13]
                form9.U9_S14.data = SensorLabels[9][14]

                form10.U10_S1.data =  SensorLabels[10][1 ]
                form10.U10_S2.data =  SensorLabels[10][2 ]
                form10.U10_S3.data =  SensorLabels[10][3 ]
                form10.U10_S4.data =  SensorLabels[10][4 ]
                form10.U10_S5.data =  SensorLabels[10][5 ]
                form10.U10_S6.data =  SensorLabels[10][6 ]
                form10.U10_S7.data =  SensorLabels[10][7 ]
                form10.U10_S8.data =  SensorLabels[10][8 ]
                form10.U10_S9.data =  SensorLabels[10][9 ]
                form10.U10_S10.data = SensorLabels[10][10]
                form10.U10_S11.data = SensorLabels[10][11]
                form10.U10_S12.data = SensorLabels[10][12]
                form10.U10_S13.data = SensorLabels[10][13]
                form10.U10_S14.data = SensorLabels[10][14]

                form_Nw.interface.data = Interface
                form_Nw.ip.data = IPaddress
                form_Nw.port.data = str(Port)
                form_Nw.router.data = Router
                form_Nw.DNS.data = DNS
                form_Nw.SSID.data = SSID
                form_Nw.password.data = Password




                return render_template('settings.html', form_1 = form1, form_2 = form2, form_3 = form3, form_4 = form4, form_5 = form5,
                                       form_6 = form6, form_7 = form7, form_8 = form8, form_9 = form9, form_10 = form10,form_Nw = form_Nw)

        app.run(debug=False,host=IPaddress, port=Port)


class threadRandomSet(threading.Thread):
    def __init__(self,Drange):
        threading.Thread.__init__(self)
        global Debug
        global UnitNo
        global pasthour
        global Thour
        global Tminute
        global pastminute
        global pasthour

        #lel#pasthour = Thour
        while UnitNo < Drange:
            UnitValues.insert(UnitNo,[])
            thisUnit = UnitNo
            UnitNo += 1


        while True:
            i = 1
            output = [[],[],[],[],[],[],[],[],[],[]]
            while i < (Drange+1):
                numset = genRandset().run()
                output[i].clear()
                output[i].append([("U"+str(i)+', , '+numset)])
                computeVals((i-1),("U"+str(i)+', , '+numset),"x")
                i +=1

            if Debug == True:
                print("Data Stream: "+str(output))

            pastminute = Tminute
            #lel#pasthour = Thour

            time.sleep(9)


class genRandset():
    def run(self):
        # set1 = str(random.randint(1,10)) #unit No
        set2 = str(round(random.uniform(20,30),2))
        set3 = str(round(random.uniform(0,50),2))
        set4 = str(round(random.uniform(35,60),2))
        set5 = str(round(random.uniform(60,80),2))
        set6 = str(round(random.uniform(0,100),2))
        set7 = str(round(random.uniform(0,20),2))
        set8 = str(round(random.uniform(20,30),2))
        set9 = str(round(random.uniform(0,50),2))
        set10 = str(round(random.uniform(35,60),2))
        set11 = str(round(random.uniform(60,80),2))
        set12 = str(round(random.uniform(80,100),2))
        set13 = str(round(random.uniform(0,20),2))
        set14 = str(round(random.uniform(0,30),2))
        set15 = str(round(random.uniform(20,30),2))

        numset = [set2,set3,set4,set5,set6,set7,set8,set9,set10,set11,set12,set13,set14,set15]
        output = ""
        for x,y in enumerate(numset):
            if x < 13:
                output += str(y)+', '
            else:
                output  += str(y)

            # output += x
            # output.append(x)

        return(output)


        #'U4, 0.37, 0.34, 0.00, 0.34, 0.38, 88.25, 0.34, 0.30, 0.34, 0.39, 0.46, 0.34, 0.41, 0.35,',


class findHighestReadings():
    def run(self,list_X):
        global displayMax_Sensors
        SSClist = []   #Sensor Sum Comapre List
        for i,unit in enumerate(list_X):
            for s,sensorReadings in enumerate(unit):
                sensorSumAve = 0
                noReadings = 0
                for reading in sensorReadings:
                    try:
                        sensorSumAve += int(reading)
                        noReadings += 1
                    except: pass
                #print("Unit: "+str(i)+", Sensor: "+str(s)+" Sum: " + str(sensorSumAve))
                try:
                    sensorSumAve = sensorSumAve/noReadings
                except:
                    sensorSumAve = 0
                sensorSumAve = round(sensorSumAve,2)
                if sensorSumAve >0:
                    SSClist.append([i,s,sensorSumAve])   #Append UNIT_no, SENSOR_no, READINGS_average
                # print (i,s,sensorSumAve)


        #function to custom sort list by its third component ie, the average value
        def custom_sort(t):
            return t[2]

        SSClist.sort(key=custom_sort, reverse = True)
        # print(SSClist)

        SSClist = SSClist[:displayMax_Sensors]  #[Unit,senosr,readningAve] from highest to lowest for top 14


        return(SSClist)


class LanIp():

    def run(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8",80))
        IP = (s.getsockname()[0])
        s.close()
        return IP


class loadUnitLists():
    def run(self,U_File,hrList,dayList,weekList,monthList,yearList):
        global LoadData
        global Debug
        global Thour
        global Tminute
        underHourFlag = False
        underDayFlag = False
        underWeekFlag = False
        underMonthFlag = False
        underYearFlag = False

        timestamp = ''
        U_File = 'data/'+ U_File

        try:
            with open(U_File) as f1:
                loadedData = str(f1.read())

            if Debug == True:
                print("Found File: " + U_File)
                print("--------Loaded Data " + U_File + "--------")
            SplitData = loadedData.split('\n\n')
            for i, line in enumerate(SplitData):
                if i == 0:
                    if len(line)>0:
                        try:
                            timestamp = line
                            if Debug == True:
                                print("Loaded [" + str(i) + "] TimeStamp: " + str(timestamp))


                                index1 = timestamp.index("/")
                                index2 = timestamp.index("/",index1+1)
                                index3 = timestamp.index("-",index2)
                                index4 = timestamp.index(":",index3)

                                L_day = (timestamp[0:index1])
                                L_month = (timestamp[index1+1:index2])
                                L_year = (timestamp[index2+1:index3])
                                L_hour = (timestamp[index3+2:index4])
                                L_minute = (timestamp[index4+1:])

                                output = L_month + " " + L_day + " " + L_year + "  " + L_hour +":"+ L_minute

                                d = datetime.datetime.now()

                                datetime_object = datetime.datetime.strptime(output, '%m %d %Y %H:%M')
                                # print (datetime_object)
                                elapsedTime = datetime_object - d
                                # print (elapsedTime)

                                result = divmod(elapsedTime.total_seconds(), 60)

                                # print(result[0]) #minutes difference between dates

                                if result[0] > -60:
                                    # print("Under 1 hour")
                                    underHourFlag = True
                                else:
                                    # print("Over 1 hour")
                                    underHourFlag = False

                                # if result[0] > -1440:
                                #     print("Under 1 day")
                                #     underDayFlag = True
                                # else:
                                #     print("Over 1 day")
                                #     underDayFlag = False
                                #
                                # if result[0] > -10080:
                                #     print("Under 1 week")
                                #     underWeekFlag = True
                                # else:
                                #     print("Over 1 week")
                                #     underWeekFlag = False
                                #
                                # if result[0] > -40320:
                                #     print("Under 1 month")
                                #     underMonthFlag = True
                                # else:
                                #     print("Over 1 month")
                                #     underMonthFlag = False
                                #
                                # if result[0] > -483830:
                                #     print("Under 1 year")
                                #     underYearFlag = True
                                # else:
                                #     print("Over 1 year")
                                #     underYearFlag = False


                        except:
                            print("Error unable to convert string to TimeStamp")
                            pass




                if i == 1:
                    if len(line)>0:
                        if underHourFlag == True:
                            try:
                                line = line[line.index("=")+2:]
                                hrList = literal_eval(line)
                                hrList = hrList[0]
                                if Debug == True:
                                    print("Loaded [" + str(i) + "] hrList: " + str(hrList))
                            except:
                                print("Error unable to literal_eval of hrList")
                                pass
                        else:
                            pass
                if i == 2:
                    if len(line)>0:
                        try:
                            line = line[line.index("=")+2:]
                            dayList = literal_eval(line)
                            dayList = dayList[0]
                            if Debug == True:
                                print("Loaded [" + str(i) + "] dayList: "  + str(dayList))
                        except:
                            print("Error unable to literal_eval of dayList")
                            dayList = []
                if i == 3:
                    if len(line)>0:
                        try:
                            line = line[line.index("=")+2:]
                            weekList = literal_eval(line)
                            weekList = weekList[0]
                            if Debug == True:
                                print("Loaded [" + str(i) + "] weekList: " + str(weekList))
                        except:
                            print("Error unable to literal_eval of weekList")
                            weekList = []
                if i == 4:
                    if len(line)>0:
                        try:
                            line = line[line.index("=")+2:]
                            monthList = literal_eval(line)
                            monthList = monthList[0]
                            if Debug == True:
                                print("Loaded [" + str(i) + "] monthList: " + str(monthList))
                        except:
                            print("Error unable to literal_eval of monthList")
                            monthList = []
                if i == 5:
                    if len(line)>0:
                        try:
                            line = line[line.index("=")+2:]
                            yearList = literal_eval(line)
                            yearList = yearList[0]
                            if Debug == True:
                                print("Loaded [" + str(i) + "] yearList: " + str(yearList))
                        except:
                            print("Error unable to literal_eval of yearList")
                            yearList = []

        except:
            if Debug == True:
                print ("*<Error- ["+ str(U_File) + "] could not be located>*")
            else:
                pass


        return(timestamp,hrList,dayList,weekList,monthList,yearList)


class loadSettings():
    def __init__(self):
        global Debug
        global Settings_File
        global SensorLabels

        global Ufile_list

        global HrAve_U1
        global HrAve_U2
        global HrAve_U3
        global HrAve_U4
        global HrAve_U5
        global HrAve_U6
        global HrAve_U7
        global HrAve_U8
        global HrAve_U9
        global HrAve_U10

        global DayAve_U1
        global DayAve_U2
        global DayAve_U3
        global DayAve_U4
        global DayAve_U5
        global DayAve_U6
        global DayAve_U7
        global DayAve_U8
        global DayAve_U9
        global DayAve_U10

        global WeekAve_U1
        global WeekAve_U2
        global WeekAve_U3
        global WeekAve_U4
        global WeekAve_U5
        global WeekAve_U6
        global WeekAve_U7
        global WeekAve_U8
        global WeekAve_U9
        global WeekAve_U10

        global MonthAve_U1
        global MonthAve_U2
        global MonthAve_U3
        global MonthAve_U4
        global MonthAve_U5
        global MonthAve_U6
        global MonthAve_U7
        global MonthAve_U8
        global MonthAve_U9
        global MonthAve_U10

        global SeasonAve_U1
        global SeasonAve_U2
        global SeasonAve_U3
        global SeasonAve_U4
        global SeasonAve_U5
        global SeasonAve_U6
        global SeasonAve_U7
        global SeasonAve_U8
        global SeasonAve_U9
        global SeasonAve_U10

        global YearAve_U1
        global YearAve_U2
        global YearAve_U3
        global YearAve_U4
        global YearAve_U5
        global YearAve_U6
        global YearAve_U7
        global YearAve_U8
        global YearAve_U9
        global YearAve_U10

        try:
            with open(Settings_File) as f1:
                loadedData = str(f1.read())

            SensorLabels = literal_eval(loadedData)

        except:
            print ("*<Error- ["+ str(Settings_File) + "] could not be located>*")


        if LoadData == True:
            for x,y in enumerate(Ufile_list[0:]):

                if x == 1:
                    try:
                        U1 = loadUnitLists()
                        _,HrAve_U1,DayAve_U1,WeekAve_U1,MonthAve_U1,YearAve_U1 = U1.run(y,HrAve_U1,DayAve_U1,WeekAve_U1,MonthAve_U1,YearAve_U1)
                    except:
                        print("Failed to load U" + str(x)) + " data."
                elif x == 2:
                    try:
                        U2 = loadUnitLists()
                        _,HrAve_U2,DayAve_U2,WeekAve_U2,MonthAve_U2,YearAve_U2 = U2.run(y,HrAve_U2,DayAve_U2,WeekAve_U2,MonthAve_U2,YearAve_U2)
                    except:
                        print("Failed to load U" + str(x)) + " data."
                elif x == 3:
                    try:
                        U3 = loadUnitLists()
                        _,HrAve_U3,DayAve_U3,WeekAve_U3,MonthAve_U3,YearAve_U3 = U3.run(y,HrAve_U3,DayAve_U3,WeekAve_U3,MonthAve_U3,YearAve_U3)
                    except:
                        print("Failed to load U" + str(x)) + " data."
                elif x == 4:
                    try:
                        U4 = loadUnitLists()
                        _,HrAve_U4,DayAve_U4,WeekAve_U4,MonthAve_U4,YearAve_U4 = U4.run(y,HrAve_U4,DayAve_U4,WeekAve_U4,MonthAve_U4,YearAve_U4)
                    except:
                        print("Failed to load U" + str(x)) + " data."
                elif x == 5:
                    try:
                        U5 = loadUnitLists()
                        _,HrAve_U5,DayAve_U5,WeekAve_U5,MonthAve_U5,YearAve_U5 = U5.run(y,HrAve_U5,DayAve_U5,WeekAve_U5,MonthAve_U5,YearAve_U5)
                    except:
                        print("Failed to load U" + str(x)) + " data."
                elif x == 6:
                    try:
                        U6 = loadUnitLists()
                        _,HrAve_U6,DayAve_U6,WeekAve_U6,MonthAve_U6,YearAve_U6 = U6.run(y,HrAve_U6,DayAve_U6,WeekAve_U6,MonthAve_U6,YearAve_U6)
                    except:
                        print("Failed to load U" + str(x)) + " data."
                elif x == 7:
                    try:
                        U7 = loadUnitLists()
                        _,HrAve_U7,DayAve_U7,WeekAve_U7,MonthAve_U7,YearAve_U7 = U7.run(y,HrAve_U7,DayAve_U7,WeekAve_U7,MonthAve_U7,YearAve_U7)
                    except:
                        print("Failed to load U" + str(x)) + " data."
                elif x == 8:
                    try:
                        U8 = loadUnitLists()
                        _,HrAve_U8,DayAve_U8,WeekAve_U8,MonthAve_U8,YearAve_U8 = U8.run(y,HrAve_U8,DayAve_U8,WeekAve_U8,MonthAve_U8,YearAve_U8)
                    except:
                        print("Failed to load U" + str(x)) + " data."
                elif x == 9:
                    try:
                        U9 = loadUnitLists()
                        _,HrAve_U9,DayAve_U9,WeekAve_U9,MonthAve_U9,YearAve_U9 = U9.run(y,HrAve_U9,DayAve_U9,WeekAve_U9,MonthAve_U9,YearAve_U9)
                    except:
                        print("Failed to load U" + str(x)) + " data."
                elif x == 10:
                    try:
                        U10 = loadUnitLists()
                        _,HrAve_U10,DayAve_U10,WeekAve_U10,MonthAve_U10,YearAve_U10 = U10.run(y,HrAve_U10,DayAve_U10,WeekAve_U10,MonthAve_U10,YearAve_U10)
                    except:
                        print("Failed to load U" + str(x)) + " data."
            if Debug == True:
                print("------------------End of Load Data------------------")
        else:
            print("loadData = False")


class saveLists(threading.Thread):
    def __init__(self,listFile,X_List):
        threading.Thread.__init__(self)
        global Thour
        global Tminute
        global Tday
        global Debug

        print("Saving Data")
        path = 'data'
        if not os.path.exists(path):
            print("Error: " + path + " directory could not be located. Creating new " + path + " directory")
            try:
                os.mkdir(path)
                if Debug == True:
                    print ("Successfully created the directory %s " % path)

            except OSError:
                print ("Creation of the directory %s failed" % path)

        if Debug == True:
            print ("<saveLists [" + path +'/'+ listFile + "] >")

        saveString = Tday+ " - "+str(Thour)+":"+str(Tminute) + "\n\n"
        saveString += str(X_List)


        with open(path+'/'+listFile,'w') as f1:
            f1.write(str(saveString))


class saveLables():
    def __init__(self):
        global Settings_File
        global SensorLabels
        print ("<saveLables>")

        # # try:
        with open(Settings_File,'w') as f1:
            # f1.write("<LABLES>")
            f1.write(str(SensorLabels))


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

if __name__ == "__main__":
    loadSettings()
    if Local == False:
        check_ip = LanIp()
        IPaddress = str(check_ip.run())
    else:
        IPaddress = '127.0.0.1'
    tParallel = threading.Thread(target=parallel, args=())
    #tParallel.daemon = True
    tParallel.start()

    if Test == True:
        Drange = 1
        trandSet = threading.Thread(target=threadRandomSet, args=(Drange,))
        trandSet.start()

    else:
        tserialComs = threading.Thread(target =serach4serial, args=())
        # tX.daemon = True
        tserialComs.start()

    loadUsers()
    webserver()

