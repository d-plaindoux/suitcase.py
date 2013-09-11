""" Core case """

from smallibs.utils.monads.maybe import *

class MatchResult:
    def __init__(self,value,variables=[]):
        self.value = value
        self.variables = variables

    def __lshift__(self,value):
        self.variables = [self.variables,value.variables]
        return self

class Case:
    @staticmethod
    def fromObject(o):
        if type(o) == int:
            return Int(o)
        elif type(o) == str:
            return String(o)
        elif type(o) == type:
            return Type(o)
        elif isinstance(o,Case):
            return o
        else:
            raise NotImplementedError()
    
    def __init__(self):
        pass

    def unapply(self,value):
        raise NotImplementedError()

    def freeVariables():
        return []

# ----------------------------------------
# Internal classes
# ----------------------------------------

class AtomCase(Case):
    def __init__(self,value):
        Case.__init__(self)
        self.value = value

    def compareWith(self,value):
        return self.value == value

    def unapply(self,value):
        return bind(self.compareWith(value), lambda _:MatchResult(value))

class __IntCase(AtomCase):
    def __init__(self,value):
        AtomCase.__init__(self,value)
        assert type(value) == int

class __StringCase(AtomCase):
    def __init__(self,value):
        AtomCase.__init__(self,value)
        assert type(value) == str

class __TypeCase(AtomCase):
    def __init__(self,value):
        AtomCase.__init__(self,value)
        assert type(value) == type

    def compareWith(self,value):
        return isinstance(value,self.value)

# ----------------------------------------
# Public factories
# ----------------------------------------

Int    = lambda value: __IntCase(value)
String = lambda value: __StringCase(value)
Type   = lambda value: __TypeCase(value)
