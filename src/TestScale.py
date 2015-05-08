#!/usr/bin/python3

import threading
import time


class Scale(threading.Thread):

    def __init__(self, comPort, container, index):
        threading.Thread.__init__(self, daemon=True)
        self.comPort = comPort
        self._stop = threading.Event()
        self.container = container
        self.index = index
        self.cycle = 0

    def run(self):
        ID = chr(ord('A') + self.index)
        while not self.stopped():
            time.sleep(.5)
            value = ID + str(self.cycle)
            self.container[ID] = value
            self.cycle += 1

# is a stop function necessary if thread runs as daemon?
# maybe necessary to close the serial port?
    def stop(self):
        self._stop.set()

    def stopped(self):
        return self._stop.isSet()
