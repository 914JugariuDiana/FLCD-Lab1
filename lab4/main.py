from FiniteAutomata import FiniteAutomata
from ui import UI

if __name__ == '__main__':

    filename = "constantFA.in"

    fa = FiniteAutomata(filename)
    ui = UI(fa)
    ui.start()