#!/usr/bin/python3

import Scale

class ScaleManager() :

    def __init__(self, scaleNames, comPorts) :
        scaleSet = set()
        self.scaleNames = scaleNames
        self.threadContainer = dict.fromkeys(self.scaleNames.keys())
        self.nameValuePairs = dict.fromkeys(self.scaleNames.values())
        ## This index will not be needed when the TestScale is pulled out.
        for port in comPorts :
            scaleSet.add(Scale.Scale(port, self.threadContainer))
        for scale in scaleSet :
            scale.start()

    def getValues(self) :
        for ID, name in self.scaleNames.items() :
            self.nameValuePairs[name] = self.threadContainer[ID]
        return self.nameValuePairs
