#!/usr/bin/python3
# -*- coding: utf-8 -*-
from tkinter import Tk, ttk, N, S, E, W, StringVar, Menu
from tkinter import font, filedialog, messagebox
from ConfigReader import configReader
import SpudScale
import threading

UPDATETIME = 100


class GUI():

    def __init__(self):
        # init Tk
        self.root = Tk()
        self.root.title("SpudScale")
        self.root.resizable(0, 0)
        self.root.option_add('*tearOff', False)
        content = ttk.Frame(self.root).grid(column=0, row=0, sticky=(N, S, E, W))

        # init config info
        configInfo = configReader()
        self.inputTitle = configInfo['input']
        self.orderedNames = configInfo['ordered']

        # init self variables
        self.spudScale = SpudScale.SpudScale()
        self.currentValues = [StringVar() for i in
                              range(len(self.orderedNames))]
        self.lastFiveValues = [[StringVar() for i in range(
                              len(self.orderedNames) + len(self.inputTitle))]
                              for j in range(5)]
        self.plotLabel = StringVar()

        self.fileName = StringVar()
        self.fileName.set(self.spudScale.fileName)

        # init font
        labelFont = font.Font(family='system', size=10, weight='bold')
        # init menubar
        menubar = Menu(self.root)
        self.root['menu'] = menubar
        menu_file = Menu(menubar)
        menubar.add_cascade(menu=menu_file, label='File')
        menu_file.add_command(label='New File', command=self.newFile)
        menu_file.add_command(label='Open File', command=self.openFile)
        menu_file.add_command(label='About', command=self.aboutDialog)

        # init lables
        # input Title Label
        ttk.Label(content, text=self.inputTitle, anchor="center", width=10,
                  font=labelFont).grid(column=0, row=0, sticky=(N, W))
        # current File Label
        ttk.Label(content, text='Current File: ', anchor="center", width=10,
                  font=labelFont).grid(column=3, row=0, columnspan=3,
                  sticky=(N, S, E, W))
        # File Label
        ttk.Label(content, textvariable=self.fileName, anchor="center",
                  width=10, relief='sunken').grid(column=2, row=1,
                  columnspan=6, sticky=(N, S, E, W))
        # plot Entry
        ttk.Entry(content, textvariable=self.plotLabel, width=12, takefocus=1)\
            .grid(column=0, row=1, sticky=(N, S, E, W))
        # record Button
        ttk.Button(content, text="Record", command=self.record)\
            .grid(column=1, row=1, sticky=(N, S, E, W))
        # last 5 Plots Label
        ttk.Label(content, text='Last 5 Plots', anchor='center',
                  font=labelFont).grid(column=3, row=2, columnspan=3,
                  sticky=(N, S, E, W))
        # live Values Label
        ttk.Label(content, text='Live Values', anchor='center',
                  font=labelFont).grid(column=0, row=3, sticky=(N, S, E, W))
        # second Title Label
        ttk.Label(content, text=self.inputTitle, anchor="center")\
            .grid(column=1, row=3)

        for i in range(len(self.orderedNames)):
            # live value labels
            scaleValue = self.currentValues[i]
            ttk.Label(content, textvariable=scaleValue,
                      anchor="center", background='white', relief='sunken',
                      width=12).grid(column=0, row=(i + 4))
            # ordered names' labels
            fieldName = self.orderedNames[i]
            ttk.Label(content, text=fieldName, anchor="center", relief='ridge',
                      width=12).grid(column=1, row=(i + 4))

        # history value labels
        for c in range(5):
            for i in range(len(self.orderedNames) + len(self.inputTitle)):
                ttk.Label(content, textvariable=self.lastFiveValues[c][i],
                          anchor="center", relief='ridge', width=12,
                          background='white').grid(column=(c + 2), row=(i + 3))

        # focus on plot entry (not working?)
        # bind enter to record button
        self.root.bind('<Return>', self.enterPressed)


        # begin Tk's mainloop
        self.update()
        self.root.mainloop()

    def enterPressed(self, event):
        self.record()

    def newFile(self):
        fileName = filedialog.asksaveasfilename(
            filetypes=(("Comma Seperated Value", "*.csv"),
                               ("Text", "*.txt"), ("All files", "*.*")))
        if fileName:
            self.spudScale.setFileName(fileName)
            self.fileName.set(self.spudScale.fileName)

    def openFile(self):
        fileName = filedialog.askopenfilename(
                  filetypes=(("Comma Seperated Value", "*.csv"),
                                     ("Text", "*.txt"), ("All files", "*.*")))
        if fileName:
            self.spudScale.setFileName(fileName)
            self.fileName.set(self.spudScale.fileName)

    def updateLastFive(self):
        lastFive = self.spudScale.getLastFiveRecorded()
        for c in range(5):
            for r in range(len(self.orderedNames) + len(self.inputTitle)):
                self.lastFiveValues[c][r].set(lastFive[c][r])

    def record(self):
        self.spudScale.record(self.plotLabel.get())
        self.updateLastFive()
        self.plotLabel.set('')

    def update(self):
        newCurrentValues = self.spudScale.getCurrentValues()
        for i in range(len(newCurrentValues)):
            value = newCurrentValues[i]
            self.currentValues[i].set(value)

        self.root.after(UPDATETIME, self.update)

    def aboutDialog(self):
        messagebox.showinfo(
            'About SpudScale',
            'SpudScale was developed for University of Florida\'s '
            'department of Horticultural Sciences.\n'
            '\n'
            'Developed and maintained by:\n'
            '\n'
            'Brett Nelson\n'
            'Brett@BrettNelson.org\n'
            '\n'
            'Rocco Febbo\n'
            'febbo87@gmail.com\n'
            '\n'
            'For source code and licensing information see:\n'
            'www.github.com\\bretter\\SpudScale')
        return


def main():
    GUI()

if __name__ == '__main__':
    main()
