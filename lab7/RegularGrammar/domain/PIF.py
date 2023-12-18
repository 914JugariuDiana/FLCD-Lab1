class PIF:
    def __init__(self):
        self.pif = []

    def add(self, token, position):
        self.pif.append([token, position])

    def __str__(self):
        result = ""
        for pair in self.pif:
            result += "( " + str(pair[0]) + ", " + str(pair[1]) + ")\n"

        return result
