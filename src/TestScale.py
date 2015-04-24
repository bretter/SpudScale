#!/usr/bin/python3

import threading
import time
import random


class Scale(threading.Thread):

    def __init__(self, comPort, container, index) :
        threading.Thread.__init__(self, daemon=True)
        self._stop = threading.Event()
        self.container = container
        self.index = index

    def run(self) :
        while not self.stopped() :
            time.sleep(random.random())
            name = chr(ord('A') + self.index)
            value = random.uniform(0, 50.0)
            self.container[self.index] = (name, value)
            print("NAME: " + name + "        VALUE: " + str(value))


# is a stop function necessary if thread runs as daemon?
# maybe necessary to close the serial port?
    def stop(self) :
        self._stop.set()

    def stopped(self) :
        return self._stop.isSet()

def main() :
    import time
    container = [0]*10
    index = 1
    scale = Scale('COM15', container, index)
    print("starting")
    scale.start()
    time.sleep(10)
    print("stopping")
    scale.stop()
    time.sleep(10)

if __name__ == '__main__':
    main()
