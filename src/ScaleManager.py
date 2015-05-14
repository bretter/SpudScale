#!/usr/bin/python3
import Scale
import TestScale


class ScaleManager():
    """ScaleManager instantiates individual Scale objects and provides a
    thread-safe method of collecting data from them.

    Args:
        scaleNames: list of strings; unique names used to ID individual scales.
        comPorts: list of strings; names of the COM ports to read from.
        test: bool; set true if physical scales are unavailable/disconnected.
    """

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
        """Retrieves most recentl scale output and outputs as a dictionary.

        Returns:
            List of strings; most current reading from Scale objects."""
        for ID, name in self.scaleNames.items():
            self.nameValuePairs[name] = self.threadContainer[ID]
        return self.nameValuePairs
