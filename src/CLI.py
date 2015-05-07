import SpudScale


class CLI():

    def __init__(self):
        self.spudScale = SpudScale.SpudScale()
        self.title = 'SpudScale' + ' '*49 + 'University of Florida'
        self.message = ''
        self.exit = False
        self.orderedNames = self.spudScale.getOrderedNames()

    def mainMenu(self):
        while not self.exit:
            choices = {'1', '2', '3', 'Q'}
            self.printMain()
            selection = input('Please make a selection: ')
            if selection in choices:
                if selection == '1':
                    self.recordMode()
                elif selection == 'Q':
                    self.exit = True
            else:
                self.message = 'Invalid Option'

    def recordMode(self):
        returnToMain = False
        while not returnToMain:
            self.printCompDisplay()
            self.blankLines(3)
            print('Enter: a plot number to record current values')
            print('       a blank line to refresh live values')
            print('       or Q to return to the main menu')
            userInput = input('Plot #: ')
            choices = {'', 'Q'}
            if userInput in choices:
                if userInput == 'Q':
                    returnToMain = True
            else:
                self.spudScale.record(userInput)

    def printCompDisplay(self):
        currentValues = self.spudScale.getCurrentValues()
        lastFiveRecorded = self.spudScale.getLastFiveRecorded()
        numCurrent = len(currentValues)
        numFive = len(lastFiveRecorded[0])
        numNames = len(self.orderedNames)
        print(self.title)
        print(' '+'_'*78)
        print(' |{0:^10s}|{1:^10s}|{2:^54s}|'.format(
            'Live', 'Scale', 'Recorded'))
        print(' |'+'-'*10+'+'+'-'*10+'+'+'-'*(10*5 + 4)+'|')
        rowVal = ['']*7
        for i in range(0, numFive):
            if (i < (numFive - numCurrent)):
                rowVal[0] = ''
            else:
                rowVal[0] = currentValues[(i - (numFive - numCurrent))]
            if (i < (numFive - numNames)):
                rowVal[1] = 'Plot#'
            else:
                rowVal[1] = self.orderedNames[(i - (numFive - numNames))]
            for j in range(0, len(lastFiveRecorded)):
                rowVal[(j + 2)] = lastFiveRecorded[j][i]
            print(' |{0:^10s}|{1:^10s}|{2:^10s}\
                |{3:^10s}|{4:^10s}|{5:^10s}|{6:^10s}|'.format(
                rowVal[0], rowVal[1], rowVal[2], rowVal[3],
                rowVal[4], rowVal[5], rowVal[6]))
        self.blankLines(3)

    def printCurrent(self):
        print('Current')

    def printMain(self):
        print(self.title)
        self.blankLines(3)
        print('        _________                .____________             .__')
        print('       /   _____/_____  __ __  __| _/   _____/ ____ _____  |  |   ____')
        print('       \\_____  \\\____ \\|  |  \\/ __ |\\_____  \\_/ ___\\\\__  \\ |  | _/ __ \\')
        print('       /        \\  |_> >  |  / /_/ |/        \\  \\___ / __ \\|  |_\\  ___/')
        print('      /_______  /   __/|____/\\____ /_______  /\\___  >____  /____/\\___  >')
        print('              \\/|__|              \\/       \\/     \\/     \\/          \\/ ')
        self.blankLines(7)
        print('Main Menu:')
        print('  (1) Record Mode')
        print('  (2) Set Output File --not yet implemented')
        print('  (Q) Exit')
        self.blankLines(2)
        print(self.message)

    def blankLines(self, lines):
        for line in range(0, lines):
            print('')


def main():
    cli = CLI()
    cli.mainMenu()

if __name__ == '__main__':
    main()
