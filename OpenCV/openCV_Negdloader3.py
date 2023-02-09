#import urllib2
from six.moves import urllib
import cv2
import numpy as np
import os
import time
import urllib2
import sys
pingTimeout = 5
complete = False
directory = 'neg200/'

def store_raw_images():
    neg_images_link = 'http://image-net.org/api/text/imagenet.synset.geturls?wnid=n14977504'
    neg_image_urls = urllib.request.urlopen(neg_images_link).read().decode()

    pic_num = 845


    if not os.path.exists(directory):
        os.makedirs(directory)

    for i in neg_image_urls.split('\n'):
        try:
            #print(i)
            request = urllib2.urlopen(i, directory + str(pic_num)+".jpg", timeout=5)
            with open(directory + str(pic_num)+".jpg", 'wb') as f:
                try:
                    f.write(request.read())
                    img = cv2.imread(directory + str(pic_num)+".jpg",cv2.IMREAD_GRAYSCALE)
                    # should be larger than samples / pos pic (so we can place our image on it)
                    resized_image = cv2.resize(img, (250, 250))
                    cv2.imwrite(directory + str(pic_num)+".jpg",resized_image)
                    #cv2.imshow("image", resized_image)
                    print ("Saved file no: " + str(pic_num))
                    pic_num += 1
                except:
                    print("error")




        except Exception as e:
            print(str(e))

        if pic_num >= 1000:
            sys.exit()


store_raw_images()

