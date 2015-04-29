#!/usr/bin/python3
# -*- coding: utf-8 -*-
import csv
import ConfigReader

class FileManager():

    def __init__(self):
        self.scaleNames = []
        self.historyFileName = 'NA'
        self.readHistory

    def readHistory(self):
        print("reading history")

    def record(self, readout):
        print("recording history")


def main():
    #read config file

    #to initiaize values
    fileManager = FileManager()
    fileManager.historyFileName = 'history.csv'
    fileManager.scaleNames = [ 'A1' , 'A2', 'A3', 'A4', 'B', 'C', 'Green', 'GC', 'Mis', 'Rots']

    #to create and save a readout
    readout = ['plotName', '12', '51', '45', '84', '32', '54', '65', '12', '45', '98']
    fileManager.record(readout)



if __name__ == '__main__':
    main()
