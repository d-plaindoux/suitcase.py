""" Maybe monad """

from monad import Monad

class Maybe(Monad):
    def __init__(self):
        Monad.__init__(self)
                
    def bind(self, funcall):
        return funcall(self.value)

class Nothing(Monad):
    def __init__(self):
        Monad.init__(self,value)

    def bind(self,funcall):
        return self
