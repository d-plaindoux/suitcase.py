""" List Cases """

from core import Case, MatchResult
from smallibs.utils.monads.maybe import *

# ----------------------------------------
# Internal classes
# ----------------------------------------

class __EmptyCase(Case):
    def __init__(self):
        Case.__init__(self)

    def unapply(self,value):
        return MatchResult(value) if set(value) == set([]) else None

class __ConsCase(Case):
    def __init__(self,head,tail):
        Case.__init__(self)
        self.head = Case.of(head)
        self.tail = Case.of(tail)

    def unapply(self,value):
        mayBeIterator = bind(type(value) == list,lambda _:iter(value))
        return bind(mayBeIterator, lambda iterator:
                    bind(self.head.unapply(iterator.next()), lambda rhead:
                         bind(self.tail.unapply(list(iterator)), lambda rtail:
                              MatchResult(value) << rhead << rtail)))

    def freeVariables():
        return 

# ----------------------------------------
# Public factories
# ----------------------------------------

Empty = __EmptyCase()
Cons = lambda head,tail: __ConsCase(head,tail)

