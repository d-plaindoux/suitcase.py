""" Matcher class """

from types import FunctionType
from smallibs.suitcase.cases.core import Case

class MatchingException(Exception):
    def __init__(self):
        pass

class Matcher:
    @staticmethod
    def create():
        return Matcher()

    #------------------------------

    class __CaseOf:
        def __init__(self,matcher,pattern):
            self.matcher = matcher
            self.pattern = Case.of(pattern)

        def then(self, callback):
            if isinstance(callback, FunctionType):
                return self.matcher.addRule(self.pattern,callback)
            else:
                return self.matcher.addRule(self.pattern,lambda _: callback)

    #------------------------------

    def __init__(self):
        self.rules = []

    def addRule(self,pattern,callback):
        self.rules.extend([(pattern,callback)])
        return self

    def caseOf(self, pattern):
        return Matcher.__CaseOf(self,pattern)

    def match(self,term):
        for rule in self.rules:
            result = rule[0].unapply(term)
            if result:
                return rule[1](result.getVariables())

        raise MatchingException()
