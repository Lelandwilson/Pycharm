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

        global HourReading

        def everyminute(UnitVal_X,HrAve_X,DayAve_X):
            global Thour
            global pasthour
            global Tminute
            global pastminute
            global Tsec

            if pastminute != Tminute:
                self.x = 0
                self.total = 0
                for n in UnitVal_X:
                    if (isinstance(n, (int, float))):
                        self.x += n
                        self.total +=1
                if (self.total>0):
                    val = round(self.x / self.total,2)
                    HrAve_X.append(val)
                UnitVal_X = []

            if pasthour != Thour:
                self.x = 0
                self.total = 0
                for n in UnitVal_X:
                    if (isinstance(n, (int, float))):
                        self.x += n
                        self.total +=1
                if (self.total>0):
                    val = round(self.x / self.total,2)
                    DayAve_X.append(val)
                HrAve_X = []


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
                if(x >0):
                    if (x==1):
                        UnitVal_1[1].append(float(y))
                        if pastminute != Tminute:
                            self.x = 0
                            self.total = 0
                            for n in UnitVal_1[1]:
                                if (isinstance(n, (int, float))):
                                    self.x += n
                                    #print(self.x)
                                    self.total +=1
                                    #print(self.total)
                            if (self.total>0):
                                val = round(self.x / self.total,2)
                                HrAve_U1[1].append(val)
                            UnitVal_1[1] = []

                    elif(x==2):
                        UnitVal_1[2].append(float(y))
                        if pastminute != Tminute:
                            self.x = 0
                            self.total = 0
                            for n in UnitVal_1[2]:
                                if (isinstance(n, (int, float))):
                                    self.x += n
                                    self.total +=1
                            if (self.total>0):
                                val = round(self.x / self.total,2)
                                HrAve_U1[2].append(val)
                            UnitVal_1[2] = []

                    elif(x==3):
                        UnitVal_1[3].append(float(y))
                        if pastminute != Tminute:
                            self.x = 0
                            self.total = 0
                            for n in UnitVal_1[3]:
                                if (isinstance(n, (int, float))):
                                    self.x += n
                                    self.total +=1
                            if (self.total>0):
                                val = round(self.x / self.total,2)
                                HrAve_U1[3].append(val)
                            UnitVal_1[3] = []

                    elif(x==4):
                        UnitVal_1[4].append(float(y))
                        if pastminute != Tminute:
                            self.x = 0
                            self.total = 0
                            for n in UnitVal_1[4]:
                                if (isinstance(n, (int, float))):
                                    self.x += n
                                    self.total +=1
                            if (self.total>0):
                                val = round(self.x / self.total,2)
                                HrAve_U1[4].append(val)
                            UnitVal_1[4] = []

                    elif(x==5):
                        UnitVal_1[5].append(float(y))
                        if pastminute != Tminute:
                            self.x = 0
                            self.total = 0
                            for n in UnitVal_1[5]:
                                if (isinstance(n, (int, float))):
                                    self.x += n
                                    self.total +=1
                            if (self.total>0):
                                val = round(self.x / self.total,2)
                                HrAve_U1[5].append(val)
                            UnitVal_1[5] = []

                    elif(x==6):
                        UnitVal_1[6].append(float(y))
                        if pastminute != Tminute:
                            self.x = 0
                            self.total = 0
                            for n in UnitVal_1[6]:
                                if (isinstance(n, (int, float))):
                                    self.x += n
                                    self.total +=1
                            if (self.total>0):
                                val = round(self.x / self.total,2)
                                HrAve_U1[6].append(val)
                            UnitVal_1[6] = []

                    elif(x==7):
                        UnitVal_1[7].append(float(y))
                        if pastminute != Tminute:
                            self.x = 0
                            self.total = 0
                            for n in UnitVal_1[7]:
                                if (isinstance(n, (int, float))):
                                    self.x += n
                                    self.total +=1
                            if (self.total>0):
                                val = round(self.x / self.total,2)
                                HrAve_U1[7].append(val)
                            UnitVal_1[7] = []

                    elif(x==8):
                        UnitVal_1[8].append(float(y))
                        if pastminute != Tminute:
                            self.x = 0
                            self.total = 0
                            for n in UnitVal_1[8]:
                                if (isinstance(n, (int, float))):
                                    self.x += n
                                    self.total +=1
                            if (self.total>0):
                                val = round(self.x / self.total,2)
                                HrAve_U1[8].append(val)
                            UnitVal_1[8] = []

                    elif(x==9):
                        UnitVal_1[9].append(float(y))
                        if pastminute != Tminute:
                            self.x = 0
                            self.total = 0
                            for n in UnitVal_1[9]:
                                if (isinstance(n, (int, float))):
                                    self.x += n
                                    self.total +=1
                            if (self.total>0):
                                val = round(self.x / self.total,2)
                                HrAve_U1[9].append(val)
                            UnitVal_1[9] = []

                    elif(x==10):
                        UnitVal_1[10].append(float(y))
                        if pastminute != Tminute:
                            self.x = 0
                            self.total = 0
                            for n in UnitVal_1[10]:
                                if (isinstance(n, (int, float))):
                                    self.x += n
                                    self.total +=1
                            if (self.total>0):
                                val = round(self.x / self.total,2)
                                HrAve_U1[10].append(val)
                            UnitVal_1[10] = []

                    elif(x==11):
                        UnitVal_1[11].append(float(y))
                        if pastminute != Tminute:
                            self.x = 0
                            self.total = 0
                            for n in UnitVal_1[11]:
                                if (isinstance(n, (int, float))):
                                    self.x += n
                                    self.total +=1
                            if (self.total>0):
                                val = round(self.x / self.total,2)
                                HrAve_U1[11].append(val)
                            UnitVal_1[11] = []

                    elif(x==12):
                        UnitVal_1[12].append(float(y))
                        if pastminute != Tminute:
                            self.x = 0
                            self.total = 0
                            for n in UnitVal_1[12]:
                                if (isinstance(n, (int, float))):
                                    self.x += n
                                    self.total +=1
                            if (self.total>0):
                                val = round(self.x / self.total,2)
                                HrAve_U1[12].append(val)
                            UnitVal_1[12] = []

                    elif(x==13):
                        UnitVal_1[13].append(float(y))
                        if pastminute != Tminute:
                            self.x = 0
                            self.total = 0
                            for n in UnitVal_1[13]:
                                if (isinstance(n, (int, float))):
                                    self.x += n
                                    self.total +=1
                            if (self.total>0):
                                val = round(self.x / self.total,2)
                                HrAve_U1[13].append(val)
                            UnitVal_1[13] = []

                    elif(x==14):
                        UnitVal_1[14].append(float(y))
                        if pastminute != Tminute:
                            self.x = 0
                            self.total = 0
                            for n in UnitVal_1[14]:
                                if (isinstance(n, (int, float))):
                                    self.x += n
                                    self.total +=1
                            if (self.total>0):
                                val = round(self.x / self.total,2)
                                HrAve_U1[14].append(val)
                            UnitVal_1[14] = []

                    #print(UnitVal_1)

        elif unitRef == "U2":
            self.currentVals = self.output
            self.currentVals = self.currentVals.split(',')
            for x, y in enumerate(self.currentVals):
                y = y.replace(" ", "")
                if(x >0):
                    if (x==1):
                        UnitVal_2[1].append(float(y))
                        if pastminute != Tminute:
                            self.x = 0
                            self.total = 0
                            for n in UnitVal_2[1]:
                                if (isinstance(n, (int, float))):
                                    self.x += n
                                    #print(self.x)
                                    self.total +=1
                                    #print(self.total)
                            if (self.total>0):
                                val = round(self.x / self.total,2)
                                HrAve_U2[1].append(val)
                            UnitVal_2[1] = []

                    elif(x==2):
                        UnitVal_2[2].append(float(y))
                        if pastminute != Tminute:
                            self.x = 0
                            self.total = 0
                            for n in UnitVal_2[2]:
                                if (isinstance(n, (int, float))):
                                    self.x += n
                                    self.total +=1
                            if (self.total>0):
                                val = round(self.x / self.total,2)
                                HrAve_U2[2].append(val)
                            UnitVal_2[2] = []

                    elif(x==3):
                        UnitVal_2[3].append(float(y))
                        if pastminute != Tminute:
                            self.x = 0
                            self.total = 0
                            for n in UnitVal_2[3]:
                                if (isinstance(n, (int, float))):
                                    self.x += n
                                    self.total +=1
                            if (self.total>0):
                                val = round(self.x / self.total,2)
                                HrAve_U2[3].append(val)
                            UnitVal_2[3] = []

                    elif(x==4):
                        UnitVal_2[4].append(float(y))
                        if pastminute != Tminute:
                            self.x = 0
                            self.total = 0
                            for n in UnitVal_2[4]:
                                if (isinstance(n, (int, float))):
                                    self.x += n
                                    self.total +=1
                            if (self.total>0):
                                val = round(self.x / self.total,2)
                                HrAve_U2[4].append(val)
                            UnitVal_2[4] = []

                    elif(x==5):
                        UnitVal_2[5].append(float(y))
                        if pastminute != Tminute:
                            self.x = 0
                            self.total = 0
                            for n in UnitVal_2[5]:
                                if (isinstance(n, (int, float))):
                                    self.x += n
                                    self.total +=1
                            if (self.total>0):
                                val = round(self.x / self.total,2)
                                HrAve_U2[5].append(val)
                            UnitVal_2[5] = []

                    elif(x==6):
                        UnitVal_2[6].append(float(y))
                        if pastminute != Tminute:
                            self.x = 0
                            self.total = 0
                            for n in UnitVal_2[6]:
                                if (isinstance(n, (int, float))):
                                    self.x += n
                                    self.total +=1
                            if (self.total>0):
                                val = round(self.x / self.total,2)
                                HrAve_U2[6].append(val)
                            UnitVal_2[6] = []

                    elif(x==7):
                        UnitVal_2[7].append(float(y))
                        if pastminute != Tminute:
                            self.x = 0
                            self.total = 0
                            for n in UnitVal_2[7]:
                                if (isinstance(n, (int, float))):
                                    self.x += n
                                    self.total +=1
                            if (self.total>0):
                                val = round(self.x / self.total,2)
                                HrAve_U2[7].append(val)
                            UnitVal_2[7] = []

                    elif(x==8):
                        UnitVal_2[8].append(float(y))
                        if pastminute != Tminute:
                            self.x = 0
                            self.total = 0
                            for n in UnitVal_2[8]:
                                if (isinstance(n, (int, float))):
                                    self.x += n
                                    self.total +=1
                            if (self.total>0):
                                val = round(self.x / self.total,2)
                                HrAve_U2[8].append(val)
                            UnitVal_2[8] = []

                    elif(x==9):
                        UnitVal_2[9].append(float(y))
                        if pastminute != Tminute:
                            self.x = 0
                            self.total = 0
                            for n in UnitVal_2[9]:
                                if (isinstance(n, (int, float))):
                                    self.x += n
                                    self.total +=1
                            if (self.total>0):
                                val = round(self.x / self.total,2)
                                HrAve_U2[9].append(val)
                            UnitVal_2[9] = []

                    elif(x==10):
                        UnitVal_2[10].append(float(y))
                        if pastminute != Tminute:
                            self.x = 0
                            self.total = 0
                            for n in UnitVal_2[10]:
                                if (isinstance(n, (int, float))):
                                    self.x += n
                                    self.total +=1
                            if (self.total>0):
                                val = round(self.x / self.total,2)
                                HrAve_U2[10].append(val)
                            UnitVal_2[10] = []

                    elif(x==11):
                        UnitVal_2[11].append(float(y))
                        if pastminute != Tminute:
                            self.x = 0
                            self.total = 0
                            for n in UnitVal_2[11]:
                                if (isinstance(n, (int, float))):
                                    self.x += n
                                    self.total +=1
                            if (self.total>0):
                                val = round(self.x / self.total,2)
                                HrAve_U2[11].append(val)
                            UnitVal_2[11] = []

                    elif(x==12):
                        UnitVal_2[12].append(float(y))
                        if pastminute != Tminute:
                            self.x = 0
                            self.total = 0
                            for n in UnitVal_2[12]:
                                if (isinstance(n, (int, float))):
                                    self.x += n
                                    self.total +=1
                            if (self.total>0):
                                val = round(self.x / self.total,2)
                                HrAve_U2[12].append(val)
                            UnitVal_2[12] = []

                    elif(x==13):
                        UnitVal_2[13].append(float(y))
                        if pastminute != Tminute:
                            self.x = 0
                            self.total = 0
                            for n in UnitVal_2[13]:
                                if (isinstance(n, (int, float))):
                                    self.x += n
                                    self.total +=1
                            if (self.total>0):
                                val = round(self.x / self.total,2)
                                HrAve_U2[13].append(val)
                            UnitVal_2[13] = []

                    elif(x==14):
                        UnitVal_2[14].append(float(y))
                        if pastminute != Tminute:
                            self.x = 0
                            self.total = 0
                            for n in UnitVal_2[14]:
                                if (isinstance(n, (int, float))):
                                    self.x += n
                                    self.total +=1
                            if (self.total>0):
                                val = round(self.x / self.total,2)
                                HrAve_U2[14].append(val)
                            UnitVal_2[14] = []

                    #print(UnitVal_2)

        elif unitRef == "U3":
            self.currentVals = self.output
            self.currentVals = self.currentVals.split(',')
            for x, y in enumerate(self.currentVals):
                y = y.replace(" ", "")
                if(x >0):
                    if (x==1):
                        UnitVal_3[1].append(float(y))
                        if pastminute != Tminute:
                            self.x = 0
                            self.total = 0
                            for n in UnitVal_3[1]:
                                if (isinstance(n, (int, float))):
                                    self.x += n
                                    #print(self.x)
                                    self.total +=1
                                    #print(self.total)
                            if (self.total>0):
                                val = round(self.x / self.total,2)
                                HrAve_U3[1].append(val)
                            UnitVal_3[1] = []

                    elif(x==2):
                        UnitVal_3[2].append(float(y))
                        if pastminute != Tminute:
                            self.x = 0
                            self.total = 0
                            for n in UnitVal_3[2]:
                                if (isinstance(n, (int, float))):
                                    self.x += n
                                    self.total +=1
                            if (self.total>0):
                                val = round(self.x / self.total,2)
                                HrAve_U3[2].append(val)
                            UnitVal_3[2] = []

                    elif(x==3):
                        UnitVal_3[3].append(float(y))
                        if pastminute != Tminute:
                            self.x = 0
                            self.total = 0
                            for n in UnitVal_3[3]:
                                if (isinstance(n, (int, float))):
                                    self.x += n
                                    self.total +=1
                            if (self.total>0):
                                val = round(self.x / self.total,2)
                                HrAve_U3[3].append(val)
                            UnitVal_3[3] = []

                    elif(x==4):
                        UnitVal_3[4].append(float(y))
                        if pastminute != Tminute:
                            self.x = 0
                            self.total = 0
                            for n in UnitVal_3[4]:
                                if (isinstance(n, (int, float))):
                                    self.x += n
                                    self.total +=1
                            if (self.total>0):
                                val = round(self.x / self.total,2)
                                HrAve_U3[4].append(val)
                            UnitVal_3[4] = []

                    elif(x==5):
                        UnitVal_3[5].append(float(y))
                        if pastminute != Tminute:
                            self.x = 0
                            self.total = 0
                            for n in UnitVal_3[5]:
                                if (isinstance(n, (int, float))):
                                    self.x += n
                                    self.total +=1
                            if (self.total>0):
                                val = round(self.x / self.total,2)
                                HrAve_U3[5].append(val)
                            UnitVal_3[5] = []

                    elif(x==6):
                        UnitVal_3[6].append(float(y))
                        if pastminute != Tminute:
                            self.x = 0
                            self.total = 0
                            for n in UnitVal_3[6]:
                                if (isinstance(n, (int, float))):
                                    self.x += n
                                    self.total +=1
                            if (self.total>0):
                                val = round(self.x / self.total,2)
                                HrAve_U3[6].append(val)
                            UnitVal_3[6] = []

                    elif(x==7):
                        UnitVal_3[7].append(float(y))
                        if pastminute != Tminute:
                            self.x = 0
                            self.total = 0
                            for n in UnitVal_3[7]:
                                if (isinstance(n, (int, float))):
                                    self.x += n
                                    self.total +=1
                            if (self.total>0):
                                val = round(self.x / self.total,2)
                                HrAve_U3[7].append(val)
                            UnitVal_3[7] = []

                    elif(x==8):
                        UnitVal_3[8].append(float(y))
                        if pastminute != Tminute:
                            self.x = 0
                            self.total = 0
                            for n in UnitVal_3[8]:
                                if (isinstance(n, (int, float))):
                                    self.x += n
                                    self.total +=1
                            if (self.total>0):
                                val = round(self.x / self.total,2)
                                HrAve_U3[8].append(val)
                            UnitVal_3[8] = []

                    elif(x==9):
                        UnitVal_3[9].append(float(y))
                        if pastminute != Tminute:
                            self.x = 0
                            self.total = 0
                            for n in UnitVal_3[9]:
                                if (isinstance(n, (int, float))):
                                    self.x += n
                                    self.total +=1
                            if (self.total>0):
                                val = round(self.x / self.total,2)
                                HrAve_U3[9].append(val)
                            UnitVal_3[9] = []

                    elif(x==10):
                        UnitVal_3[10].append(float(y))
                        if pastminute != Tminute:
                            self.x = 0
                            self.total = 0
                            for n in UnitVal_3[10]:
                                if (isinstance(n, (int, float))):
                                    self.x += n
                                    self.total +=1
                            if (self.total>0):
                                val = round(self.x / self.total,2)
                                HrAve_U3[10].append(val)
                            UnitVal_3[10] = []

                    elif(x==11):
                        UnitVal_3[11].append(float(y))
                        if pastminute != Tminute:
                            self.x = 0
                            self.total = 0
                            for n in UnitVal_3[11]:
                                if (isinstance(n, (int, float))):
                                    self.x += n
                                    self.total +=1
                            if (self.total>0):
                                val = round(self.x / self.total,2)
                                HrAve_U3[11].append(val)
                            UnitVal_3[11] = []

                    elif(x==12):
                        UnitVal_3[12].append(float(y))
                        if pastminute != Tminute:
                            self.x = 0
                            self.total = 0
                            for n in UnitVal_3[12]:
                                if (isinstance(n, (int, float))):
                                    self.x += n
                                    self.total +=1
                            if (self.total>0):
                                val = round(self.x / self.total,2)
                                HrAve_U3[12].append(val)
                            UnitVal_3[12] = []

                    elif(x==13):
                        UnitVal_3[13].append(float(y))
                        if pastminute != Tminute:
                            self.x = 0
                            self.total = 0
                            for n in UnitVal_3[13]:
                                if (isinstance(n, (int, float))):
                                    self.x += n
                                    self.total +=1
                            if (self.total>0):
                                val = round(self.x / self.total,2)
                                HrAve_U3[13].append(val)
                            UnitVal_3[13] = []

                    elif(x==14):
                        UnitVal_3[14].append(float(y))
                        if pastminute != Tminute:
                            self.x = 0
                            self.total = 0
                            for n in UnitVal_3[14]:
                                if (isinstance(n, (int, float))):
                                    self.x += n
                                    self.total +=1
                            if (self.total>0):
                                val = round(self.x / self.total,2)
                                HrAve_U3[14].append(val)
                            UnitVal_3[14] = []

                    #print(UnitVal_3)

        elif unitRef == "U4":
            self.currentVals = self.output
            self.currentVals = self.currentVals.split(',')
            for x, y in enumerate(self.currentVals):
                y = y.replace(" ", "")
                if(x >0):
                    if (x==1):
                        UnitVal_4[1].append(float(y))
                        if pastminute != Tminute:
                            self.x = 0
                            self.total = 0
                            for n in UnitVal_4[1]:
                                if (isinstance(n, (int, float))):
                                    self.x += n
                                    #print(self.x)
                                    self.total +=1
                                    #print(self.total)
                            if (self.total>0):
                                val = round(self.x / self.total,2)
                                HrAve_U4[1].append(val)
                            UnitVal_4[1] = []

                    elif(x==2):
                        UnitVal_4[2].append(float(y))
                        if pastminute != Tminute:
                            self.x = 0
                            self.total = 0
                            for n in UnitVal_4[2]:
                                if (isinstance(n, (int, float))):
                                    self.x += n
                                    self.total +=1
                            if (self.total>0):
                                val = round(self.x / self.total,2)
                                HrAve_U4[2].append(val)
                            UnitVal_4[2] = []

                    elif(x==3):
                        UnitVal_4[3].append(float(y))
                        if pastminute != Tminute:
                            self.x = 0
                            self.total = 0
                            for n in UnitVal_4[3]:
                                if (isinstance(n, (int, float))):
                                    self.x += n
                                    self.total +=1
                            if (self.total>0):
                                val = round(self.x / self.total,2)
                                HrAve_U4[3].append(val)
                            UnitVal_4[3] = []

                    elif(x==4):
                        UnitVal_4[4].append(float(y))
                        if pastminute != Tminute:
                            self.x = 0
                            self.total = 0
                            for n in UnitVal_4[4]:
                                if (isinstance(n, (int, float))):
                                    self.x += n
                                    self.total +=1
                            if (self.total>0):
                                val = round(self.x / self.total,2)
                                HrAve_U4[4].append(val)
                            UnitVal_4[4] = []

                    elif(x==5):
                        UnitVal_4[5].append(float(y))
                        if pastminute != Tminute:
                            self.x = 0
                            self.total = 0
                            for n in UnitVal_4[5]:
                                if (isinstance(n, (int, float))):
                                    self.x += n
                                    self.total +=1
                            if (self.total>0):
                                val = round(self.x / self.total,2)
                                HrAve_U4[5].append(val)
                            UnitVal_4[5] = []

                    elif(x==6):
                        UnitVal_4[6].append(float(y))
                        if pastminute != Tminute:
                            self.x = 0
                            self.total = 0
                            for n in UnitVal_4[6]:
                                if (isinstance(n, (int, float))):
                                    self.x += n
                                    self.total +=1
                            if (self.total>0):
                                val = round(self.x / self.total,2)
                                HrAve_U4[6].append(val)
                            UnitVal_4[6] = []

                    elif(x==7):
                        UnitVal_4[7].append(float(y))
                        if pastminute != Tminute:
                            self.x = 0
                            self.total = 0
                            for n in UnitVal_4[7]:
                                if (isinstance(n, (int, float))):
                                    self.x += n
                                    self.total +=1
                            if (self.total>0):
                                val = round(self.x / self.total,2)
                                HrAve_U4[7].append(val)
                            UnitVal_4[7] = []

                    elif(x==8):
                        UnitVal_4[8].append(float(y))
                        if pastminute != Tminute:
                            self.x = 0
                            self.total = 0
                            for n in UnitVal_4[8]:
                                if (isinstance(n, (int, float))):
                                    self.x += n
                                    self.total +=1
                            if (self.total>0):
                                val = round(self.x / self.total,2)
                                HrAve_U4[8].append(val)
                            UnitVal_4[8] = []

                    elif(x==9):
                        UnitVal_4[9].append(float(y))
                        if pastminute != Tminute:
                            self.x = 0
                            self.total = 0
                            for n in UnitVal_4[9]:
                                if (isinstance(n, (int, float))):
                                    self.x += n
                                    self.total +=1
                            if (self.total>0):
                                val = round(self.x / self.total,2)
                                HrAve_U4[9].append(val)
                            UnitVal_4[9] = []

                    elif(x==10):
                        UnitVal_4[10].append(float(y))
                        if pastminute != Tminute:
                            self.x = 0
                            self.total = 0
                            for n in UnitVal_4[10]:
                                if (isinstance(n, (int, float))):
                                    self.x += n
                                    self.total +=1
                            if (self.total>0):
                                val = round(self.x / self.total,2)
                                HrAve_U4[10].append(val)
                            UnitVal_4[10] = []

                    elif(x==11):
                        UnitVal_4[11].append(float(y))
                        if pastminute != Tminute:
                            self.x = 0
                            self.total = 0
                            for n in UnitVal_4[11]:
                                if (isinstance(n, (int, float))):
                                    self.x += n
                                    self.total +=1
                            if (self.total>0):
                                val = round(self.x / self.total,2)
                                HrAve_U4[11].append(val)
                            UnitVal_4[11] = []

                    elif(x==12):
                        UnitVal_4[12].append(float(y))
                        if pastminute != Tminute:
                            self.x = 0
                            self.total = 0
                            for n in UnitVal_4[12]:
                                if (isinstance(n, (int, float))):
                                    self.x += n
                                    self.total +=1
                            if (self.total>0):
                                val = round(self.x / self.total,2)
                                HrAve_U4[12].append(val)
                            UnitVal_4[12] = []

                    elif(x==13):
                        UnitVal_4[13].append(float(y))
                        if pastminute != Tminute:
                            self.x = 0
                            self.total = 0
                            for n in UnitVal_4[13]:
                                if (isinstance(n, (int, float))):
                                    self.x += n
                                    self.total +=1
                            if (self.total>0):
                                val = round(self.x / self.total,2)
                                HrAve_U4[13].append(val)
                            UnitVal_4[13] = []

                    elif(x==14):
                        UnitVal_4[14].append(float(y))
                        if pastminute != Tminute:
                            self.x = 0
                            self.total = 0
                            for n in UnitVal_4[14]:
                                if (isinstance(n, (int, float))):
                                    self.x += n
                                    self.total +=1
                            if (self.total>0):
                                val = round(self.x / self.total,2)
                                HrAve_U4[14].append(val)
                            UnitVal_4[14] = []

                    #print(UnitVal_4)

        elif unitRef == "U5":
            self.currentVals = self.output
            self.currentVals = self.currentVals.split(',')
            for x, y in enumerate(self.currentVals):
                y = y.replace(" ", "")
                if(x >0):
                    if (x==1):
                        everyminute(UnitVal_5[1],HrAve_U5[1],DayAve_U5[1])

                        # UnitVal_5[1].append(float(y))
                        # if pastminute != Tminute:
                        #     self.x = 0
                        #     self.total = 0
                        #     for n in UnitVal_5[1]:
                        #         if (isinstance(n, (int, float))):
                        #             self.x += n
                        #             #print(self.x)
                        #             self.total +=1
                        #             #print(self.total)
                        #     if (self.total>0):
                        #         val = round(self.x / self.total,2)
                        #         HrAve_U5[1].append(val)
                        #     UnitVal_5[1] = []

                        # if pasthour != Thour:
                        #     self.x = 0
                        #     self.total = 0
                        #     for n in HrAve_U5[1]:
                        #         if (isinstance(n, (int, float))):
                        #             self.x += n
                        #             self.total +=1
                        #     if (self.total>0):
                        #         val = round(self.x / self.total,2)
                        #         DayAve_U5[1].append(val)
                        #     HrAve_U5[1] = []


                    elif(x==2):
                        everyminute(UnitVal_5[2],HrAve_U5[2],DayAve_U5[2])
                        # UnitVal_5[2].append(float(y))
                        # if pastminute != Tminute:
                        #     self.x = 0
                        #     self.total = 0
                        #     for n in UnitVal_5[2]:
                        #         if (isinstance(n, (int, float))):
                        #             self.x += n
                        #             self.total +=1
                        #     if (self.total>0):
                        #         val = round(self.x / self.total,2)
                        #         HrAve_U5[2].append(val)
                        #     UnitVal_5[2] = []
                        #
                        # if pasthour != Thour:
                        #     self.x = 0
                        #     self.total = 0
                        #     for n in HrAve_U5[2]:
                        #         if (isinstance(n, (int, float))):
                        #             self.x += n
                        #             self.total +=1
                        #     if (self.total>0):
                        #         val = round(self.x / self.total,2)
                        #         DayAve_U5[2].append(val)
                        #     HrAve_U5[2] = []

                    elif(x==3):
                        everyminute(UnitVal_5[3],HrAve_U5[3],DayAve_U5[3])
                        # UnitVal_5[3].append(float(y))
                        # if pastminute != Tminute:
                        #     self.x = 0
                        #     self.total = 0
                        #     for n in UnitVal_5[3]:
                        #         if (isinstance(n, (int, float))):
                        #             self.x += n
                        #             self.total +=1
                        #     if (self.total>0):
                        #         val = round(self.x / self.total,2)
                        #         HrAve_U5[3].append(val)
                        #     UnitVal_5[3] = []
                        #
                        # if pasthour != Thour:
                        #     self.x = 0
                        #     self.total = 0
                        #     for n in HrAve_U5[3]:
                        #         if (isinstance(n, (int, float))):
                        #             self.x += n
                        #             self.total +=1
                        #     if (self.total>0):
                        #         val = round(self.x / self.total,2)
                        #         DayAve_U5[3].append(val)
                        #     HrAve_U5[3] = []

                    elif(x==4):
                        everyminute(UnitVal_5[4],HrAve_U5[4],DayAve_U5[4])
                        # UnitVal_5[4].append(float(y))
                        # if pastminute != Tminute:
                        #     self.x = 0
                        #     self.total = 0
                        #     for n in UnitVal_5[4]:
                        #         if (isinstance(n, (int, float))):
                        #             self.x += n
                        #             self.total +=1
                        #     if (self.total>0):
                        #         val = round(self.x / self.total,2)
                        #         HrAve_U5[4].append(val)
                        #     UnitVal_5[4] = []
                        #
                        # if pasthour != Thour:
                        #     self.x = 0
                        #     self.total = 0
                        #     for n in HrAve_U5[4]:
                        #         if (isinstance(n, (int, float))):
                        #             self.x += n
                        #             self.total +=1
                        #     if (self.total>0):
                        #         val = round(self.x / self.total,2)
                        #         DayAve_U5[4].append(val)
                        #     HrAve_U5[4] = []

                    elif(x==5):
                        everyminute(UnitVal_5[5],HrAve_U5[5],DayAve_U5[5])
                        # UnitVal_5[5].append(float(y))
                        # if pastminute != Tminute:
                        #     self.x = 0
                        #     self.total = 0
                        #     for n in UnitVal_5[5]:
                        #         if (isinstance(n, (int, float))):
                        #             self.x += n
                        #             self.total +=1
                        #     if (self.total>0):
                        #         val = round(self.x / self.total,2)
                        #         HrAve_U5[5].append(val)
                        #     UnitVal_5[5] = []
                        #
                        # if pasthour != Thour:
                        #     self.x = 0
                        #     self.total = 0
                        #     for n in HrAve_U5[5]:
                        #         if (isinstance(n, (int, float))):
                        #             self.x += n
                        #             self.total +=1
                        #     if (self.total>0):
                        #         val = round(self.x / self.total,2)
                        #         DayAve_U5[5].append(val)
                        #     HrAve_U5[5] = []

                    elif(x==6):
                        everyminute(UnitVal_5[6],HrAve_U5[6],DayAve_U5[6])
                        # UnitVal_5[6].append(float(y))
                        # if pastminute != Tminute:
                        #     self.x = 0
                        #     self.total = 0
                        #     for n in UnitVal_5[6]:
                        #         if (isinstance(n, (int, float))):
                        #             self.x += n
                        #             self.total +=1
                        #     if (self.total>0):
                        #         val = round(self.x / self.total,2)
                        #         HrAve_U5[6].append(val)
                        #     UnitVal_5[6] = []
                        #
                        # if pasthour != Thour:
                        #     self.x = 0
                        #     self.total = 0
                        #     for n in HrAve_U5[6]:
                        #         if (isinstance(n, (int, float))):
                        #             self.x += n
                        #             self.total +=1
                        #     if (self.total>0):
                        #         val = round(self.x / self.total,2)
                        #         DayAve_U5[6].append(val)
                        #     HrAve_U5[6] = []

                    elif(x==7):
                        UnitVal_5[7].append(float(y))
                        if pastminute != Tminute:
                            self.x = 0
                            self.total = 0
                            for n in UnitVal_5[7]:
                                if (isinstance(n, (int, float))):
                                    self.x += n
                                    self.total +=1
                            if (self.total>0):
                                val = round(self.x / self.total,2)
                                HrAve_U5[7].append(val)
                            UnitVal_5[7] = []

                        if pasthour != Thour:
                            self.x = 0
                            self.total = 0
                            for n in HrAve_U5[7]:
                                if (isinstance(n, (int, float))):
                                    self.x += n
                                    self.total +=1
                            if (self.total>0):
                                val = round(self.x / self.total,2)
                                DayAve_U5[7].append(val)
                            HrAve_U5[7] = []

                    elif(x==8):
                        UnitVal_5[8].append(float(y))
                        if pastminute != Tminute:
                            self.x = 0
                            self.total = 0
                            for n in UnitVal_5[8]:
                                if (isinstance(n, (int, float))):
                                    self.x += n
                                    self.total +=1
                            if (self.total>0):
                                val = round(self.x / self.total,2)
                                HrAve_U5[8].append(val)
                            UnitVal_5[8] = []

                        if pasthour != Thour:
                            self.x = 0
                            self.total = 0
                            for n in HrAve_U5[8]:
                                if (isinstance(n, (int, float))):
                                    self.x += n
                                    self.total +=1
                            if (self.total>0):
                                val = round(self.x / self.total,2)
                                DayAve_U5[8].append(val)
                            HrAve_U5[8] = []

                    elif(x==9):
                        UnitVal_5[9].append(float(y))
                        if pastminute != Tminute:
                            self.x = 0
                            self.total = 0
                            for n in UnitVal_5[9]:
                                if (isinstance(n, (int, float))):
                                    self.x += n
                                    self.total +=1
                            if (self.total>0):
                                val = round(self.x / self.total,2)
                                HrAve_U5[9].append(val)
                            UnitVal_5[9] = []

                        if pasthour != Thour:
                            self.x = 0
                            self.total = 0
                            for n in HrAve_U5[9]:
                                if (isinstance(n, (int, float))):
                                    self.x += n
                                    self.total +=1
                            if (self.total>0):
                                val = round(self.x / self.total,2)
                                DayAve_U5[9].append(val)
                            HrAve_U5[9] = []

                    elif(x==10):
                        UnitVal_5[10].append(float(y))
                        if pastminute != Tminute:
                            self.x = 0
                            self.total = 0
                            for n in UnitVal_5[10]:
                                if (isinstance(n, (int, float))):
                                    self.x += n
                                    self.total +=1
                            if (self.total>0):
                                val = round(self.x / self.total,2)
                                HrAve_U5[10].append(val)
                            UnitVal_5[10] = []

                        if pasthour != Thour:
                            self.x = 0
                            self.total = 0
                            for n in HrAve_U5[10]:
                                if (isinstance(n, (int, float))):
                                    self.x += n
                                    self.total +=1
                            if (self.total>0):
                                val = round(self.x / self.total,2)
                                DayAve_U5[10].append(val)
                            HrAve_U5[10] = []

                    elif(x==11):
                        UnitVal_5[11].append(float(y))
                        if pastminute != Tminute:
                            self.x = 0
                            self.total = 0
                            for n in UnitVal_5[11]:
                                if (isinstance(n, (int, float))):
                                    self.x += n
                                    self.total +=1
                            if (self.total>0):
                                val = round(self.x / self.total,2)
                                HrAve_U5[11].append(val)
                            UnitVal_5[11] = []

                        if pasthour != Thour:
                            self.x = 0
                            self.total = 0
                            for n in HrAve_U5[11]:
                                if (isinstance(n, (int, float))):
                                    self.x += n
                                    self.total +=1
                            if (self.total>0):
                                val = round(self.x / self.total,2)
                                DayAve_U5[11].append(val)
                            HrAve_U5[11] = []

                    elif(x==12):
                        UnitVal_5[12].append(float(y))
                        if pastminute != Tminute:
                            self.x = 0
                            self.total = 0
                            for n in UnitVal_5[12]:
                                if (isinstance(n, (int, float))):
                                    self.x += n
                                    self.total +=1
                            if (self.total>0):
                                val = round(self.x / self.total,2)
                                HrAve_U5[12].append(val)
                            UnitVal_5[12] = []

                        if pasthour != Thour:
                            self.x = 0
                            self.total = 0
                            for n in HrAve_U5[12]:
                                if (isinstance(n, (int, float))):
                                    self.x += n
                                    self.total +=1
                            if (self.total>0):
                                val = round(self.x / self.total,2)
                                DayAve_U5[12].append(val)
                            HrAve_U5[12] = []

                    elif(x==13):
                        UnitVal_5[13].append(float(y))
                        if pastminute != Tminute:
                            self.x = 0
                            self.total = 0
                            for n in UnitVal_5[13]:
                                if (isinstance(n, (int, float))):
                                    self.x += n
                                    self.total +=1
                            if (self.total>0):
                                val = round(self.x / self.total,2)
                                HrAve_U5[13].append(val)
                            UnitVal_5[13] = []

                        if pasthour != Thour:
                            self.x = 0
                            self.total = 0
                            for n in HrAve_U5[13]:
                                if (isinstance(n, (int, float))):
                                    self.x += n
                                    self.total +=1
                            if (self.total>0):
                                val = round(self.x / self.total,2)
                                DayAve_U5[13].append(val)
                            HrAve_U5[13] = []

                    elif(x==14):
                        UnitVal_5[14].append(float(y))
                        if pastminute != Tminute:
                            self.x = 0
                            self.total = 0
                            for n in UnitVal_5[14]:
                                if (isinstance(n, (int, float))):
                                    self.x += n
                                    self.total +=1
                            if (self.total>0):
                                val = round(self.x / self.total,2)
                                HrAve_U5[14].append(val)
                            UnitVal_5[14] = []

                        if pasthour != Thour:
                            self.x = 0
                            self.total = 0
                            for n in HrAve_U5[14]:
                                if (isinstance(n, (int, float))):
                                    self.x += n
                                    self.total +=1
                            if (self.total>0):
                                val = round(self.x / self.total,2)
                                DayAve_U5[14].append(val)
                            HrAve_U5[14] = []

                    #print(UnitVal_5)






        elif unitRef == "U6":
            UnitVal_6 = self.output
        elif unitRef == "U7":
            UnitVal_7 = self.output
        elif unitRef == "U8":
            UnitVal_8 = self.output
        elif unitRef == "U9":
            UnitVal_9 = self.output
        elif unitRef == "U10":
            UnitVal_10 = self.output

        print("Result: " + str(UnitValues))
        pastminute = Tminute
        pasthour = Thour
        #print("Past Minute:"+str(pastminute))
        print("Day Ave U5: " + str(DayAve_U5))
