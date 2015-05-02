#!/usr/bin/python3
# -*- coding: utf-8 -*-
import csv

class FileManager():

    def __init__(self, fileName):
        self.fileName = fileName

    def readHistory(self):
        history = []
        with open(self.fileName, newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                history.append(row)
        return history

    def record(self, readout):
        with open(self.fileName, 'a', newline='') as csvfile:
            writer = csv.writer(csvfile, 'excel')
            writer.writerow(readout)


def main():
    from ConfigReader import configReader
    #read config file
    usrconfig = configReader()

    #to initiaize values
    fileManager = FileManager('testOutput.py')
    fileManager.fileName = usrconfig['History']
    #fileManager.scaleNames = usrconfig['Scales']

    #to create and save a readout
    readout = ['plotName', '12', '51', '45', '84', '32', '54', '65', '12', '45', '98']
    fileManager.record(readout)

    fileManager.readHistory()



if __name__ == '__main__':
    main()
