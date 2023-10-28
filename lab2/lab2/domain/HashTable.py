class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(self.size)]
    
    def hashFunction(self, key):
        res = 0

        for char in str(key):
            res += ord(char)

        return res % self.size

    def add(self, key):
        if self.contains(key):
            return self.getPos(key)

        self.table[self.hashFunction(key)].append(key)

        return self.getPos(key)

    def contains(self, key):
        return key in self.table[self.hashFunction(key)]
        
    def getPos(self, key):
        if self.contains(key) == False:
            return -1, -1

        index = self.hashFunction(key)
        listIndex = 0
        for value in self.table[index]:
            if value == key:
                break 
            else:
                listIndex += 1

        return index, listIndex

    def remove(self, key):
        self.table[self.hashFunction(key)].remove(key)

    def __str__(self):
        result = ""
        for i in range(self.size):
            result += '(' + str(i) + ", " + str(self.table[i]) + '\n'

        return result

