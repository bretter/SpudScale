#!/usr/bin/python3
# -*- coding: utf-8 -*-
from tkinter import *
from tkinter import ttk
import SpudScale
from ConfigReader import configReader
import threading

UPDATETIME = 0.01

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
        self.currentValues = [StringVar() for i in range(10)]
        self.lastFiveValuesList = [[StringVar() for i in range(11)] for j in range(5)]
        self.plotLabel = StringVar()

        """init lables"""
        #input Title Label
        titleLabel = ttk.Label(content, text=self.inputTitle, anchor="center").grid(column = 0,row = 0, sticky=(N, W))
        #plot Entry
        plotEntry = ttk.Entry(content, textvariable = self.plotLabel,width=10).grid(column = 0, row = 1, sticky=(N, W))
        #record Button
        recordButton = ttk.Button(content, text="Record ->", command = self.record).grid(column = 1, row = 1, sticky=(N, W))
        #new Button
        newButton = ttk.Button(content, text="New...", command = self.newFile).grid(column = 3, row = 1)
        #last 5 Plots Label
        last5PlotsLabel = ttk.Label(content, text='Last 5 Plots', anchor='center').grid(column = 4, row= 2)
        #live Values Label
        liveValuesLabel = ttk.Label(content, text='Live Values', anchor='center').grid(column = 0, row= 3)
        #second Title Label
        secondTitleLabel = ttk.Label(content, text=self.inputTitle, anchor="center").grid(column = 1,row = 3)
        #live value labels
        liveValueLabels = [ttk.Label(content, textvariable=self.currentValues[l], anchor="center", background='white',relief='sunken',width=10).grid(column = 0,row = l + 4) for l in range(10)]
        #ordered names' labels
        orderedNamesLabels = [ttk.Label(content, text=self.orderedNames[l], anchor="center",relief='ridge',width=10).grid(column = 1,row = l + 4) for l in range(10)]
        #history value labels
        for c in range (5):
            historyValueLabels = [ttk.Label(content, textvariable=self.lastFiveValuesList[c][l], anchor="center",relief='ridge',width=10, background='white').grid(column = c + 2,row = l + 3) for l in range(11)]

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

    def updateLastFive(self):
        for c in range(4,0,-1):
            for r in range(11):
                self.lastFiveValuesList[c][r].set(self.lastFiveValuesList[c - 1][r].get())

        self.lastFiveValuesList[0][0].set(self.plotLabel.get())
        for w in range (10):
            self.lastFiveValuesList[0][w + 1].set(self.spudScale.getCurrentValues()[w])

    def record(self):
        self.updateLastFive()
        self.spudScale.record(self.plotLabel.get())
        self.plotLabel.set('')

    def startTimer(self):
        if self.RUNNING:
            t = threading.Timer(UPDATETIME, self.startTimer)
            t.start()
            i = 0
            for w in self.spudScale.getCurrentValues():
                self.currentValues[i].set(w)
                i += 1

def main() :
    gui = GUI()

if __name__ == '__main__':
    main()
