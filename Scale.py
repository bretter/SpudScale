import serial
import threading

class Scale:

    def __init__(self, comPort, test=False) :
        self.TEST = test
        self.port = comPort
        self.recentValues = [0] * 10
        self.stable = False
        self.identity = "unknown"
        if self.TEST :
            self.rand = __import__('random')
        else :
            self.serialPort = serial.Serial(comPort)
            getName(serialPort)
            self.readThread = threading.Thread(target=portReader, args=(serialPort))
            readThread.start()

    def query(self) :
        """
        Returns a tuple with the most recently read value and the stability status.
        """
        if not self.TEST :
            return (self.recentValues[0], self.stable)
        else:
            return (self.rand.uniform(0,75), self.rand.choice([True, False]))

    def update(self, newReading) :
        """
        Appends the most recently read value to the head of recentValues and trims the tail.
        Determines weather conditions for stability have been met.
        """

    def discoverName(self, serialPort) :
        """
        Parses the scale input for the identiy of the scale and assigns a name to identity.
        """

def main() :
    time = __import__('time')
    scale = Scale('comNone', True)
    while True :
        print(scale.query())
        time.sleep(3)

if __name__ == '__main__':
    main()
