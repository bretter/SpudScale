#!/usr/bin/python3
# -*- coding: utf-8 -*-
from tkinter import *
from tkinter import ttk
import random
import threading

UPDATETIME = 1.0
RUNNING = True

class Readout:
    def __init__(self,plotLabel = "",weights = []):
        self.weights = []
        self.plotLabel = plotLabel
        if len(weights) > 0:
            for i in range(10):
                weight = StringVar()
                weight.set(weights[i].get())
                self.weights.append(weight)
        else:
            for w in range(10):
                r = random.random()
                self.weights.append(StringVar())

            for w in range(10):
                r = random.random()
                self.weights[w].set(str(int((r * 100))))

    def update(self):
        for w in range(10):
            r = random.random()
            self.weights[w].set(str(int((r * 100))))

    def setWeights(self,weights):
        for i in range(10):
            weight = StringVar()
            weight.set(weights[i])
            self.weights.append(weight)

    def getWeights(self):
        return self.weights

    def initLabels(self, window):
        self.TkWeightLabels = []
        self.TkScaleNumLabels = []
        self.scaleNumTitleLbl = ttk.Label(window, text="Scale #:", anchor="center", relief="solid")
        self.weightLbl = ttk.Label(window, text="Weight:", anchor="center", relief="solid")
        for l in range(10):
            self.TkScaleNumLabels.append(ttk.Label(window, text=str(l+1), anchor="center", relief="solid"))
            self.TkWeightLabels.append(ttk.Label(window, textvariable=self.weights[l], anchor="center", relief="solid"))

        for l in range(10):
            self.TkScaleNumLabels[l].grid(column=0, row=l+1, sticky=(N, S, E, W))
            self.TkWeightLabels[l].grid(column=1, row=l+1, sticky=(N, S, E, W))

        self.scaleNumTitleLbl.grid(column=0, row=0, sticky=(N, S, E, W))
        self.weightLbl.grid(column=1, row=0, sticky=(N, S, E, W))

    def setWindow(self, window):
        self.window = window

    def updateLabels(self):
        self.scaleNumTitleLbl.window = self.window
        self.weightLbl.window = self.window
        for l in range(10):
            self.TkScaleNumLabels.window = self.window
            self.TkWeightLabels.window = self.window



def record(*args):
    #create a new frame for the readout and set it in historyFrame
    newFrame = ttk.Frame(historyFrame, borderwidth=5, width=100, height=400)
    newFrame.grid(column=len(pastReadoutFrame), row=0, sticky=(N, S, E, W))
    #append it to pastReadoutFrames
    pastReadoutFrame.append(newFrame)
    for l in range(len(pastReadoutFrame)):
        pastReadoutFrame[l].columnconfigure(0, weight=1)
        for k in range(11):
            pastReadoutFrame[l].rowconfigure(k, weight=1)
    #create a copy of liveReadout and append it to pastReadouts
    SavedReadout = Readout(plotLbl,liveReadout.getWeights())
    SavedReadout.initLabels(pastReadoutFrame[len(pastReadoutFrame) - 1])
    pastReadouts.append(SavedReadout)

def update():
    if RUNNING:
        threading.Timer(UPDATETIME, update).start()
        liveReadout.update()

root = Tk()
root.title("Spud Scale")

"""Tk Variables"""
#Frames
#-ROOT Frames
content = ttk.Frame(root, padding=(3,3,12,12))
#-CONTENT Frames
liveFrame = ttk.Labelframe(content, borderwidth=5,  text="Live Values", width=100, height=400)
gridKeyFrame = ttk.Frame(content, borderwidth=1 ,relief="solid", width=100, height=400)
historyFrame = ttk.Labelframe(content, borderwidth=5, text="Plot Histroy", width=800, height=400)
#-HISTORY Frames
pastReadoutFrame = []

#Readout Objects
liveReadout = Readout()
liveReadout.initLabels(liveFrame)
pastReadouts = [] #for history

#Widgets in content
plotLbl = ttk.Label(content, text="Plot #:", anchor="center")
plotEnry = ttk.Entry(content)
recordButton = ttk.Button(content, text="Record ->", command=record)

#Labels in Live Frame
liveValueLabels = []

"""Tk Grid Calls"""
#Grid calls from frames
content.grid(column=0, row=0, sticky=(N, S, E, W))
liveFrame.grid(column=0, row=3, sticky=(N, S, E, W), pady=5)
gridKeyFrame.grid(column=1, row=3, sticky=(N, S, E, W), pady=5)
historyFrame.grid(column=2, row=2,rowspan=2, sticky=(N, S, E, W), pady=5)

#Grid calls from widgets in content
plotLbl.grid(column=0, row=0, sticky=(N, W), padx=5)
plotEnry.grid(column=0, row=1, sticky=(N, E, W), padx=5)
recordButton.grid(column=1, row=0)

#Window resizing stuff
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
content.columnconfigure(0, weight=3)
content.columnconfigure(1, weight=3)
content.columnconfigure(2, weight=3)
content.columnconfigure(3, weight=1)
content.columnconfigure(4, weight=1)
content.rowconfigure(1, weight=1)

liveFrame.columnconfigure(0, weight=1)
liveFrame.columnconfigure(1, weight=1)
for l in range(11):
    liveFrame.rowconfigure(l, weight=1)


historyFrame.columnconfigure(0, weight=1)
historyFrame.rowconfigure(0, weight=1)



update()
root.mainloop()
RUNNING = False
