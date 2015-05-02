#!/usr/bin/python3

from ScaleManager import ScaleManager
from FileManager import FileManager
#import GUI as UI
from ConfigReader import configReader

class SpudScale() :

    def __init__(self) :
        self.fileName = ''

        configInfo = configReader()
        comPorts = configInfo['ports']
        self.inputTitle = configInfo['input']
        self.orderedNames = configInfo['ordered']
        self.scaleAddressNames = configInfo['scales']

        self.numScales = len(comPorts)
        self.numInputs = len(self.inputTitle)
        self.numOutputs  = self.numInputs + self.numScales
        self.currentValues = [None]*self.numScales
        self.lastFiveRecorded = [[None]*(self.numOutputs)]*5

        #self.ui = UI(inputTitle, self.orderedNames)

        self.scaleManager = ScaleManager(self.scaleAddressNames, comPorts)

        self.fileManager = FileManager('testOutput.csv')
        self.fileManager.record(self.inputTitle + self.orderedNames)

    def record(self, userInput) :
        recordEntry = [userInput] + self.getCurrentValues()
        self.fileManager.record(recordEntry)
        self.updateLastFiveRecorded(recordEntry)

    def getCurrentValues(self) :
        newValues = self.scaleManager.getValues()
        for i in range(0, self.numScales) :
            name = self.orderedNames[i]
            self.currentValues[i] = newValues[name]
        return self.currentValues

    def getLastFiveRecorded(self) :
        return self.lastFiveRecorded

    def setFileName(self, newFileName) :
        self.fileName = newFileName

    def updateLastFiveRecorded(self, recordEntry) :
        i = len(self.lastFiveRecorded) - 1
        while i > 0 :
            self.lastFiveRecorded[i] = self.lastFiveRecorded[i - 1]
            i -= 1
        self.lastFiveRecorded[0] = recordEntry

def main() :
    import time
    spudScale = SpudScale()
    time.sleep(10)
    for i in range(0,100) :
        print(spudScale.getCurrentValues())
        spudScale.record('Line' + str(i))
        if (i%5 == 0) :
            print(spudScale.getLastFiveRecorded())
        time.sleep(.5)
    return 0

if __name__ == '__main__':
    main()

"""
getScaleNames()
getCurrentValues()
recordValues(plotNumber)
getLastFive()
Is there anything else it would need?
.setFileName(...)
"""
