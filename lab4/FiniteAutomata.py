class FiniteAutomata:
    def __init__(self, filename):
        self.Q = []
        self.sigma = []
        self.transitions = []
        self.finalStates = []
        self.initialState = ''
        self.getFAFromFile(filename)

    def getFAFromFile(self, filename):
        file = open(filename, "r")
        lines = file.readlines()

        for line in lines:
            line = line.replace(" ", '')
            line = line.replace("\n", '')
            elements = line.split("=")

            if elements[0] == 'Q':
                self.Q = elements[1].split(",")
            elif elements[0] == 'sigma':
                self.sigma = elements[1].split(",")
            elif elements[0] == 'trans':
                self.transitions.append(elements[1].split(','))
            elif elements[0] == 'q0':
                self.initialState = elements[1]
            elif elements[0] == "F":
                self.finalStates = elements[1].split(',')

    def getAllStates(self):
        stringBuilder = "Q = {"

        for state in self.Q:
            stringBuilder += state
            stringBuilder += ', '

        stringBuilder = stringBuilder[0:-2] + "}"

        return stringBuilder

    def getAllAlphabet(self):
        stringBuilder = "Σ = {"

        for elem in self.sigma:
            stringBuilder += elem
            stringBuilder += ', '

        stringBuilder = stringBuilder[0:-2] + "}"

        return stringBuilder

    def getAllTransitions(self):
        stringBuilder = ""

        for transition in self.transitions:
            stringBuilder = stringBuilder + "δ(" + transition[0] + ', ' + transition[1] + ")=" + transition[2]
            stringBuilder += '\n'

        return stringBuilder

    def getInitialState(self):
        return "q0 = " + self.initialState

    def getFinalStates(self):
        stringBuilder = "F = {"

        for elem in self.finalStates:
            stringBuilder += elem
            stringBuilder += ', '

        stringBuilder = stringBuilder[0:-2] + "}"

        return stringBuilder

    def isDFA(self):
        list = []
        for transition in self.transitions:
            move = [transition[0], transition[1]]
            if move in list:
                return False

            list.append(move)

        return True

    def checkRec(self, sequence, currentPos, result):
        if len(sequence) == 0 and currentPos in self.finalStates:
            result.append(True)
        elif True in result or len(sequence) == 0:
            return
        else:
            for transition in self.transitions:
                if currentPos == transition[0] and transition[1] == sequence[0]:
                    self.checkRec(sequence[1:], transition[2], result)

        return False

    def checkSequence(self):
        print("Sequence to be checked: ")
        sequence = input()
        result = []
        self.checkRec(sequence, self.initialState, result)

        return True in result



