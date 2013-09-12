""" Core case """

from smallibs.utils.monads.maybe import *

# ----------------------------------------
# Public classes
# ----------------------------------------

class MatchResult:
    def __init__(self,value,variables):
        self.value = value
        self.variables = variables

    def __lshift__(self,value):
        self.variables.extend(value.getVariables())
        return self

    def getVariables(self):
        return self.variables

class Case:
    @staticmethod
    def of(o):
        basicConverter = {
            int   : Int,
            float : Float,
            str   : String,
            bool  : Bool,
            type  : Type
        }

        if type(o) in basicConverter:
            return basicConverter[type(o)](o)
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
        return bind(self.compareWith(value), lambda _:MatchResult(value,[]))

# ----------------------------------------

class __AnyCase(Case):
    def __init__(self):
        Case.__init__(self)

    def unapply(self,value):
        return MatchResult(value,[])

# ----------------------------------------

class __VarCase(Case):
    def __init__(self,value=None):
        Case.__init__(self)
        self.value = value if value else _

    def of(self,value):
        return __VarCase(value)

    def unapply(self,value):
        return bind(self.value.unapply(value),lambda _:MatchResult(value,[value]))

# ----------------------------------------

class __IntCase(AtomCase):
    def __init__(self,value):
        AtomCase.__init__(self,value)
        assert type(value) == int

# ----------------------------------------

class __FloatCase(AtomCase):
    def __init__(self,value):
        AtomCase.__init__(self,value)
        assert type(value) == float

# ----------------------------------------

class __StringCase(AtomCase):
    def __init__(self,value):
        AtomCase.__init__(self,value)
        assert type(value) == str

# ----------------------------------------

class __BoolCase(AtomCase):
    def __init__(self,value):
        AtomCase.__init__(self,value)
        assert type(value) == bool

# ----------------------------------------

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
Float  = lambda value: __FloatCase(value)
String = lambda value: __StringCase(value)
Bool   = lambda value: __BoolCase(value)
Type   = lambda value: __TypeCase(value)
_      = __AnyCase()
var    = __VarCase()
