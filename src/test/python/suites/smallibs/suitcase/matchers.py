import unittest

from smallibs.utils.monads.maybe import *
from smallibs.suitcase.cases.core import Case, _
from smallibs.suitcase.cases.list import Empty,Cons
from smallibs.suitcase.match.matcher import Matcher, MatchingException

class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_should_match_int(self):
        matcher = Matcher.create()
        matcher.caseOf(1).then(lambda r:True)
        assert matcher.match(1)
        
    def test_should_not_match_int(self):
        matcher = Matcher.create()
        matcher.caseOf(1).then(lambda r:True)
        matcher.caseOf(_).then(lambda r:False)

        assert matcher.match(0) == False
        
def suite():
   suite = unittest.TestSuite()
   suite.addTest(unittest.makeSuite(TestCase))
   return suite

if __name__ == '__main__':
    unittest.main()
