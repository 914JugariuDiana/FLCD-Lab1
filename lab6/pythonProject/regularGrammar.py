from operator import indexOf

class RegularGrammar:
    def __init__(self, filename):
        self.N = []
        self.sigma = []
        self.productions = {}
        self.startSymbol = ''
        self.getGrammarFromFile(filename)

    def getGrammarFromFile(self, filename):
        file = open(filename, "r")
        lines = file.readlines()

        for line in lines:
            elements = []
            line = line.replace("\n", '')
            position = indexOf(line, "=")
            elements.append(line[:position])
            elements.append(line[position + 1:])

            if elements[0] == 'N':
                self.N = elements[1].split(" ")
            elif elements[0] == 'sigma':
                self.sigma = elements[1].split(" ")
            elif elements[0] == 'P':
                elements[1].replace(" ", "")
                prod = elements[1].split("|")
                if prod[0] in self.productions.keys():
                    self.productions[prod[0]].append(prod[1])
                else:
                    self.productions[prod[0]] = [prod[1]]
            elif elements[0] == 'S':
                self.startSymbol = elements[1]

        file.close()

        if not self.isCFG():
            print("This is not a CFG")
            return

    def getAllNonterminals(self):
        stringBuilder = "N = {"

        for state in self.N:
            stringBuilder += state
            stringBuilder += ', '

        stringBuilder = stringBuilder[0:-2] + "}"

        return stringBuilder

    def getAllTerminals(self):
        stringBuilder = "Σ = {"

        for elem in self.sigma:
            stringBuilder += elem
            stringBuilder += ', '

        stringBuilder = stringBuilder[0:-2] + "}"

        return stringBuilder

    def getAllProductions(self):
        stringBuilder = ""

        for key in self.productions.keys():
            stringBuilder = stringBuilder + key + ' -> '
            if type(self.productions[key]) == list:
                for elem in self.productions[key]:
                    stringBuilder = stringBuilder + elem + "|"
            stringBuilder = stringBuilder[:-1]
            stringBuilder += '\n'

        return stringBuilder

    def getStartSymbol(self):
        return "S = " + self.startSymbol

    def isCFG(self):
        list = []
        for key in self.productions.keys():
            for terminal in self.productions[key]:
                if terminal in list and key in self.N:
                    print(terminal, " ", key)
                    list.append(terminal)
                    return False


        return True

