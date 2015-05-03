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
