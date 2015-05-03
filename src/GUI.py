#!/usr/bin/python3
# -*- coding: utf-8 -*-
from tkinter import *
from tkinter import ttk

CONST_SIMULATION_MODE = True

class UI():

    def __init__(self, spudScale, inputTitle, orderedNames):
        root = Tk()
        root.title("Spud Scale")
        root.mainloop()
