import unittest

from smallibs.genlex.matchers import *
from smallibs.genlex.stream import *
from smallibs.genlex.lexer import *

class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_should_have_an_int(self):
        stream = Stream("123 soleil")
        
        assert IntMatcher()(stream).join() == 123
        
    def test_should_have_a_string(self):
        stream = Stream('"soleil" 123"')

        assert StringMatcher()(stream).join() == "soleil"        

    def test_should_have_a_string_delim(self):
        stream = Stream("'soleil' 123")

        assert StringDelimMatcher()(stream).join() == "soleil"

    def test_should_have_an_int_and_string(self):
        stream = Stream("123'soleil'")
        genlex = Genlex() <<accept>> StringDelimMatcher() \
                          <<accept>> IntMatcher()
        
        tokens = genlex.parse(stream)

        assert tokens.next() == 123
        assert tokens.next() == "soleil"
        assert tokens.next() == None
                
    def test_should_have_an_int_and_string_with_spaces(self):
        stream = Stream("123 'soleil'")
        genlex = Genlex() <<skip>>   Generic((lambda s:s),r'\s+') \
                          <<accept>> StringDelimMatcher() \
                          <<accept>> IntMatcher()
                    
        tokens = genlex.parse(stream)

        assert tokens.next() == 123
        assert tokens.next() == "soleil"
        assert tokens.next() == None
                
def suite():
   suite = unittest.TestSuite()
   suite.addTest(unittest.makeSuite(TestCase))
   return suite

if __name__ == '__main__':
    unittest.main()
