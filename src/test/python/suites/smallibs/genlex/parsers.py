''' Test for generic parser '''

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
        matcher = Match.create()
        
        matcher <<case>> (int,matcher) <<then>> True \
                <<case>> (str,matcher) <<then>> True \
                <<case>> _             <<then>> True 
        
        assert IntMatcher()(stream).join() == 123
                
def suite():
   suite = unittest.TestSuite()
   suite.addTest(unittest.makeSuite(TestCase))
   return suite

if __name__ == '__main__':
    unittest.main()
