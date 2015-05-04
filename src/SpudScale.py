#!/usr/bin/python3

from ScaleManager import ScaleManager
import FileManager
#import CLI as UI
from ConfigReader import configReader

class SpudScale() :

    def __init__(self) :
        self.fileName = ''

        configInfo = configReader()
        comPorts = configInfo['ports']
        addNames = configInfo['scales']
        self.inputTitle = configInfo['input']
        self.orderedNames = configInfo['ordered']

        self.numScales = len(comPorts)
        self.numInputs = len(self.inputTitle)
        self.numOutputs  = self.numInputs + self.numScales
        self.currentValues = ['']*self.numScales
        self.lastFiveRecorded = [['']*(self.numOutputs)]*5

        self.scaleManager = ScaleManager(addNames, comPorts)

        self.fileName = 'testOutput.csv'
        self.newFile = True

        #self.ui = UI.UI(self, self.inputTitle, self.orderedNames)


    def record(self, userInput) :
        if self.newFile :
            recordEntry = self.inputTitle + self.orderedNames
            FileManager.writeData(self.fileName, recordEntry)
            self.newFile = False
        recordEntry = [userInput] + self.getCurrentValues()
        FileManager.writeData(self.fileName, recordEntry)
        self.updateLastFiveRecorded(recordEntry)

    def getCurrentValues(self) :
        newValues = self.scaleManager.getValues()
        for i in range(0, self.numScales) :
            name = self.orderedNames[i]
            self.currentValues[i] = newValues[name]
        return self.currentValues

    def getLastFiveRecorded(self) :
        return self.lastFiveRecorded

    def getOrderedNames(self) :
        return self.orderedNames

    def setFileName(self, newFileName) :
        self.fileName = newFileName
        self.newFile = True

    def updateLastFiveRecorded(self, recordEntry) :
        i = len(self.lastFiveRecorded) - 1
        while i > 0 :
            self.lastFiveRecorded[i] = self.lastFiveRecorded[i - 1]
            i -= 1
        self.lastFiveRecorded[0] = recordEntry

def debug() :
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

def main() :
    import GUI as UI
    spudScale = SpudScale()


if __name__ == '__main__':
    #main()
    debug()
