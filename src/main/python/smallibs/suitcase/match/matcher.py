""" Matcher class """

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

        def then(self, value):
            return self.matcher.addRule(self.pattern,value)            

    #------------------------------

    def __init__(self):
        self.rules = []

    def addRule(self,pattern,value):
        self.rules.extend([(pattern,value)])
        return self

    def caseOf(self, pattern):
        return Matcher.__CaseOf(self,pattern)

    def match(self,term):
        for rule in self.rules:
            result = rule[0].unapply(term)
            if result:
                return rule[1](result.variables)

        raise MatchingException()
