import re

from domain.FiniteAutomata import FiniteAutomata
from domain.PIF import PIF
from domain.SymbolTable import SymbolTable


class Scanner:
    def __init__(self):
        self.faIdentifier = FiniteAutomata("identifierFA.in")
        self.faIntegerConstant = FiniteAutomata("constantFA.in")
        self.pif = PIF()
        self.st = SymbolTable(50)
        self.separators = ['(', ')', ' ', '\n', '[', ']', ';', ',', '{', '}']
        self.operators = ["+", "++", "-", "--", "*", "/", "!=", "=", "==", "<", "<=", ">", ">=", "^"]
        self.reservedWords = ["defined", "func", "array", "char", "const", "for", "if", "else", "integer", "boolean",
                              "return", "while", "READ", "WRITE", "PRINT", "mod", "and", "or", "length"]
        self.errors = ""

    def scan(self, filename):
        file = open(filename, 'r')
        token = ""
        lines = file.readlines()
        for line in lines:
            newLine = line.replace('\n', '')
            for character in newLine:
                if character in self.separators:
                    self.classifyToken(token, lines.index(line))
                    token = ""
                    self.classifyToken(character, lines.index(line))
                else:
                    token += character

        self.writeToFile(self.pif.__str__(), "pif.out")
        self.writeToFile(self.st.__str__(), "st.out")
        if self.errors == "":
            return "lexically correct"

        return self.errors

    def classifyToken(self, token, pos):
        if token == '' or token == ' ':
            return
        if token in self.reservedWords or token in self.operators or token in self.separators:
            self.pif.add(token, 0)
        elif self.checkConstant(token) or self.checkIdentifier(token):
            pos = self.st.add(token)

            if self.checkConstant(token):
                self.pif.add("const", pos)
            else:
                self.pif.add("id", pos)
        else:
            self.errors += "Lexical error: line " + str(pos + 1) + " -> " + str(token) + "\n"

    def checkConstant(self, token):
        if self.faIntegerConstant.checkSequence(token):
            return True

        constant_pattern = r'^(0|[+-]?[1-9][0-9]*)$|^\'.\'$|^\".*\"$'
        return (re.match(constant_pattern, token)) is not None

    # def checkIdentifier(self, token):
    #     return re.match(r'^[a-z]([a-zA-Z]|[0-9])*$', token) is not None

    def checkIdentifier(self, token):
        return self.faIdentifier.checkSequence(token)

    def writeToFile(self, content, filename):
        file = open(filename, "w")
        file.write(content)
        file.close()
