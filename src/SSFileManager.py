#!/usr/bin/python3
# -*- coding: utf-8 -*-
import csv
from ConfigReader import *

class FileManager():

    def __init__(self):
        self.scaleNames = []
        self.historyFileName = 'NA'
        self.readHistory

    def readHistory(self):
        print("reading history")

    def record(self, readout):
        print("recording history")
        with open(self.historyFileName, 'a', newline='') as csvfile:
            writer = csv.writer(csvfile, 'excel')
            writer.writerow(readout)


def main():
    #read config file
    usrconfig = configReader()

    #to initiaize values
    fileManager = FileManager()
    fileManager.historyFileName = usrconfig['History']
    fileManager.scaleNames = usrconfig['Scales']

    #to create and save a readout
    readout = ['plotName', '12', '51', '45', '84', '32', '54', '65', '12', '45', '98']
    fileManager.record(readout)



if __name__ == '__main__':
    main()
