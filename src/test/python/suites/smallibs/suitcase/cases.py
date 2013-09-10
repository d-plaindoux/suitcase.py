import unittest

from smallibs.utils.monads import Maybe
from smallibs.suitcase.cases.list import Empty,Cons

class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_empty_case_should_match_empty_list(self):
        assert Maybe.bind(Empty.unapply([]),lambda a:True)

    def test_empty_case_should_not_match_not_empty_list(self):
        assert Maybe.bind(Empty.unapply([1]),lambda a:True) == None
        
    def test_cons_case_should_match_not_empty_list(self):
        assert Maybe.bind(Cons(1,Empty).unapply([1]),lambda a:True)
        
    def test_cons_case_should_not_match_not_empty_list(self):
        assert Maybe.bind(Cons(1,Empty).unapply([2]),lambda a:True) == None
        
def suite():
   suite = unittest.TestSuite()
   suite.addTest(unittest.makeSuite(TestCase))
   return suite

if __name__ == '__main__':
    unittest.main()
