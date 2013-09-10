""" Core case """

from smallibs.utils.monads import Maybe

class MatchResult:
    def __init__(self,value):
        self.value = value

class Case:
    @staticmethod
    def fromObject(o):
        if type(o) == int:
            return Int(o)
        elif type(o) == str:
            return String(o)
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

    def unapply(self,value):
        return Maybe.bind(self.value == value, lambda _:MatchResult(value))

class __IntCase(AtomCase):
    def __init__(self,value):
        AtomCase.__init__(self,value)
        assert type(value) == int

class __StringCase(AtomCase):
    def __init__(self,value):
        AtomCase.__init__(self,value)
        assert type(value) == str

# ----------------------------------------
# Public factories
# ----------------------------------------

Int    = lambda value: __IntCase(value)
String = lambda value: __StringCase(value)

