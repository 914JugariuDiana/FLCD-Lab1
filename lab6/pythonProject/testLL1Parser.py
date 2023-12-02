import unittest

from LL1Parser import LL1Parser
from regularGrammar import RegularGrammar


class test_LL1Parser(unittest.TestCase):
    def setUp(self):
        filename = "g1.txt"
        grammar = RegularGrammar(filename)
        self.parser = LL1Parser(grammar)

    def testFirst(self):
        self.parser.computeFirst()
        for key in self.parser.first.keys():
            print(key, " ", self.parser.first[key])

        self.assertTrue('(' in self.parser.first['S'])
        self.assertTrue('a' in self.parser.first['S'])
        self.assertTrue("epsilon" in self.parser.first['A'])
        self.assertTrue('a' in self.parser.first['D'])
