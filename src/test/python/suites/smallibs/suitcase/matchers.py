import unittest

from smallibs.utils.monads.maybe import *
from smallibs.suitcase.cases.core import Case, _, var
from smallibs.suitcase.cases.list import Empty,Cons
from smallibs.suitcase.match.matcher import Matcher, MatchingException

class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_should_match_int(self):
        matcher = Matcher.create()
        matcher.caseOf(1).then(True)
        matcher.caseOf(_).then(False)
        
        assert matcher.match(1)
        
    def test_should_not_match_int(self):
        matcher = Matcher.create()
        matcher.caseOf(1).then(True)
        matcher.caseOf(_).then(False)

        assert matcher.match(0) == False

    def test_should_match_empty(self):
        matcher = Matcher.create()
        matcher.caseOf(Empty).then(True)
        matcher.caseOf(_).then(False)
            
        assert matcher.match([])
        
    def test_should_not_match_empty(self):
        matcher = Matcher.create()
        matcher.caseOf(Empty).then(True)
        matcher.caseOf(_).then(False)

        assert matcher.match([1]) == False
        
    def test_should_match_cons(self):
        matcher = Matcher.create()
        matcher.caseOf(Cons(_,_)).then(True)
        matcher.caseOf(_).then(False)

        assert matcher.match([1])
        
    def test_should_not_match_cons(self):
        matcher = Matcher.create()
        matcher.caseOf(Cons(_,_)).then(True)
        matcher.caseOf(_).then(False)

        assert matcher.match([]) == False

    def test_should_capture_int(self):
        matcher = Matcher.create()
        matcher.caseOf(var).then(lambda i:i[0])

        assert matcher.match(1) == 1
        
    def test_should_capture_match_cons_head(self):
        matcher = Matcher.create()
        matcher.caseOf(Cons(var,_)).then(lambda i:i[0])
        matcher.caseOf(_).then(False)

        assert matcher.match([1]) == 1
        
def suite():
   suite = unittest.TestSuite()
   suite.addTest(unittest.makeSuite(TestCase))
   return suite

if __name__ == '__main__':
    unittest.main()
