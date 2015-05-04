#!/usr/bin/python3
# -*- coding: utf-8 -*-
from tkinter import *
from tkinter import ttk
import SpudScale
from ConfigReader import configReader
import threading

UPDATETIME = 1.0

class GUI():

    def __init__(self):
        """init Tk"""
        root = Tk()
        root.title("Spud Scale")
        content = ttk.Frame(root).grid(column=0, row=0, sticky=(N, S, E, W))

        """init config info"""
        configInfo = configReader()
        self.inputTitle = configInfo['input']
        self.orderedNames = configInfo['ordered']

        """init self variables"""
        self.spudScale = SpudScale.SpudScale()
        self.currentValues = self.spudScale.getCurrentValues()
        self.plotLabel = StringVar()
        self.numRecorded = 0

        """init lables"""
        #inputTitleLabel
        titleLabel = ttk.Label(content, text=self.inputTitle, anchor="center").grid(column = 0,row = 0, sticky=(N, W))
        #plotEntry
        plotEntry = ttk.Entry(content, textvariable = self.plotLabel).grid(column = 0, row = 1, sticky=(N, W))
        #recordButton
        recordButton = ttk.Button(content, text="Record ->", command = self.record).grid(column = 1, row = 1, sticky=(N, W))
        #newButton
        newButton = ttk.Button(content, text="New...", command = self.newFile).grid(column = 3, row = 1)
        #last5PlotsLabel
        last5PlotsLabel = ttk.Label(content, text='Last 5 Plots', anchor='center').grid(column = 4, row= 2)
        #liveValuesLabel
        liveValuesLabel = ttk.Label(content, text='Live Values', anchor='center').grid(column = 0, row= 3)
        #secondTitleLabel
        secondTitleLabel = ttk.Label(content, text=self.inputTitle, anchor="center").grid(column = 1,row = 3)

        secondTitleLabel = ttk.Label(content, text=self.inputTitle, anchor="center").grid(column = 1,row = 3)
        secondTitleLabel = ttk.Label(content, text=self.inputTitle, anchor="center").grid(column = 2,row = 3)
        secondTitleLabel = ttk.Label(content, text=self.inputTitle, anchor="center").grid(column = 3,row = 3)
        secondTitleLabel = ttk.Label(content, text=self.inputTitle, anchor="center").grid(column = 4,row = 3)
        secondTitleLabel = ttk.Label(content, text=self.inputTitle, anchor="center").grid(column = 5,row = 3)

        #begin threaded loop for updating current scale values
        self.RUNNING = True
        self.startTimer()
        #begin Tk's mainloop
        root.mainloop()
        #end threaded loop
        self.RUNNING = False

    def newFile(self):
        from tkinter import filedialog
        fileName = filedialog.asksaveasfilename()
        self.spudScale.setFileName(fileName)

    def record(self):
        self.numRecorded += 1
        if(self.numRecorded % 5 == 0) :
            self.spudScale.updateLastFiveRecorded()
        self.spudScale.record(self.plotLabel.get())

    def startTimer(self):
        if self.RUNNING:
            t = threading.Timer(UPDATETIME, self.startTimer)
            t.start()
            self.currentValues = self.spudScale.getCurrentValues()

def main() :
    gui = GUI()

if __name__ == '__main__':
    main()
