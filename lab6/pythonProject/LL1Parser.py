import copy


class LL1Parser:
    def __init__(self, grammar):
        self.grammar = grammar
        self.first = {}
        for terminal in self.grammar.sigma:
            self.first[terminal] = terminal

    def computeFirst(self):
        for key in self.grammar.productions.keys():
            if key not in self.first.keys():
                self.first[key] = []
            for elem in self.grammar.productions[key]:
                if elem in self.grammar.sigma or elem == "epsilon":
                    self.first[key].append(elem)
                elif elem[0] in self.grammar.sigma:
                    self.first[key].append(elem[0])

        grammar = self.grammar
        while True:
            # currentFirst = dict(self.first)
            currentFirst = copy.deepcopy(self.first)
            for key in self.grammar.productions.keys():
                for elem in grammar.productions[key]:
                    if elem[0] in self.grammar.N and len(self.first[elem[0]]) == 1 and "epsilon" in self.first[elem[0]]:
                        for char in elem:
                            if 'epsilon' in self.first[char] and len(self.first[char]) == 1:
                                continue
                            else:
                                if char in self.grammar.N and len(self.first[char]) != 0:
                                    self.first[key] = list(set(self.first[key] + self.first[char]))
                                    if "epsilon" in self.first[key]:
                                        self.first[key].remove("epsilon")
                                    break
                                elif char in self.grammar.sigma:
                                    self.first[key] += self.first[char]
                                    break
                    elif elem[0] in self.grammar.N and len(self.first[elem[0]]) != 0:
                        self.first[key] = list(set(self.first[key] + self.first[elem[0]]))
                        if "epsilon" in self.first[key]:
                            self.first[key].remove("epsilon")
                        break

            if currentFirst == self.first:
                break
