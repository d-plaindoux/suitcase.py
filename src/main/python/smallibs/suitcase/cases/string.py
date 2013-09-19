""" List Cases """

import re

from core import Case, MatchResult
from smallibs.utils.monads.options import option

# ----------------------------------------
# Internal classes
# ----------------------------------------

class __RegexCase(Case):
    def __init__(self,value):
        Case.__init__(self)
        self.value = "^" + value + "$"

    def unapply(self,value):
        return option(re.match(self.value,value)).bind(lambda res:option(MatchResult(res.groups(),[])))

# ----------------------------------------
# Public factories
# ----------------------------------------

Regex = lambda value: __RegexCase(value)

