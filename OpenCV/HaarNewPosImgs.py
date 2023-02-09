import os
import time

currentfile = ''
currentfile_extension = ''
fileLoc = '50_50bids'
Posimgs_fileLoc = fileLoc +'/'+ 'Posimgs/'
numberOfPics = 100
# PosInfo_file = 'info'+ currentfile_noExtension + 'lst'

# CommandString = 'opencv_createsamples -img '+ fileLoc+ '/' + currentfile + ' -bg bg.txt -info ' + fileLoc +'/' + Posimgs_fileLoc+ '/' + PosInfo_file + ' -pngoutput 12mmBirds/Posimgs -maxxangle .5 -maxyangle .5 -maxzangle .5 -num 100'
def create_pos_imgs():
    for file_type in [fileLoc]:

        for img in os.listdir(file_type):
            #print"File:" + str(img)
            currentfile = str(img)
            index1 = currentfile.find('.')
            currentfile_noExtension = currentfile[0:index1]
            currentfile_extension = currentfile[index1:]
            #print currentfile_noExtension
            #print currentfile_extension

            PosInfo_file = 'info'+ currentfile_noExtension + '.lst'
            CommandString = 'opencv_createsamples -img '+ fileLoc+ '/' + currentfile + ' -bg bg.txt -info ' + Posimgs_fileLoc + PosInfo_file + ' -pngoutput '+ Posimgs_fileLoc + ' -maxxangle .5 -maxyangle .5 -maxzangle .5 -num '+ str(numberOfPics)

            print (CommandString)
            #os.system(CommandString)
            time.sleep(0.5)


create_pos_imgs()
