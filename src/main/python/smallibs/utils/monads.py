""" Maybe monad """

class Maybe:
    @staticmethod
    def unit(v): return v

    @staticmethod    
    def bind(v,f): return f(v) if (v) else None


