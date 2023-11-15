
class UI:
    def __init__(self, fa):
        self.fa = fa
        self.options = {1: "getAllStates", 2: "getAllAlphabet",  3: "getAllTransitions",
                        4: "getInitialState", 5: "getFinalStates", 6: "checkSequence"}

    def getMenu(self):
        string = ""
        string += "Options:\n"
        string += "1 -> print all states\n"
        string += "2 -> print the alphabet\n"
        string += "3 -> print all transitions\n"
        string += "4 -> print the initial state\n"
        string += "5 -> print final states\n"
        string += "6 -> check if sequence is accepted\n"
        string += "0 -> exit"

        return string

    def start(self):
        if not self.fa.isDFA():
            print("This is not a DFA")
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
                func = getattr(self.fa, func_name)
                print(func())
            elif option == 0:
                return
            else:
                print("No such option! Try again")