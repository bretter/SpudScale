#!/usr/bin/python3
# -*- coding: utf-8 -*-
import csv

def readData(fileName):
    history = []
    with open(fileName, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            history.append(row)
    return history

def writeData(fileName, readout):
    with open(fileName, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile, 'excel')
        writer.writerow(readout)
