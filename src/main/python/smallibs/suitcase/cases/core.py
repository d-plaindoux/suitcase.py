""" Core case """

from smallibs.monads.options import option

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

    def __str__(self):
        return "MatchResult(%s,%s)" % (self.value,self.variables)

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
            return (basicConverter[type(o)](o))
        elif isinstance(o,Case):
            return (o)
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

class __TraceCase(Case):        
    def __init__(self,value):
        Case.__init__(self)
        self.value = value

    def unapply(self,value):
        print "# %s.unapply(%s) = ???" % (self.value,value)
        result = self.value.unapply(value)
        print "# %s.unapply(%s) = %s" % (self.value,value,result)
        return result

# ----------------------------------------

class __AnyCase(Case):
    def __init__(self):
        Case.__init__(self)

    def unapply(self,value):
        return option(MatchResult(value,[]))

# ----------------------------------------

class __VarCase(Case):
    def __init__(self,value):
        Case.__init__(self)        
        self.value = _ if value == None else Case.of(value)

    def of(self,value):
        return varWith(value)

    def unapply(self,value):
        return self.value.unapply(value).bind(lambda res:option(MatchResult(value,[res.value]) << res))

# ----------------------------------------

class AtomCase(Case):
    def __init__(self,value):
        Case.__init__(self)
        assert value != None
        self.value = value

    def compareWith(self,value):
        return option(True if self.value == value else None)

    def unapply(self,value):
        return self.compareWith(value).bind(lambda _:option(MatchResult(value,[])))

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
        return option(True if isinstance(value,self.value) else None)

# ----------------------------------------

class __ReentrantCase(Case):
    def __init__(self,matcher):
        Case.__init__(self)
        self.matcher = matcher

    def unapply(self,value):
        try:
            return option(MatchResult(self.match(value),[]))
        except:
            return option()

    def caseOf(self, pattern):
        return self.matcher.caseOf(pattern)

    def match(self,term):
        return self.matcher.match(term)
        
# ----------------------------------------
# Public factories
# ----------------------------------------

Int       = lambda value: __IntCase(value)
Float     = lambda value: __FloatCase(value)
String    = lambda value: __StringCase(value)
Bool      = lambda value: __BoolCase(value)
Type      = lambda value: __TypeCase(value)
varWith   = lambda value: __VarCase(value)
reentrant = lambda value: __ReentrantCase(value)
trace     = lambda value: __TraceCase(value)

_         = __AnyCase()
var       = __VarCase(None)

# Force scope
