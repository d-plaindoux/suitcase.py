''' Dedicated lexer based on specific recognizer '''

import re

class Stream:
    def __init__(self,value):
        self._offset = 0;
        self._value = value

    def offset(self,value):
        self._offset += value

    def value(self):
        return self._value

class Recognizer:
    def __init__(self, kind, regex):
        self.kind = kind
        self.regex = '^(' + regex + ')'

    def __call__(self,stream):
        result = re.match(self.regex,stream.value())
        if result:
            stream.offset(len(result.group()))
            groups = result.groups()
            return self.kind(groups[len(groups)-1])
        else:
            None

class IntRecognizer(Recognizer):
    def __init__(self):
        Recognizer.__init__(self,(lambda s:int(s)),'^\\d+')
        
class StringRecognizer(Recognizer):
    def __init__(self):
        Recognizer.__init__(self,(lambda s:s),'"([^"]*)"')
        
class StringDelimRecognizer(Recognizer):
    def __init__(self):
        Recognizer.__init__(self,(lambda s:s),"'([^']*)'")
        
