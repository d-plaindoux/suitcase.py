import unittest

from smallibs.monads.options import option
from smallibs.suitcase.cases.core import Case, var, _
from smallibs.suitcase.cases.list import Empty,Cons
from smallibs.suitcase.cases.string import Regex
from smallibs.monads.monad import bind

def test(a,expected):
    return (a |bind| (lambda _:option(True))).join() == expected

class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_type_should_match(self):
        assert test(Case.of(int).unapply(1),True)

    def test_type_should_not_match(self):
        assert test(Case.of(str).unapply(1),None)

    def test_int_should_match(self):
        assert test(Case.of(1).unapply(1),True)

    def test_int_should_not_match(self):
        assert test(Case.of(0).unapply(1),None)

    def test_float_should_match(self):
        assert test(Case.of(1.2).unapply(1.2),True)

    def test_float_should_not_match(self):
        assert test(Case.of(0.2).unapply(1.2),None)

    def test_bool_should_match(self):
        assert test(Case.of(True).unapply(True),True)

    def test_bool_should_not_match(self):
        assert test(Case.of(True).unapply(False),None)

    def test_string_should_match(self):
        assert test(Case.of('Hello').unapply('Hello'),True)

    def test_string_should_not_match(self):
        assert test(Case.of('Hello').unapply('World'),None)

    def test_var_should_match(self):
        # ERROR
        assert test(var.unapply(1),True)

    def test_var_should_not_match_int(self):
        assert test(var.of(0).unapply(1),None)

    def test_any_should_match(self):
        assert test(_.unapply(1),True)

    def test_empty_case_should_match_empty_list(self):
        assert test(Empty.unapply([]),True)

    def test_empty_case_should_not_match_not_empty_list(self):
        assert test(Empty.unapply([1]),None)
        
    def test_cons_case_should_match_not_empty_list(self):
        assert test(Cons(1,Empty).unapply([1]),True)
        
    def test_cons_case_should_not_match_not_empty_list(self):
        assert test(Cons(1,Empty).unapply([2]),None)
        
    def test_regexp_should_match_string(self):
        assert test(Regex("a*b*").unapply("aaabbb"),True)

    def test_regexp_should_not_match_string(self):
        assert test(Regex("a*b*").unapply("aaabbbcccc"),None)
        
    def test_regexp_should_not_match_again_string(self):
        assert test(Regex("a*b*").unapply("ccccaaabbb"),None)
        
def suite():
   suite = unittest.TestSuite()
   suite.addTest(unittest.makeSuite(TestCase))
   return suite

if __name__ == '__main__':
    unittest.main()
