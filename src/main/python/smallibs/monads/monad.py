""" Monad definition """

class Monad:
    def __init__(self,value):
        self.value = value;

    def bind(self,funcall):
        raise NotImplementedError()

    def join(self):
        return self.value
