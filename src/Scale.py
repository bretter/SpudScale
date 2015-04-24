#!/usr/bin/python3

import threading
import serial

class Scale(threading.Thread):

    def __init__(self, comPort, container, index) :
        threading.Thread.__init__(self, daemon=True)
        self._stop = threading.Event()
        self.container = container
        self.index = index
        self.port = comPort
        self.ser = serial.Serial(
            port=comPort,\
            baudrate=9600,\
            parity=serial.PARITY_NONE,\
            stopbits=serial.STOPBITS_ONE,\
            bytesize=serial.EIGHTBITS,\
            timeout=None)

    def run(self) :
        # length of scale output (used to ensure only complete messages are processed)
        msgLength = 21
        while True :
            rawLine = self.ser.readline()
            if (len(rawLine) == msgLength) :
                line = rawLine.decode('ascii')
                print(line)
                name = line[0]
                sign = line[6]
                value = float(line[9:13])
                unit = line[15:17]
                if (sign == '-') :
                    value = 0
                sp = "        "
                print("NAME: " + name + sp + "SIGN: " + sign + sp + "UNIT: " + unit + sp + "VALUE: " + str(value))
                self.container[self.index] = (name, value)
            if self.stopped() :
                self.ser.close()
                break

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
