""" Maybe monad """

def unit(v):
    return v

def bind(v,f):
    return f(v) if (v) else None
