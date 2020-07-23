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

# This opens up a software automatically to show the feed. Uses the other A/D converter
subprocess.Popen("\"C:\\Program Files (x86)\\Deskshare\\IP Camera Viewer 4\\IP Camera Viewer.exe\"")
class videoRecord:
    def __init__(self, master):
        # Get todays date
        todaysDate = time.strftime("%m/%d/%Y")
        dropvar = StringVar(master)
        dropvar.set("custom")  # PY_VAR0
        # GUI size
        master.geometry("450x400")

        ################################# DEFINE WIDGETS AND BUTTONS ##########################################

        # Date widgets
        self.Date_label = Label(master, text="Date")
        self.Date = Label(master, text=todaysDate)
        # Protocol browse label and button
        self.protocol_label = Label(master, text="Select a Protocol")
        self.protocol_button = Button(master, text="Browse", command=self.browse_button)
        # Main Data Folder for Dropbox       
        self.mainDataFold_label = Label(master, text="Data Folder")
        self.mainDataFold_name = Label(master, text="Select a protocol json")
        # Experiment Folder for dropbox
        self.experiment_label = Label(master, text="Experiment")
        self.experiment_name = Label(master, text="Select a protocol json")
        # Selected protocol Folder for dropbox
        self.selected_label = Label(master, text="Selected Protocol")
        self.selected_name = Label(master, text ="Select a protocol json")
        # Subject ID widgets
        self.subjectID_label = Label(master, text="SubjectID")
        self.subjectID = Entry(master)
        # Video Name widgets
        self.nameID_label = Label(master, text="Video Name")
        self.nameID = Entry(master)
        # Arrow buttons
        self.arrowleft = Button(master, text="<-", command=self.leftarw)
        self.arrowright = Button(master, text="->", command=self.righarw)
        # First output space
        self.outputDir_label = Label(master, text="First Output Location")
        self.outputDir = Entry(master)
        # Video length
        self.length_label = Label(master, text="Video Length")
        self.length = Entry(master)
        self.length.insert(END, "")
        self.length_tail = Label(master, text="sec")
        # Video format
        self.vidFormat_label = Label(master, text="Video Format")
        self.vidFormat = Entry(master)
        self.vidFormat.insert(END, "mjpeg")
        # Video containers (extension)
        self.vidContainer_label = Label(master, text="Container Format")
        self.vidContainer = Entry(master)
        self.vidContainer.insert(END, "mov")
        # Video scale
        self.vidScale_label = Label(master, text="Video Scale")
        self.vidScale = Entry(master)
        self.vidScale.insert(END, '640x480')
        # Framerate
        self.frameRate_label = Label(master, text="Frame Rate")
        self.frameRate = Entry(master)
        self.frameRate_tail = Label(master, text="fps")
        self.frameRate.insert(END, '29.97')
        # Startbutton
        self.startbutton = Button(master, text="Start", command=self.recordVid)

        ################################## PLACE WIDGETS AND BUTTONS ##############################################

        # Date row 0 column 0&1
        self.Date_label.grid(row=0, column=0, sticky=NSEW)
        self.Date.grid(row=0, column=1, sticky=NSEW)
        # Protocol browse buttons row 1 column 0&1
        self.protocol_label.grid(row=1, column=0, sticky=NSEW)
        self.protocol_button.grid(row=1, column=1, sticky=NSEW)      
        # Main data information
        self.mainDataFold_label.grid(row=2, column=0, sticky=NSEW)
        self.mainDataFold_name.grid(row=2, column=1, sticky=NSEW)
        # Experiment information
        self.experiment_label.grid(row=3, column=0, sticky=NSEW)
        self.experiment_name.grid(row=3, column=1, sticky=NSEW)
        # Protocol information
        self.selected_label.grid(row=4, column=0, sticky=NSEW)
        self.selected_name.grid(row=4, column=1, sticky=NSEW)
        # Subject ID stuff
        self.subjectID_label.grid(row=5, column=0, sticky=NSEW)
        self.subjectID.grid(row=5, column=1, sticky=NSEW)
        # Video Name Stuff
        self.nameID_label.grid(row=6, column=0, sticky=NSEW)
        self.nameID.grid(row=6, column=1, sticky=NSEW)
        self.arrowleft.grid(row=6, column=2, sticky=NSEW)
        self.arrowright.grid(row=6, column=3, sticky=NSEW)
        # Output
        self.outputDir_label.grid(row=7, column=0, sticky=NSEW)
        self.outputDir.grid(row=7, column=1, sticky=NSEW)
        # Length
        self.length_label.grid(row=8, column=0, sticky=NSEW)
        self.length.grid(row=8, column=1, sticky=NSEW)
        self.length_tail.grid(row=8, column=2, sticky=NSEW)
        # Format
        self.vidFormat_label.grid(row=9, column=0, sticky=NSEW)
        self.vidFormat.grid(row=9, column=1, sticky=NSEW)
        # Container (extension)
        self.vidContainer_label.grid(row=10, column=0, sticky=NSEW)
        self.vidContainer.grid(row=10, column=1, sticky=NSEW)
        # Scake
        self.vidScale_label.grid(row=11, column=0, sticky=NSEW)
        self.vidScale.grid(row=11, column=1, sticky=NSEW)
        # Framerate
        self.frameRate_label.grid(row=12, column=0, sticky=NSEW)
        self.frameRate.grid(row=12, column=1, sticky=NSEW)
        self.frameRate_tail.grid(row=12, column=2, sticky=NSEW)
        # Start button
        self.startbutton.grid(row=13, column=1, sticky=NSEW)

        # Some column size specifications
        master.columnconfigure(0, weight=1)
        master.columnconfigure(1, weight=1)
        master.rowconfigure(0, weight=1)
        master.rowconfigure(1, weight=1)
        master.rowconfigure(2, weight=1)
        master.rowconfigure(3, weight=1)
        master.rowconfigure(4, weight=1)
        master.rowconfigure(5, weight=1)
        master.rowconfigure(6, weight=1)
        master.rowconfigure(7, weight=1)
        master.rowconfigure(8, weight=1)
        master.rowconfigure(9, weight=1)
        master.rowconfigure(10, weight=1)
        master.rowconfigure(11, weight=1)
        master.rowconfigure(12, weight=1)
        master.rowconfigure(13, weight=1)
        
    def browse_button(self):
        root.filename = filedialog.askopenfilename(initialdir="/", title="Select file",
                                                   filetypes=(("json files", "*.json"), ("all files", "*.*")))
        with open(root.filename) as config_file:
            job_config = json.load(config_file)
            mainDataFolder = job_config['mainDataFolder']
            experiment = job_config['experiment']
            outputz = job_config['initialOutputPath']
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
            self.mainDataFold_name.config(text=mainDataFolder)
            self.experiment_name.config(text=experiment)
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

    def saveVid(self): 
        # Get some paths
        cnt = self.vidContainer.get()
        outdir = self.outputDir.get()        
        
        # Get the main folder, experiment, and protocol name
        folder_name = self.mainDataFold_name.cget('text')
        exp_name = self.experiment_name.cget('text')
        protocol_name = self.selected_name.cget('text')
        existing_subj_folder = 'C:\\Users\\LDOG_experimenter\\"Dropbox (Aguirre-Brainard Lab)"\\%s\\Experiments\\%s\\%s\\Videos' % (folder_name, exp_name, protocol_name)
        # THIS LINE IS FOR TESTING: existing_subj_folder = 'C:\\Users\\ozenc\\Desktop\\%s\\Videos' % protocol_name
        
        # If this new protocol does not exist, create it 
        if not os.path.exists(existing_subj_folder):
            os.system('mkdir %s' % existing_subj_folder)
        
        # Get date mm/dd/YY
        today = date.today()
        date_of_scan = today.strftime("%Y-%m-%d")

        # Get name of the video 
        name = self.subjectID.get() 
        savefolder = os.path.join(existing_subj_folder, name, date_of_scan)
        if not os.path.exists(savefolder):
            os.system('mkdir %s' % savefolder)
        fresh_vid_name = id_vid + '.' + cnt
        freshvid = os.path.join(outdir, fresh_vid_name)
        
        # If the video exists in the dropbox path, add _dup to the file name
        if os.path.exists(os.path.join(savefolder, fresh_vid_name)):
            modded_new_name = id_vid + '_dup01' + '.' + cnt        
            if os.path.exists(os.path.join(savefolder, modded_new_name)):
                modded_new_name = id_vid + '_dup02' + '.' + cnt
                if os.path.exists(os.path.join(savefolder, modded_new_name)):
                    modded_new_name = id_vid + '_dup03' + '.' + cnt
                    if os.path.exists(os.path.join(savefolder, modded_new_name)):
                        modded_new_name = id_vid + '_dup04' + '.' + cnt
                        if os.path.exists(os.path.join(savefolder, modded_new_name)):
                            modded_new_name = id_vid + '_dup05' + '.' + cnt  
                            if os.path.exists(os.path.join(savefolder, modded_new_name)):
                                modded_new_name = id_vid + '_dup06' + '.' + cnt
            save_path = os.path.join(savefolder, modded_new_name)                
        else:
            save_path = os.path.join(savefolder, fresh_vid_name)
        
        # Save the video to Dropbox
        process = 'copy %s %s' % (freshvid, save_path)
        print(process)
        os.system(process)
        
    def recordVid(self):
        global id_vid
        global outputname
        global cnt
        global outdir
        
        id_vid = self.nameID.get()
        ln = self.length.get()
        frmt = self.vidFormat.get()
        cnt = self.vidContainer.get()
        scl = self.vidScale.get()
        fr = self.frameRate.get()
        outdir = self.outputDir.get()
        outputname = "%s\%s.%s" % (outdir, id_vid, cnt)

        if ln == '':
            command = 'ffmpeg -f dshow -rtbufsize 1500M -i video="Decklink Video Capture":audio="Decklink Audio Capture" -c:v %s -q:v 0 -y -vf scale=%s -r %s %s' % (
            frmt, scl, fr, outputname)
        else:
            command = 'ffmpeg -f dshow -rtbufsize 1500M -i video="Decklink Video Capture":audio="Decklink Audio Capture" -c:v %s -q:v 0 -y -vf scale=%s -r %s -t %s %s' % (
            frmt, scl, fr, ln, outputname)
            
        # THIS LINE IS FOR TESTING WITH THE LAPTOP CAMERA:
        command = 'ffmpeg -f dshow -rtbufsize 1500M -i video="FaceTime HD Camera" -c:v %s -q:v 0 -y -vf scale=%s -r %s -t %s %s' % (frmt, scl, fr, ln, outputname)
        os.system(command)
        print('Saving the video to  Dropbox')
        self.saveVid()
    
    def updatesMELA(self):
        self.outputDir.insert(END, outputz)

root = Tk()
root.title('GKAguirreLab Video Recorder')
obj = videoRecord(root)
root.mainloop()
