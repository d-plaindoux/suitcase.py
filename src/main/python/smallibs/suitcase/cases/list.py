""" List Cases """

from core import Case, MatchResult
from smallibs.utils.monads import Maybe

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
        self.head = Case.fromObject(head)
        self.tail = Case.fromObject(tail)

    def unapply(self,value):
        mayBeIterator = Maybe.bind(type(value) == list,lambda _:iter(value))
        return Maybe.bind(mayBeIterator, lambda iterator:
                          Maybe.bind(self.head.unapply(iterator.next()), lambda rhead:
                          Maybe.bind(self.tail.unapply(list(iterator)), lambda rtail: MatchResult(value))))

# ----------------------------------------
# Public factories
# ----------------------------------------

Empty = __EmptyCase()
Cons = lambda head,tail: __ConsCase(head,tail)

