from tkinter import *
from tkinter.filedialog import  *
import tkinter.messagebox
import tkinter as tk
from tkinter import ttk
from time import sleep
import sys
#from tkinter import tk
from math import sqrt
from sklearn import neighbors
import numpy as np  
import cv2
import os
from os import listdir, mkdir
from os.path import isdir, join, isfile, splitext, exists
import datetime
import pickle
from PIL import Image, ImageFont, ImageDraw, ImageEnhance
import face_recognition
from face_recognition import face_locations
from face_recognition.cli import image_files_in_folder
import tkinter
from PIL import Image
from PIL import ImageTk
from openpyxl import Workbook, load_workbook

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

window = tkinter.Tk()
window.geometry("{0}x{1}+0+0".format(window.winfo_screenwidth(),window.winfo_screenheight()))
background = PhotoImage(file="BG.png")
BGLabel = Label(window, image=background)
BGLabel.place(x=0,y=0,relwidth=1,relheight=1)

#logString="\nATTENDANCE MANAGEMENT SYSTEM\n"
logLabel = Label(text="\nAUTOMATED  ATTENDANCE  SYSTEM\n",bg="black",fg="white",font=12)
logLabel.pack(side=TOP,fill=X)
#window.minsize(height=window.winfo_height(), width=window.winfo_width())

def crop():
    exec(open("prepare_test_image_set.py").read())
def train():
    exec(open("Knn_training.py").read())
def mark_att():
    exec(open("Knn_algo.py").read())
def create_dataset():
    exec(open("Dataset_Generator.py").read())
def show():
    file = "Attendance Records\Attendance.xlsx"
    os.startfile(file)


    

b1=Button(window, text='GENERATE DATASET', font=2, command=create_dataset, width=20, height=2, bg="black", foreground="white", bd=10)
b1.place( x=100, y= 150 )

b2=Button(window, text='TRAINING', font=2, command=train, width=20, height=2, bg="black", foreground="white", bd=10)
b2.place( x=100, y= 250 )

b3=Button(window, text='UPLOAD IMAGE', font=2,  command=crop, width=20, height=2, bg="black", foreground="white", bd=10)
b3.place( x=100, y= 350 )

b4=Button(window, text='MARK ATTENDANCE', font=2, command=mark_att, width=20, height=2, bg="black", foreground="white", bd=10)
b4.place( x=100, y= 450 )

b5=Button(window, text='SHOW ATTENDANCE', font=2, command=show, width=20, height=2, bg="black", foreground="white", bd=10)
b5.place( x=100, y= 550 )

