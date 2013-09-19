""" Maybe monad """

from monad import Monad

class Something(Monad):
    def __init__(self,value):
        Monad.__init__(self,value)

    def bind(self, funcall):
        return funcall(self.value)

class Nothing(Monad):
    def __init__(self):
        Monad.__init__(self,None)

    def bind(self,funcall):
        return self

def option(value=None):
    return Nothing() if value == None else Something(value)
