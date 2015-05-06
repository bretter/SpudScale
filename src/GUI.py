#!/usr/bin/python3
# -*- coding: utf-8 -*-
from tkinter import *
from tkinter import ttk
import SpudScale
from ConfigReader import configReader
import threading
from tkinter import font

UPDATETIME = 0.1

class GUI():

    def __init__(self):
        """init Tk"""
        root = Tk()
        root.title("SpudScale")
        root.resizable(0,0)
        root.option_add('*tearOff', FALSE)
        content = ttk.Frame(root).grid(column=0, row=0, sticky=(N, S, E, W))

        """init config info"""
        configInfo = configReader()
        self.inputTitle = configInfo['input']
        self.orderedNames = configInfo['ordered']

        """init self variables"""
        self.spudScale = SpudScale.SpudScale()
        self.currentValues = [StringVar() for i in range(10)]
        self.lastFiveValuesList = [[StringVar() for i in range(11)] for j in range(5)]
        self.plotLabel = StringVar()
        self.fileName = StringVar()
        self.fileName.set(self.spudScale.fileName)

        """init font"""
        labelFont = font.Font(family='system', size=10, weight='bold')
        fileFont = font.Font(family='system', size=10, slant='italic')

        """init menubar"""
        menubar = Menu(root)
        root['menu'] = menubar
        menu_file = Menu(menubar)
        menu_edit = Menu(menubar)
        menubar.add_cascade(menu=menu_file, label='File')
        menu_file.add_command(label='New', command=self.newFile)

        """init lables"""
        #input Title Label
        titleLabel = ttk.Label(content, text=self.inputTitle, anchor="center",width=10,font=labelFont).grid(column = 0,row = 0, sticky=(N, W))
        #current File Label
        currentFileLabel = ttk.Label(content, text='Current File: ', anchor="center",width=10,font=labelFont).grid(column = 3,row = 0,columnspan=3, sticky=(N, S, E, W))
        #File Label
        fileLabel = ttk.Label(content, textvariable=self.fileName, anchor="center",width=10,relief='sunken',font=fileFont).grid(column = 2,row = 1,columnspan=6, sticky=(N, S, E, W))
        #plot Entry
        plotEntry = ttk.Entry(content, textvariable = self.plotLabel,width=10,takefocus=1).grid(column = 0, row = 1, sticky=(N, W))
        #record Button
        recordButton = ttk.Button(content, text="Record ->", command = self.record).grid(column = 1, row = 1, sticky=(N, W))
        #last 5 Plots Label
        last5PlotsLabel = ttk.Label(content, text='Last 5 Plots', anchor='center',font=labelFont).grid(column = 3, row= 2, columnspan=3, sticky=(N, S, E, W))
        #live Values Label
        liveValuesLabel = ttk.Label(content, text='Live Values', anchor='center',font=labelFont).grid(column = 0, row= 3, sticky=(N, S, E, W))
        #second Title Label
        secondTitleLabel = ttk.Label(content, text=self.inputTitle, anchor="center").grid(column = 1,row = 3)
        #live value labels
        liveValueLabels = [ttk.Label(content, textvariable=self.currentValues[l], anchor="center", background='white',relief='sunken',width=12).grid(column = 0,row = l + 4) for l in range(10)]
        #ordered names' labels
        orderedNamesLabels = [ttk.Label(content, text=self.orderedNames[l], anchor="center",relief='ridge',width=12).grid(column = 1,row = l + 4) for l in range(10)]
        #history value labels
        for c in range (5):
            historyValueLabels = [ttk.Label(content, textvariable=self.lastFiveValuesList[c][l], anchor="center",relief='ridge',width=12, background='white').grid(column = c + 2,row = l + 3) for l in range(11)]

        #focus on plot entry (not working?)
        #bind enter to record button
        root.bind('<Return>', self.record)


        #begin threaded loop for updating current scale values
        self.RUNNING = True
        self.startTimer()
        #begin Tk's mainloop
        root.mainloop()
        #end threaded loop
        self.RUNNING = False

    def newFile(self):
        from tkinter import filedialog
        fileName = filedialog.askopenfilename(filetypes=(("Comma Seperated Value", "*.csv")
                                                         ,("Text", "*.txt")
                                                         ,("All files", "*.*")))
        self.spudScale.setFileName(fileName)
        self.fileName.set(self.spudScale.fileName)

    def updateLastFive(self):
        lastFive = self.spudScale.getLastFiveRecorded()
        for c in range(5):
            for r in range(11):
                self.lastFiveValuesList[c][r].set(lastFive[c][r])

    def record(self,*args):
        self.spudScale.record(self.plotLabel.get())
        self.updateLastFive()
        self.plotLabel.set('')

    def startTimer(self):
        if self.RUNNING:
            t = threading.Timer(UPDATETIME, self.startTimer)
            t.daemon = True
            t.start()
            i = 0
            for w in self.spudScale.getCurrentValues():
                self.currentValues[i].set(w)
                i += 1

def main() :
    gui = GUI()

if __name__ == '__main__':
    main()
