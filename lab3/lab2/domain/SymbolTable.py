from lab2.domain.HashTable import HashTable


class SymbolTable:
    def __init__(self, size):
        self.symbolTable = HashTable(size)

    def add(self, key):
        return self.symbolTable.add(key);

    def contains(self, key):
        return self.symbolTable.contains(key);

    def getPos(self, key):
        return self.symbolTable.getPos(key);

    def remove(self, key):
        return self.symbolTable.remove(key);

    def __str__(self):
        return self.symbolTable.__str__();
