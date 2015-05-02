#!/usr/bin/python3

import threading
import serial

class Scale(threading.Thread):

    def __init__(self, comPort, container) :
        threading.Thread.__init__(self, daemon=True)
        self._stop = threading.Event()
        self.container = container
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
                ID = line[0]
                sign = line[6]
                if (sign == '-') :
                    value = '0.00'
                else :
                    value = line[8:13].replace(' ','')
                #unit = line[15:17]
                #sp = "        "
                #print("ID: " + ID + sp + "SIGN: " + sign + sp + "UNIT: " + unit + sp + "VALUE: " + value)
                self.container[ID] = value
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
    container = {}
    scale = Scale('COM15', container)
    print("starting")
    scale.start()
    time.sleep(10)
    print("stopping")
    scale.stop()
    time.sleep(10)

if __name__ == '__main__':
    main()
