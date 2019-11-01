from tkinter import *
from tkinter.filedialog import  *
import tkinter.messagebox
#************************DETECTION***********************************

def faceDetect():
    browseFile = askopenfilename(parent = root,title = "Choose Your Image")
    if len(browseFile)==0:
        tkinter.messagebox.showinfo(title='ERROR',text="PROBLEM IN LOADING IMAGE")
    else:   
        tkinter.messagebox.showinfo('NOTICE',"Image Loaded Successfully")
        answer = tkinter.messagebox.askquestion('Proceed?', "Run Face Detection?")
        if answer == 'yes':
            detection(browseFile)
            
def detection(fileName):
    print(fileName)
    tkinter.messagebox.showinfo('SUCCESS!',"Faces Detected And Cropped from "+fileName)
    
#***********************ATTENDANCE***********************************

def markAttendance():
    browseFile = askdirectory(title = "Choose the Folder")
    if len(browseFile)==0:
        tkinter.messagebox.showinfo(title='ERROR',text="CANNOT LOAD THE FOLDER")
    else:   
        answer = tkinter.messagebox.askquestion('Proceed?', "Do you wish to mark attendance?")
        if answer == 'yes':
            attendance(browseFile)
def attendance(dirName):
    print(dirName)
    tkinter.messagebox.showinfo('SUCCESS!',"Attendance Marked from "+dirName)

#***********************TRAIN DATA***********************************

def trainData():
    lines = [' - The training data is ready',' - .pkl file has been prepared','Proceed to Face Detection']
    tkinter.messagebox.showinfo('NOTICE',"\n".join(lines))

#***********************CREATE DATASET***********************************

def createDataset():

    def startCamera():
        print("First Name: %s\nLast Name: %s" % (e1.get(), e2.get()))

    master = Tk()
    Label(master, text="Name").grid(row=0)
    Label(master, text="Roll Number").grid(row=1)

    e1 = Entry(master)
    e2 = Entry(master)

    e1.grid(row=0, column=1)
    e2.grid(row=1, column=1)

    Button(master, text='Quit', command=master.quit).grid(row=3, column=0, sticky=W, pady=4)
    Button(master, text='Show', command=startCamera).grid(row=3, column=1, sticky=W, pady=4)

    master.mainloop()

#***********************GUI MAIN***********************************#

root = Tk()
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(),root.winfo_screenheight()))
background = PhotoImage(file="BG.png")
BGLabel = Label(root, image=background)
BGLabel.place(x=0,y=0,relwidth=1,relheight=1)

#textFrame = Frame(width=100,height=40)
#textFrame.pack(side=TOP)

logString="\nATTENDANCE MANAGEMENT SYSTEM\n"
logLabel = Label(text=logString,bg="yellow")
logLabel.pack(side=TOP,fill=X,anchor=W,)

buttonFrame = Frame()
buttonFrame.pack(side=BOTTOM)

button1 = Button(buttonFrame, text="Mark Attendance", width=40, height=10, command=markAttendance)
button2 = Button(buttonFrame, text="Detect Faces", width=40, height=10, command=faceDetect)
button3 = Button(buttonFrame, text="Train Dataset", width=40, height=10, command=trainData)
button4 = Button(buttonFrame, text="Create Dataset", width=40, height=10, command=createDataset)
button1.grid(row=1,column=0)
button2.grid(row=2,column=0)
button3.grid(row=3,column=0)
button4.grid(row=4,column=0)

root.mainloop()