import unittest

from lab2.service.Scanner import Scanner


class test_Scanner(unittest.TestCase):
    def setUp(self):
        self.scanner = Scanner()

    def testCheckConstant_numbers_true(self):
        self.assertTrue(self.scanner.checkConstant("+152"))
        self.assertTrue(self.scanner.checkConstant("-12"))
        self.assertTrue(self.scanner.checkConstant("1"))

    def testCheckConstant_Strings_true(self):
        self.assertTrue(self.scanner.checkConstant("\'a\'"))
        self.assertTrue(self.scanner.checkConstant("\"abc\""))
        self.assertTrue(self.scanner.checkConstant("\"--775#$%^&kAndeAdsA\""))

    def testCheckConstant_wrongNumbers_false(self):
        self.assertFalse(self.scanner.checkConstant("012"))

    def testCheckIdentifier_identifiersName_true(self):
        self.assertTrue(self.scanner.checkIdentifier("a1"))
        self.assertTrue(self.scanner.checkIdentifier("number"))
        self.assertTrue(self.scanner.checkIdentifier("carNumber"))

    def testCheckIdentifier_wrongIdentifier_false(self):
        self.assertFalse(self.scanner.checkIdentifier("1ads"))
        self.assertFalse(self.scanner.checkIdentifier("1542"))
        self.assertFalse(self.scanner.checkIdentifier("uskjh$#"))
