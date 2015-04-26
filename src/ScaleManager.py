#!/usr/bin/python3

import TestScale
import time

class ScaleManager() :

    def __init__(self, scaleNames, comPorts) :
        scaleSet = set()
        self.scaleNames = scaleNames
        self.threadContainer = dict.fromkeys(self.scaleNames.keys())
        self.nameValuePairs = dict.fromkeys(self.scaleNames.values())
        ## This index will not be needed when the TestScale is pulled out.
        i = 0
        for port in comPorts :
            scaleSet.add(TestScale.Scale(port, self.threadContainer, i))
            i += 1
        for scale in scaleSet :
            scale.start()

    def getValues(self) :
        for ID, name in self.scaleNames.items() :
            self.nameValuePairs[name] = self.threadContainer[ID]
        return self.nameValuePairs

def main() :
    scaleNames = {'A' : 'A1',\
                              'B' : 'A2',\
                              'C' : 'A3',\
                              'D' : 'A4',\
                              'E' : 'B',\
                              'F' : 'C',\
                              'G' : 'Green',\
                              'H' : 'GC',\
                              'I' : 'Mis',\
                              'J' : 'Rots'}
    comPorts = {'COM0',\
                          'COM1',\
                          'COM2',\
                          'COM3',\
                          'COM4',\
                          'COM5',\
                          'COM6',\
                          'COM7',\
                          'COM8',\
                          'COM9'}
    scaleManager = ScaleManager(scaleNames, comPorts)
    while True :
        print(scaleManager.getValues())
        time.sleep(1)

if __name__ == '__main__':
    main()
