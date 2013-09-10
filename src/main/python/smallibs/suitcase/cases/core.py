""" Core case """

class MatchResult:
    def __init__(self,value):
        self.value = value

class Case:
    @staticmethod
    def fromObject(o):
        if type(o) == int:
            return Int(o)
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

class IntCase(Case):
    def __init__(self,value):
        Case.__init__(self)
        self.value = value

    def unapply(self,value):
        return MatchResult(value) if self.value == value else None

def Int(value):
    return IntCase(value)

