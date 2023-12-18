from service.LL1Parser import LL1Parser
from domain.regularGrammar import RegularGrammar
from service.Scanner import Scanner
from ui import UI

if __name__ == '__main__':

    filename = "g1.txt"
    seqFilename = "seq1.in"
    # filename = "g2-DJ.txt"
    # seqFilename = "seq2.in"

    scanner = Scanner()
    scanner.scan(seqFilename)
    rg = RegularGrammar(filename)
    parser = LL1Parser(rg, scanner)
    parser.checkSequence(seqFilename)
    # ui = UI(rg)
    # ui.start()