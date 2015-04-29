#!/usr/bin/python3
# -*- coding: utf-8 -*-
from tkinter import *
from SSFileManager import *
import threading

IsRunning = True
CONST_UPDATETIME = 1.0
CONST_SIMULATION_MODE = True





"""run our update code in a different thread while root.mainloop runs?"""
def update():
    if IsRunning:
        threading.Timer(CONST_UPDATETIME, update).start()
        if CONST_SIMULATION_MODE:
            pass
            #Data.SimUpdate()
        else:
            pass
            #Data.Update()

def main():
    #initialize objects
    root=Tk()
    fileManager = FileManager()

    update() #Start our thread
    root.mainloop() #This runs untill you close the window

    IsRunning = False #Stop our thread


if __name__ == "__main__":
    main()
