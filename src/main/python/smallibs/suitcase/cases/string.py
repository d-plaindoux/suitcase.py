""" List Cases """

from core import Case, MatchResult
from smallibs.utils.monads.maybe import *

# ----------------------------------------
# Internal classes
# ----------------------------------------

class _RegexCase(Case):
    def __init__(self,value):
        Case.__init__(self)
        self.value = "^" + value

    def unapply(self,value):
        return 

# ----------------------------------------
# Public factories
# ----------------------------------------

Regex = lambda value: __RegexCase(value)

