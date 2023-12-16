from LL1Parser import LL1Parser


class UI:
    def __init__(self, regularGrammar):
        self.rg = regularGrammar
        self.options = {1: "getAllNonterminals", 2: "getAllTerminals", 3: "getAllProductions",
                        4: "getStartSymbol"}

    def getMenu(self):
        string = ""
        string += "Options:\n"
        string += "1 -> print all nonterminals\n"
        string += "2 -> print the terminals\n"
        string += "3 -> print all productions\n"
        string += "4 -> print the start symbol\n"
        string += "5 -> first and follow\n"
        string += "6 -> parsing table\n"
        string += "7 -> check sequence\n"
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
                print("Try an option")
                continue

            if option == 5:
                self.parser = LL1Parser(self.rg)
                print('FIRST')
                self.parser.computeFirst()
                self.parser.print_first()
                print('\nFOLLOW')
                self.parser.compute_follow()
                self.parser.print_follow()
            elif option == 6:
                self.parser = LL1Parser(self.rg)
                res = self.parser.parsing_table()
                if res is not None:
                    print("conflicts: ", res)
                else:
                    # print(self.parser.table)
                    self.parser.print_table()
            elif option == 7:
                print("Sequence to be checked: ")
                sequence = input()
                self.parser = LL1Parser(self.rg)
                self.parser.parseSequence(sequence)
                print(self.parser.ds)

            elif option in self.options.keys():
                func_name = self.options[option]
                func = getattr(self.rg, func_name)
                print(func())
            elif option == 0:
                return
            else:
                print("No such option! Try again")


# defined integer func name ( integer IDENTIFIER ) { char IDENTIFIER ; }