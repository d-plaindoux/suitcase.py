import unittest

from smallibs.suitcase.cases.core import Case, _, var, reentrant
from smallibs.suitcase.cases.list import Empty,Cons
from smallibs.suitcase.cases.string import Regex
from smallibs.suitcase.match.matcher import Match, MatchingException

class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_should_match_int(self):
        matcher = Match.create()
        matcher.caseOf(1).then(True)
        matcher.caseOf(_).then(False)
        
        assert matcher.match(1)
        
    def test_should_not_match_int(self):
        matcher = Match.create()
        matcher.caseOf(1).then(True)
        matcher.caseOf(_).then(False)

        assert matcher.match(0) == False

    def test_should_match_empty(self):
        matcher = Match.create()
        matcher.caseOf(Empty).then(True)
        matcher.caseOf(_).then(False)
            
        assert matcher.match([])
        
    def test_should_not_match_empty(self):
        matcher = Match.create()
        matcher.caseOf(Empty).then(True)
        matcher.caseOf(_).then(False)

        assert matcher.match([1]) == False
        
    def test_should_match_cons(self):
        matcher = Match.create()
        matcher.caseOf(Cons(_,_)).then(True)
        matcher.caseOf(_).then(False)

        assert matcher.match([1])
        
    def test_should_not_match_cons(self):
        matcher = Match.create()
        matcher.caseOf(Cons(_,_)).then(True)
        matcher.caseOf(_).then(False)

        assert matcher.match([]) == False

    def test_should_capture_int(self):
        matcher = Match.create()
        matcher.caseOf(var).then(lambda i:i[0])

        assert matcher.match(1) == 1
        
    def test_should_capture_match_cons_head(self):
        matcher = Match.create()
        matcher.caseOf(Cons(var,_)).then(lambda i:i[0])
        matcher.caseOf(_).then(False)

        assert matcher.match([1]) == 1
        
    def test_should_add_all_elements(self):
        matcher = Match.create()
        matcher.caseOf(Empty).then(0)
        matcher.caseOf(Cons(var,var)).then(lambda i:i[0] + matcher.match(i[1]))

        assert matcher.match([1,2,3]) == 6 # A perfect number :-)

    def test_should_add_all_elements_with_reentrant_matcher(self):
        matcher = reentrant(Match.create())
        matcher.caseOf(Empty).then(0)
        matcher.caseOf(Cons(var,var.of(matcher))).then(lambda i:i[0] + i[1])

        assert matcher.match([1,2,3]) == 6 # A perfect number :-)
        
    def test_should_match_string_using_regex(self):
        matcher = Match.create()
        matcher.caseOf(var.of(Regex('(\w+)\s+(\w+)!'))).then(lambda r:r[0])

        assert matcher.match('Hello World!') == ('Hello','World')
                
def suite():
   suite = unittest.TestSuite()
   suite.addTest(unittest.makeSuite(TestCase))
   return suite

if __name__ == '__main__':
    unittest.main()
