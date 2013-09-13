""" List Cases """

import re

from core import Case, MatchResult
from smallibs.utils.monads.maybe import *

# ----------------------------------------
# Internal classes
# ----------------------------------------

class __RegexCase(Case):
    def __init__(self,value):
        Case.__init__(self)
        self.value = "^" + value + "$"

    def unapply(self,value):
        return bind(re.match(self.value,value),lambda res:MatchResult(res.groups(),[]))

# ----------------------------------------
# Public factories
# ----------------------------------------

Regex = lambda value: __RegexCase(value)

