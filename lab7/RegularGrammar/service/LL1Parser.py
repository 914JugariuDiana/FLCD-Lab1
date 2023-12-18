import copy

from tabulate import tabulate


class LL1Parser:
    def __init__(self, grammar, scanner):
        self.grammar = grammar
        self.scanner = scanner
        self.first = {}
        self.follow = {}
        for terminal in self.grammar.sigma:
            self.first[terminal] = terminal
        for non_terminal in self.grammar.N:
            self.follow[non_terminal] = []

        self.table = {}
        for terminal in self.grammar.sigma:
            self.table[terminal] = []
        for non_terminal in self.grammar.N:
            self.table[non_terminal] = []

        self.sequenceAccepted = False
        self.ds = ""
        self.dsError = ""

    def computeFirst(self):
        for key in self.grammar.productions.keys():
            if key not in self.first.keys():
                self.first[key] = []
            for elem in self.grammar.productions[key]:
                if elem[0] in self.grammar.sigma or elem[0] == "epsilon":
                    self.first[key].append(elem[0])
                    self.first[key] = list(set(self.first[key]))

        grammar = self.grammar
        while True:
            currentFirst = copy.deepcopy(self.first)
            for key in self.grammar.productions.keys():
                for elem in grammar.productions[key]:
                    if elem[0] in self.grammar.N and "epsilon" in self.first[elem[0]]:
                        for char in elem:
                            if 'epsilon' in self.first[char]:
                                self.first[key] = list(set(self.first[key] + self.first[char]))
                            else:
                                if char in self.grammar.N and len(self.first[char]) != 0:
                                    self.first[key] = list(set(self.first[key] + self.first[char]))
                                    if "epsilon" in self.first[key]:
                                        self.first[key].remove("epsilon")
                                    break
                                elif char in self.grammar.sigma:
                                    self.first[key] = list(set(list(self.first[char]) + self.first[key]))
                                    break
                    elif elem[0] in self.grammar.N:  # and len(self.first[elem[0]]) != 0:
                        self.first[key] = list(set(self.first[key] + self.first[elem[0]]))
                        if "epsilon" in self.first[key]:
                            self.first[key].remove("epsilon")
                        # break

            if self.compareDictionaries(currentFirst, self.first):
                break

    def compute_follow(self):
        self.follow[self.grammar.startSymbol].append("epsilon")

        while True:
            previousFollow = copy.deepcopy(self.follow)
            for nonterminal in self.grammar.N:
                for key in self.grammar.productions.keys():
                    for result in self.grammar.productions[key]:
                        if nonterminal in result:
                            for i in range(len(result)):
                                firstForNextSymbol = []

                                if result[i] == nonterminal:
                                    if len(result) > i + 1:
                                        firstForNextSymbol = copy.deepcopy(self.first[result[i + 1]])
                                        if isinstance(firstForNextSymbol, str):
                                            firstForNextSymbol = [firstForNextSymbol]
                                        for value in firstForNextSymbol:
                                            if value not in self.follow[nonterminal]:
                                                self.follow[nonterminal].append(value)
                                    else:
                                        for value in previousFollow[key]:
                                            if value not in self.follow[nonterminal]:
                                                self.follow[nonterminal].append(value)

                                    if "epsilon" in firstForNextSymbol:
                                        firstForNextSymbol.remove("epsilon")
                                        for value in previousFollow[key]:
                                            if value not in self.follow[nonterminal]:
                                                self.follow[nonterminal].append(value)
                                        for value in firstForNextSymbol:
                                            if value not in self.follow[nonterminal]:
                                                self.follow[nonterminal].append(value)

            if self.compareDictionaries(previousFollow, self.follow):
                break

    def parsing_table(self):
        self.computeFirst()
        self.compute_follow()
        for i in self.grammar.sigma:
            self.table[i] = [[i, "POP", 0]]

        index = 0
        for element in self.first.keys():
            if element in self.grammar.N:
                production = self.grammar.productions[element]
                for prod in production:
                    if "epsilon" in prod:
                        index += 1

                        for elem_follow in self.follow[element]:
                            self.table[element].append(
                                [elem_follow, 'epsilon', index])
                    else:
                        index += 1
                        char = prod[0]
                        if char in self.grammar.sigma:
                            self.table[element].append(
                                [char, prod, index])
                        else:
                            for elem in self.first[char]:
                                self.table[element].append(
                                    [elem, production[0], index])

        errors = []
        for key in self.table.keys():
            for elem in self.table[key]:
                for element in self.table[key]:
                    if elem[0] == element[0] and elem[1] != element[1]:
                        errors.append([key, elem[0], [elem[1], element[1]]])

        if len(errors) != 0:
            return errors

    def parseSequence(self, sequence):
        self.parsing_table()

        inputStack = []
        for elem in sequence.split(' '):
            inputStack.append(elem)

        workingStack = []
        resultStack = ""

        workingStack.append(self.grammar.startSymbol)

        self.searchSequence(inputStack, workingStack, resultStack)

        if not self.sequenceAccepted:
            self.printToFile("ps.txt", self.dsError)

    def checkSequence(self, filename):
        file = open(filename)
        sequence = file.read()

        self.parseSequence(sequence)

    def searchSequence(self, inputStack, workingStack, resultStack):
        if self.sequenceAccepted:
            return

        self.ds += "(" + ' '.join(str(elem) for elem in inputStack)
        self.ds += ', ' + ''.join(str(workingStack)) + ', ' + resultStack + ') -> '
        dsCopy = copy.deepcopy(self.ds)

        terminals = []

        if ("epsilon" in inputStack and len(inputStack) == 1 or len(inputStack) == 0) and len(workingStack) == 0:
            self.ds += 'accepted'
            self.printToFile("ps.txt", self.ds)
            self.sequenceAccepted = True
            return self.ds

        for elem in self.table[workingStack[0]]:
            terminals.append(str(elem[0]))

        if inputStack[0] == workingStack[0] or (self.scanner.checkIdentifier(inputStack[0]) and workingStack[0] ==
                                                "id") or (
                self.scanner.checkConstant(inputStack[0]) and workingStack[0] == "constants"):
            inputStack.pop(0)
            workingStack.pop(0)

            if len(inputStack) == 0 and len(workingStack) != 0:
                inputStack.append("epsilon")

            self.searchSequence(copy.deepcopy(inputStack), copy.deepcopy(workingStack), copy.deepcopy(resultStack))
        elif inputStack[0] in terminals:
            for elem in self.table[workingStack[0]]:
                if inputStack[0] == elem[0] or (self.scanner.checkIdentifier(inputStack[0]) and elem[0] ==
                                                "id") or (
                        self.scanner.checkConstant(inputStack[0]) and elem[0] == "constants"):
                    if elem[1] == "epsilon":
                        workingStack.pop(0)
                        resultStack += str(elem[2])
                        self.searchSequence(copy.deepcopy(inputStack), copy.deepcopy(workingStack), copy.deepcopy(resultStack))
                        # self.ds = dsCopy
                    else:
                        workingStack.pop(0)
                        workingStack = elem[1] + workingStack
                        resultStack += str(elem[2])
                        self.searchSequence(copy.deepcopy(inputStack), copy.deepcopy(workingStack), copy.deepcopy(resultStack))
                        # self.ds = dsCopy copy.deepcopy(inputStack), copy.deepcopy(workingStack), copy.deepcopy(resultStack)
        else:
            self.dsError = copy.deepcopy(self.ds) + "not accepted"
            return

    def print_table(self):
        self.parsing_table()

        headers = list(self.grammar.sigma)

        data = {i: [' '] * len(headers) for i in self.table}

        for i in self.table:
            for j in self.grammar.sigma:
                if len(self.table[i]) != 0:
                    if isinstance(self.table[i][0], list):
                        for elem in self.table[i]:
                            if j == elem[0]:
                                data[i][headers.index(j)] = ', '.join((''.join(elem[1]), str(elem[2])))
                else:
                    if j == self.table[i][0]:
                        data[i][headers.index(j)] = ', '.join((self.table[i][1], str(self.table[i][2])))

        transposed_data = {**{'Keys': list(data.keys())},
                           **{k: [data[i][headers.index(k)] for i in data] for k in headers}}

        print(transposed_data)

        print(tabulate(transposed_data, headers='keys', tablefmt='grid'))

    def print_first(self):
        for key in self.first.keys():
            print(key, self.first[key])

    def print_follow(self):
        for key in self.follow.keys():
            print(key, self.follow[key])

    def compareDictionaries(self, dict1, dict2):
        if not sorted(dict1.keys()) == sorted(dict2.keys()):
            return False

        for key in dict1.keys():
            if not sorted(dict1[key]) == sorted(dict2[key]):
                return False

        return True

    def printToFile(self, filename, content):
        file = open(filename, 'w')

        file.write(content)
