import unittest

from smallibs.suitcase.cases import _,var,reentrant
from smallibs.suitcase.cases.list import *
from smallibs.suitcase.cases.string import *
from smallibs.suitcase.match import *

class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_should_match_int(self):
        matcher = Match.create()
        matcher <<case>> 1 <<then>> True \
                <<case>> _ <<then>> False
        
        assert matcher.match(1)
        
    def test_should_not_match_int(self):
        matcher = Match.create()
        matcher <<case>> 1 <<then>> True \
                <<case>> _ <<then>> False

        assert matcher.match(0) == False

    def test_should_match_empty(self):
        matcher = Match.create()
        matcher <<case>> Empty <<then>> True \
                <<case>> _     <<then>> False
            
        assert matcher.match([])
        
    def test_should_not_match_empty(self):
        matcher = Match.create()
        matcher <<case>> Empty <<then>> True \
                <<case>> _     <<then>> False

        assert matcher.match([1]) == False
        
    def test_should_match_cons(self):
        matcher = Match.create()
        matcher <<case>> Cons(_,_) <<then>> True \
                <<case>> _         <<then>> False

        assert matcher.match([1])
        
    def test_should_not_match_cons(self):
        matcher = Match.create()
        matcher <<case>> Cons(_,_) <<then>> True \
                <<case>> _         <<then>> False

        assert matcher.match([]) == False

    def test_should_capture_int(self):
        matcher = Match.create()
        matcher <<case>> var <<then>> (lambda i:i[0])

        assert matcher.match(1) == 1
        
    def test_should_capture_match_cons_head(self):
        matcher = Match.create()
        matcher <<case>> Cons(var,_) <<then>> (lambda i:i[0])
        matcher <<case>> _           <<then>> False

        assert matcher.match([1]) == 1
        
    def test_should_add_all_elements(self):
        matcher = Match.create()
        matcher <<case>> Empty         <<then>> 0 \
                <<case>> Cons(var,var) <<then>> (lambda i:i[0] + matcher.match(i[1]))

        assert matcher.match([1,2,3]) == 6 # A perfect number :-)

    def test_should_add_all_elements_with_reentrant_matcher(self):
        matcher = reentrant(Match.create())
        matcher <<case>> Empty                     <<then>> 0 \
                <<case>> Cons(var,var.of(matcher)) <<then>> (lambda i:i[0] + i[1])

        assert matcher.match([1,2,3]) == 6 # A perfect number :-)
        
    def test_should_match_string_using_regex(self):
        matcher = Match.create()
        matcher <<case>> var.of(Regex('(\w+)\s+(\w+)!')) <<then>> (lambda r:r[0])

        assert matcher.match('Hello World!') == ('Hello','World')
                
def suite():
   suite = unittest.TestSuite()
   suite.addTest(unittest.makeSuite(TestCase))
   return suite

if __name__ == '__main__':
    unittest.main()
