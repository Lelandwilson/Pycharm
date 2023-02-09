from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort
import os

UserList = []
UsersFile = "setup/Users.txt"

FaildLogins = []


app = Flask(__name__)
 
@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return "Hello Boss!  <a href='/logout'>Logout</a>"
 
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
            print "<Users.txt file not found>"
            print "<Creating Users.txt with default user credentials>"
            f1 = open(UsersFile,'w')
            f1.write("<USERS>")
            f1.close()


class SaveUsers():

    def __init__(self):
        global UsersFile
        global UserList

        #User:Password
        print "<SaveSettings_Pwds>"

        if (not os.path.exists(UsersFile)):
            print "<Pwds File does not exist>"
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
                print "<Users File Updated>"
            except:
                print "Error in saving- Users File could not be updated"

            f1.close()

        except:
            print "*<Error- ["+ str(UsersFile) + "] not found, Please create>*"



if __name__ == "__main__":
    loadUsers()
    app.secret_key = os.urandom(12)
    app.run(debug=True,host='127.0.0.1', port=4000)


