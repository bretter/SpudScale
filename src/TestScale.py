#!/usr/bin/python3
import threading
import time


class Scale(threading.Thread):
    """This Scale is a debugging tool for use when real scales are unavailable.

    Each instance of Scale launches a thread which generates dummy output
    and saves that input to an entry in a dict.

    Args:
        comPort: string; name of a COM port.
        container: dict; shared memory for use by all Scale threads.
        index: string; used to identify the scale.
    """

    def __init__(self, comPort, container, index):
        threading.Thread.__init__(self, daemon=True)
        self.comPort = comPort
        self._stop = threading.Event()
        self.container = container
        self.index = index
        self.cycle = 0

    def run(self):
        """Dummy output data loop."""
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
