""" List Cases """

from core import Case, MatchResult
from smallibs.utils.monads import Maybe

class EmptyCase(Case):

    def __init__(self):
        Case.__init__(self)

    def unapply(self,value):
        return MatchResult(value) if set(value) == set([]) else None

Empty = EmptyCase()

class ConsCase(Case):
    def __init__(self,head,tail):
        Case.__init__(self)
        self.head = Case.fromObject(head)
        self.tail = Case.fromObject(tail)

    def unapply(self,value):
        iterator = iter(value)
        return Maybe.bind(self.head.unapply(iterator.next()), lambda r:
               Maybe.bind(self.tail.unapply(list(iterator)), lambda r: MatchResult(value)))

def Cons(head,tail):
    return ConsCase(head,tail)

