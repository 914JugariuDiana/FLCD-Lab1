from operator import indexOf



class RegularGrammar:
    def __init__(self, filename):
        self.N = []
        self.sigma = []
        self.productions = {}
        self.startSymbol = ''
        self.numberedProduction = {}
        self.getGrammarFromFile(filename)
        self.first = {}
        for terminal in self.sigma:
            self.first[terminal] = terminal

    def getGrammarFromFile(self, filename):
        indice = 0
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
                indice += 1
                prod = elements[1].split("|")
                values = prod[1].split(' ')
                self.numberedProduction[tuple(values)] = indice
                if prod[0] in self.productions.keys():
                    self.productions[prod[0]].append(values)
                else:
                    self.productions[prod[0]] = [values]
            elif elements[0] == 'S':
                self.startSymbol = elements[1]

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
                    stringBuilder = stringBuilder + ' '.join(elem) + " |"
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
