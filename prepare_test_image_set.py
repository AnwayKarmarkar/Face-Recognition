import numpy as np  
import cv2
import os, os.path
import datetime
from tkinter import *
from tkinter.filedialog import  *
import tkinter.messagebox

def prepare_test_im(imageDir, faceCascade = "", faceCascade2 = ""):
    tkinter.messagebox.showinfo(title='WAIT',message="FINDING FACES FROM IMAGE..")
    now = datetime.datetime.now()
    folder_name = now.strftime("%d-%m-%y")
    cnt = 1
    image_path_list = []
    valid_image_extensions = [".jpg", ".jpeg", ".png", ".tif", ".tiff"] 
    valid_image_extensions = [item.lower() for item in valid_image_extensions]

    for file in os.listdir(imageDir):
        extension = os.path.splitext(file)[1]
        if extension.lower() not in valid_image_extensions:
            continue
        image_path_list.append(os.path.join(imageDir, file))

    for img_path in image_path_list:
        image = cv2.imread(img_path)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        # Detect faces in the image
        #for scale in [float(i)/10 for i in range(11, 13)]:
        #for neighbors in range(2,4):
        faces = faceCascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=2,minSize=(100,100))
        print("Faces {0} found".format(len(faces)))
        faceCount=format(len(faces))
        messageString=faceCount+" Faces Found"
        tkinter.messagebox.showinfo(title='SUCCESS',message=messageString)
        #Draw a rectangle around the faces  
        for (x, y, w, h) in faces:
            img1 = cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),5)
            #Cropping the images
            path = "test/"+folder_name
            if not os.path.exists(path):
               os.mkdir(path)
            cv2.imwrite("test/"+str(folder_name)+"/Image"+ str(cnt) + ".jpg", gray[y:(y)+(h+15),x:(x)+(w+15)])
            cnt = cnt + 1
            resized = cv2.resize(img1,(800,640), interpolation = cv2.INTER_AREA)
            cv2.imshow("Faces found", resized)
            
        faces2 = faceCascade2.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=2,minSize=(100,100))
        print("Faces {0} found".format(len(faces2)))
        faceCount=format(len(faces2))
        messageString=faceCount+" Faces Found"
        tkinter.messagebox.showinfo(title='SUCCESS',message=messageString)
        #Draw a rectangle around the faces  
        for (x, y, w, h) in faces2:
            img2 = cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),5)
            #Cropping the images
            path = "test/"+folder_name
            if not os.path.exists(path):
               os.mkdir(path)
            cv2.imwrite("test/"+str(folder_name)+"/Image"+ str(cnt) + ".jpg", gray[y:(y)+(h+15),x:(x)+(w+15)])
            cnt = cnt + 1
            resized2 = cv2.resize(img2,(800,640), interpolation = cv2.INTER_AREA)
            cv2.imshow("Faces found", resized2)

if __name__ == "__main__":
    # Create the haar cascade
    cascPath = "haarcascade_frontalface_alt.xml"
    cascPath2 = "haarcascade_profileface.xml"
    faceCascade = cv2.CascadeClassifier(cascPath)
    faceCascade2 = cv2.CascadeClassifier(cascPath2)
    browseFile = askdirectory(title = "Choose Your Image")
    prepare_test_im(browseFile, faceCascade = faceCascade, faceCascade2 = faceCascade2)
    #resized = cv2.resize(image,(800,640), interpolation = cv2.INTER_AREA)
    #cv2.imshow("Faces found", resized)  
    cv2.waitKey(0)            
