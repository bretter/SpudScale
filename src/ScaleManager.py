#!/usr/bin/python3

import Scale
import TestScale


class ScaleManager():

    def __init__(self, scaleNames, comPorts, test):
        scaleSet = set()
        self.scaleNames = scaleNames
        self.threadContainer = dict.fromkeys(self.scaleNames.keys())
        self.nameValuePairs = dict.fromkeys(self.scaleNames.values())
        if test:
            i = 0
            for port in comPorts:
                scaleSet.add(TestScale.Scale(port, self.threadContainer, i))
                i += 1
        else:
            for port in comPorts:
                scaleSet.add(Scale.Scale(port, self.threadContainer))
        for scale in scaleSet:
            scale.start()

    def getValues(self):
        for ID, name in self.scaleNames.items():
            self.nameValuePairs[name] = self.threadContainer[ID]
        return self.nameValuePairs
