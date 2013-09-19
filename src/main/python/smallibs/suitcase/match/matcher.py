""" Match class """

from types import FunctionType
from smallibs.suitcase.cases.core import Case

class MatchingException(Exception):
    def __init__(self):
        pass

class Match:
    @staticmethod
    def create():
        return Match()

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
        return Match.__CaseOf(self,pattern)

    def match(self,term):
        for rule in self.rules:
            result = rule[0].unapply(term).join()
            if result:
                variables = result.getVariables()
                return rule[1](variables)

        raise MatchingException()
