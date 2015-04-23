#!/usr/bin/python3

import serial
#import io

class Scale:

    def __init__(self, comPort, container, index) :
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
        self.readLoop()


    def readLoop(self) :
        # length of scale output (used to ensure only complete messages are processed)
        msgLength = 21
        while True :
            rawLine = self.ser.readline()
            while len(rawInput) = msgLength :
                line = rawLine.decode('ascii')
                print(rawInput)
                print(len(rawInput))
                name = rawInput[0]
                sign = rawInput[6]
                value = float(rawInput[9:13])
                unit = rawInput[15:17]
                if (sign == '-') :
                    value = 0
                sp = "        "
                print("NAME: " + name + sp + "SIGN: " + sign + sp + "UNIT: " + unit + sp + "VALUE: " + value)
                self.container[self.index] = (name, value)


def main() :
    container = [0]*10
    index = 1
    Scale('COM15', container, index)

if __name__ == '__main__':
    main()
