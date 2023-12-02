class UI:
    def __init__(self, regularGrammar):
        self.rg = regularGrammar
        self.options = {1: "getAllNonterminals", 2: "getAllTerminals",  3: "getAllProductions",
                        4: "getStartSymbol"}

    def getMenu(self):
        string = ""
        string += "Options:\n"
        string += "1 -> print all nonterminals\n"
        string += "2 -> print the terminals\n"
        string += "3 -> print all productions\n"
        string += "4 -> print the start symbol\n"
        string += "0 -> exit"

        return string

    def start(self):
        if not self.rg.isCFG():
            print("This is not a CFG")
            return

        option = None

        while option != 0:
            print(self.getMenu())
            option = input()
            if option.isdigit():
                option = int(option)
            else:
                print("No such option! Try again")

            if option in self.options.keys():
                func_name = self.options[option]
                func = getattr(self.rg, func_name)
                print(func())
            elif option == 0:
                return
            else:
                print("No such option! Try again")