import unittest

from smallibs.genlex.lexer import *

class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_should_have_an_int(self):
        stream = Stream("123 soleil")
        
        assert IntRecognizer()(stream) == 123
        
    def test_should_have_a_string(self):
        stream = Stream('"soleil" 123"')

        assert StringRecognizer()(stream) == "soleil"        

    def test_should_have_a_string_delim(self):
        stream = Stream("'soleil' 123'")

        assert StringDelimRecognizer()(stream) == "soleil"        
                
def suite():
   suite = unittest.TestSuite()
   suite.addTest(unittest.makeSuite(TestCase))
   return suite

if __name__ == '__main__':
    unittest.main()
