import unittest

from lab2.domain.HashTable import HashTable


class test_HashTable(unittest.TestCase):
    def setUp(self):
        self.st = HashTable(5)
        self.st.add('dsf')
        self.st.add('dsffsad')
        self.st.add('dfs')
        self.st.add('fsd')
        self.st.add('dsfsdrklf')
        self.st.add('dsffkld')
        self.st.add('dsfklrr')

    def testContains_containedElement_true(self):
        self.assertTrue(self.st.contains("dsf"))

    def testContains_notPresentElement_false(self):
        self.assertFalse(self.st.contains("aa"))

    def testGetPosition_element_correctPosition(self):
        self.assertEquals(self.st.getPos("dsf"), (2, 0))

    def testRemove_presentElement_removed(self):
        self.st.remove("dfs")
        self.assertEquals(self.st.getPos("dfs"), (-1, -1))

    def tearDown(self):
        del self.st
