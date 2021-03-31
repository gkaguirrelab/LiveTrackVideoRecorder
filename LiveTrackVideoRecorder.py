from tkinter import *
from tkinter import filedialog
import time
from datetime import date
import subprocess
import os
import json
from pyautogui import hotkey
import sys

# This is a script which record videos with custom settings
# Works with ffmpeg

subprocess.Popen("\"C:\\Program Files (x86)\\Deskshare\\IP Camera Viewer 4\\IP Camera Viewer.exe\"") #Set this path to IP Camera Viever
class videoRecord:
    def __init__(self, master):
        todaysDate = time.strftime("%m/%d/%Y")
        dropvar = StringVar(master)
        dropvar.set("custom")  # PY_VAR0
        master.geometry("300x300")

        self.Date_label = Label(master, text="Date")
        self.Date = Label(master, text=todaysDate)
        self.protocol_label = Label(master, text="Protocol")
        self.protocol_button = Button(master, text="Browse", command=self.browse_button)
        self.selected_label = Label(master, text="Selected")
        self.selected_name = Label(master, text ="None")
        self.subjectID_label = Label(master, text="SubjectID")
        self.subjectID = Entry(master)
        self.nameID_label = Label(master, text="Name")
        self.nameID = Entry(master)
        self.arrowleft = Button(master, text="<-", command=self.leftarw)
        self.arrowright = Button(master, text="->", command=self.righarw)
        self.outputDir_label = Label(master, text="Output Directory")
        self.outputDir = Entry(master)
        self.length_label = Label(master, text="Video Length")
        self.length = Entry(master)
        self.length.insert(END, "")
        self.length_tail = Label(master, text="sec")
        self.vidFormat_label = Label(master, text="Video Format")
        self.vidFormat = Entry(master)
        self.vidFormat.insert(END, "mjpeg")
        self.vidContainer_label = Label(master, text="Container Format")
        self.vidContainer = Entry(master)
        self.vidContainer.insert(END, "mov")
        self.vidScale_label = Label(master, text="Video Scale")
        self.vidScale = Entry(master)
        self.vidScale.insert(END, '640x480')
        self.frameRate_label = Label(master, text="Frame Rate")
        self.frameRate = Entry(master)
        self.frameRate_tail = Label(master, text="fps")
        self.frameRate.insert(END, '29.97')
        self.startbutton = Button(master, text="Start", command=self.recordVid)
        self.savebutton = Button(master, text="Save", command=self.saveVid)

        self.Date_label.grid(row=0, column=0, sticky=NSEW)
        self.Date.grid(row=0, column=1, sticky=NSEW)
        self.protocol_label.grid(row=1, column=0, sticky=NSEW)
        self.protocol_button.grid(row=1, column=1, sticky=NSEW)
        self.selected_label.grid(row=2, column=0, sticky=NSEW)
        self.selected_name.grid(row=2, column=1, sticky=NSEW)
        self.subjectID_label.grid(row=3, column=0, sticky=NSEW)
        self.subjectID.grid(row=3, column=1, sticky=NSEW)       
        self.nameID_label.grid(row=4, column=0, sticky=NSEW)
        self.nameID.grid(row=4, column=1, sticky=NSEW)
        self.arrowleft.grid(row=4, column=2, sticky=NSEW)
        self.arrowright.grid(row=4, column=3, sticky=NSEW)
        self.outputDir_label.grid(row=5, column=0, sticky=NSEW)
        self.outputDir.grid(row=5, column=1, sticky=NSEW)
        self.length_label.grid(row=6, column=0, sticky=NSEW)
        self.length.grid(row=6, column=1, sticky=NSEW)
        self.length_tail.grid(row=6, column=2, sticky=NSEW)
        self.vidFormat_label.grid(row=7, column=0, sticky=NSEW)
        self.vidFormat.grid(row=7, column=1, sticky=NSEW)
        self.vidContainer_label.grid(row=8, column=0, sticky=NSEW)
        self.vidContainer.grid(row=8, column=1, sticky=NSEW)
        self.vidScale_label.grid(row=9, column=0, sticky=NSEW)
        self.vidScale.grid(row=9, column=1, sticky=NSEW)
        self.frameRate_label.grid(row=10, column=0, sticky=NSEW)
        self.frameRate.grid(row=10, column=1, sticky=NSEW)
        self.frameRate_tail.grid(row=10, column=2, sticky=NSEW)
        self.startbutton.grid(row=11, column=1, sticky=NSEW)
        self.savebutton.grid(row=12, column=1, sticky=NSEW)

        master.columnconfigure(0, weight=1)
        master.columnconfigure(1, weight=1)
        master.rowconfigure(0, weight=1)
        master.rowconfigure(1, weight=1)
        master.rowconfigure(2, weight=1)
        master.rowconfigure(3, weight=1)
        master.rowconfigure(4, weight=1)
        master.rowconfigure(5, weight=1)

    def browse_button(self):
        root.filename = filedialog.askopenfilename(initialdir="/", title="Select file",
                                                   filetypes=(("json files", "*.json"), ("all files", "*.*")))
        with open(root.filename) as config_file:
            job_config = json.load(config_file)
            outputz = job_config['outputpath']
            rundict = job_config['runs']
            protname = job_config['protocol']
            global nameslist
            global lengthlist
            n = 0
            nameslist = list(rundict.keys())
            lengthlist = []
            for i in rundict.keys():
                lengthlist.append(list(rundict[i].values()))
            self.nameID.insert(END, nameslist[n])
            self.outputDir.insert(END, outputz)
            self.length.insert(END, lengthlist[n])
            #self.selected_name.delete(0,END)
            self.selected_name.config(text=protname)
        return n

    def righarw(self):
        getnameID = self.nameID.get()
        getfilledindex = nameslist.index(getnameID)
        getfilledindex = getfilledindex + 1
        self.nameID.delete(0,END)
        self.length.delete(0,END)
        self.nameID.insert(END, nameslist[getfilledindex])
        self.length.insert(END, lengthlist[getfilledindex])

    def leftarw(self):
        getnameID = self.nameID.get()
        getfilledindex = nameslist.index(getnameID)
        getfilledindex = getfilledindex - 1
        self.nameID.delete(0,END)
        self.length.delete(0,END)
        self.nameID.insert(END, nameslist[getfilledindex])
        self.length.insert(END, lengthlist[getfilledindex])

    def recordVid(self):
        global id
        global outputname
        global cnt
        global outdir
        
        id = self.nameID.get()
        ln = self.length.get()
        frmt = self.vidFormat.get()
        cnt = self.vidContainer.get()
        scl = self.vidScale.get()
        fr = self.frameRate.get()
        outdir = self.outputDir.get()
        outputname = "%s\%s.%s" % (outdir, id, cnt)

        if ln == '':
            command = 'ffmpeg -f dshow -rtbufsize 1500M -i video="Decklink Video Capture":audio="Decklink Audio Capture" -c:v %s -q:v 0 -y -vf scale=%s -r %s %s' % (
            frmt, scl, fr, outputname)
        else:
            command = 'ffmpeg -f dshow -rtbufsize 1500M -i video="Decklink Video Capture":audio="Decklink Audio Capture" -c:v %s -q:v 0 -y -vf scale=%s -r %s -t %s %s' % (
            frmt, scl, fr, ln, outputname)
        global p
        p = subprocess.Popen(command)
        return p
        return outputname
        return id
        return cnt
        
    def updatesMELA(self):
        self.outputDir.insert(END, outputz)

    def saveVid(self):
        p.kill()
        existing_subj_folder = 'C:\\Users\\LDOG_experimenter\\"Dropbox (Aguirre-Brainard Lab)"\\LDOG_data\\Experiments\\OLApproach_TrialSequenceMR\\MRScotoLDOG\\Videos'
        selected_path_name = self.selected_name.cget(("text"))
        if selected_path_name == 'AGTC':
            existing_subj_folder = 'C:\\Users\\LDOG_experimenter\\"Dropbox (Aguirre-Brainard Lab)"\\AGTC_data\\Videos'
        
        # Get date mm/dd/YY
        today = date.today()
        date_of_scan = today.strftime("%Y-%m-%d")

        # Get name of the video 
        name = self.subjectID.get() 
        savefolder = os.path.join(existing_subj_folder, name, date_of_scan)
        if not os.path.exists(savefolder):
            os.system('mkdir %s' % savefolder)
        freshvid = os.path.join(outdir,id + '.' + cnt)
        process = 'echo F|xcopy %s %s' % (freshvid, savefolder)
        print(process)
        os.system(process)

root = Tk()
root.title('GKAguirrelab Video Recorder')
obj = videoRecord(root)
root.mainloop()
