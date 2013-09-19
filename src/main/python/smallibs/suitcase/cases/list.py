""" List Cases """

from core import Case, MatchResult
from smallibs.monads.monad import bind
from smallibs.monads.options import option

# ----------------------------------------
# Internal classes
# ----------------------------------------

class __EmptyCase(Case):
    def __init__(self):
        Case.__init__(self)

    def unapply(self,value):
        return option(MatchResult(value,[]) if set(value) == set([]) else None)

class __ConsCase(Case):
    def __init__(self,head,tail):
        Case.__init__(self)
        self.head = Case.of(head)
        self.tail = Case.of(tail)

    def unapply(self,value):
        if type(value) == list and len(value) > 0:
            iterator = iter(value)
            return self.head.unapply(iterator.next()) |bind| (
                   lambda rhead:self.tail.unapply(list(iterator)) |bind| (
                   lambda rtail:option(MatchResult(value,[]) << rhead << rtail)))
        else:
            return option()
        
    def freeVariables():
        variables = []
        variables.extend(self.head.freeVariables())
        variables.extend(self.tail.freeVariables())
        return variables

# ----------------------------------------
# Public factories
# ----------------------------------------

Empty = __EmptyCase()
Cons = lambda head,tail: __ConsCase(head,tail)

