""" Matcher class """

class Matcher:

    @staticmethod
    def create():
        return Matcher()

    #------------------------------

    class __CaseOf:
        def __init__(self,matcher,pattern):
            self.matcher = matcher
            self.pattern = pattern

        def then(self, value):
            return self.matcher.addRule(self.pattern,value)            

    #------------------------------

    def __init__(self):
        self.rules = []

    def caseOf(self, pattern):
        return Matcher.__CaseOf(self,pattern)

    def addRule(self,pattern,value):
        self.rules.extend([(pattern,value)])
        return self

    def match(self,term):
        pass
