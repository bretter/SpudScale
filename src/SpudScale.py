#!/usr/bin/python3
from ScaleManager import ScaleManager
from ConfigReader import configReader
import FileManager


class SpudScale():
    """The SpudScale class acts as a 'main' class for the code back-end.

    SpudScale instantiates all the major components of system.
    It also manages communication between the disparate classes.
    """

    def __init__(self):
        self.fileName = ''

        configInfo = configReader()
        comPorts = configInfo['ports']
        addNames = configInfo['scales']
        if 'test-mode' in configInfo:
            testMode = configInfo['test-mode']
        else:
            testMode = False
        self.inputTitle = configInfo['input']
        self.orderedNames = configInfo['ordered']

        self.numScales = len(comPorts)
        self.numInputs = len(self.inputTitle)
        self.numOutputs = self.numInputs + self.numScales
        self.currentValues = ['']*self.numScales
        self.lastFiveRecorded = [['']*(self.numOutputs)]*5

        self.scaleManager = ScaleManager(addNames, comPorts, testMode)

        self.fileName = 'testOutput.csv'
        self.newFile = True

    def record(self, userInput):
        """Collects and formats user input and data for writing to a file.

        Args:
            uerInput: User inputted value to be recorded with data.

        Returns:
            None
        """
        if self.newFile:
            recordEntry = self.inputTitle + self.orderedNames
            FileManager.writeData(self.fileName, recordEntry)
            self.newFile = False
        recordEntry = [userInput] + self.getCurrentValues()
        FileManager.writeData(self.fileName, recordEntry)
        self.updateLastFiveRecorded(recordEntry)

    def getCurrentValues(self):
        """Gets recent scale values and orders them based on config file.

        Returns:
            List of strings; values sorted for use by GUI."""
        newValues = self.scaleManager.getValues()
        for i in range(0, self.numScales):
            name = self.orderedNames[i]
            self.currentValues[i] = newValues[name]
        return self.currentValues

    def getLastFiveRecorded(self):
        """Returns the five most recent output entries.

        Retures:
            List of lists of strings; recently recorded values.
        """
        return self.lastFiveRecorded

    def getOrderedNames(self):
        """Getter function for ordered names as defined in the config file.

        Returns:
            List of strings; scale names."""
        return self.orderedNames

    def setFileName(self, newFileName):
        """Sets the name of the output file.

        Args:
            newFileName: string containing new file name.

        Returns:
            None
        """
        self.fileName = newFileName
        self.newFile = True

    def updateLastFiveRecorded(self, recordEntry):
        """Updates the list of recently recorded values.

        Args:
            recordEntry: list of strings."""
        i = len(self.lastFiveRecorded) - 1
        while i > 0:
            self.lastFiveRecorded[i] = self.lastFiveRecorded[i - 1]
            i -= 1
        self.lastFiveRecorded[0] = recordEntry
