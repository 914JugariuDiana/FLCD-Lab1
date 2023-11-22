from regularGrammar import RegularGrammar
from ui import UI

if __name__ == '__main__':

    # filename = "g1.txt"
    filename = "g2-DJ.txt"

    rg = RegularGrammar(filename)
    ui = UI(rg)
    ui.start()