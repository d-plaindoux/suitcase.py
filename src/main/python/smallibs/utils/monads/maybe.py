""" Maybe monad """

def unit(v):
    return v

def bind(v,f):
    return None if v == None else f(v)

