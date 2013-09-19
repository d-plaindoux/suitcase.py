''' Dedicated lexer based on specific recognizer '''

import re
from smallibs.monads.monad import bind
from smallibs.monads.options import option

class Stream:
    def __init__(self,value):
        self._offset = 0;
        self._value = value

    def offset(self,value):
        self._offset += value
        return self

    def value(self):
        return self._value

class Recognizer:
    def __init__(self, kind, regex):
        self.kind = kind
        self.regex = '^(' + regex + ')'

    def __call__(self,stream):
        return (option(re.match(self.regex,stream.value())) |bind| (
                lambda result: option(stream.offset(len(result.group()))) |bind| (
                lambda _: option(self.kind(result.groups()[len(result.groups())-1]))))).join()

class IntRecognizer(Recognizer):
    def __init__(self):
        Recognizer.__init__(self,(lambda s:int(s)),'^\\d+')
        
class StringRecognizer(Recognizer):
    def __init__(self):
        Recognizer.__init__(self,(lambda s:s),'"([^"]*)"')
        
class StringDelimRecognizer(Recognizer):
    def __init__(self):
        Recognizer.__init__(self,(lambda s:s),"'([^']*)'")
        
