import unittest

from smallibs.utils.monads.maybe import *
from smallibs.suitcase.cases.core import Case
from smallibs.suitcase.cases.list import Empty,Cons

class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_type_should_match(self):
        assert bind(Case.of(int).unapply(1),lambda _:True)

    def test_type_should_not_match(self):
        assert bind(Case.of(str).unapply(1),lambda _:True) == None

    def test_int_should_match(self):
        assert bind(Case.of(1).unapply(1),lambda _:True)

    def test_int_should_not_match(self):
        assert bind(Case.of(0).unapply(1),lambda _:True) == None

    def test_float_should_match(self):
        assert bind(Case.of(1.2).unapply(1.2),lambda _:True)

    def test_float_should_not_match(self):
        assert bind(Case.of(0.2).unapply(1.2),lambda _:True) == None

    def test_bool_should_match(self):
        assert bind(Case.of(True).unapply(True),lambda _:True)

    def test_bool_should_not_match(self):
        assert bind(Case.of(True).unapply(False),lambda _:True) == None

    def test_string_should_match(self):
        assert bind(Case.of('Hello').unapply('Hello'),lambda _:True)

    def test_string_should_not_match(self):
        assert bind(Case.of('Hello').unapply('World'),lambda _:True) == None

    def test_empty_case_should_match_empty_list(self):
        assert bind(Empty.unapply([]),lambda _:True)

    def test_empty_case_should_not_match_not_empty_list(self):
        assert bind(Empty.unapply([1]),lambda _:True) == None
        
    def test_cons_case_should_match_not_empty_list(self):
        assert bind(Cons(1,Empty).unapply([1]),lambda _:True)
        
    def test_cons_case_should_not_match_not_empty_list(self):
        assert bind(Cons(1,Empty).unapply([2]),lambda _:True) == None
        
def suite():
   suite = unittest.TestSuite()
   suite.addTest(unittest.makeSuite(TestCase))
   return suite

if __name__ == '__main__':
    unittest.main()
