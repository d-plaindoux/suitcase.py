''' Dedicated matchers applied on a stream '''

import re
from smallibs.utils.infix import Infix
from smallibs.monads.monad import bind
from smallibs.monads.options import option

class AbstractMatcher:
    def __init__(self, kind, regex):
        self.kind = kind
        self.regex = re.compile('^(' + regex + ')')

    def __call__(self,stream):
        return option(re.match(self.regex,stream.value())) |bind| (
               lambda result: option(stream.offset(len(result.group()))) |bind| (
               lambda _: option(self.kind(result.groups()[len(result.groups())-1]))))

class IntMatcher(AbstractMatcher):
    def __init__(self):
        AbstractMatcher.__init__(self,(lambda s:int(s)),'^\\d+')
        
class StringMatcher(AbstractMatcher):
    def __init__(self):
        AbstractMatcher.__init__(self,(lambda s:s),'"([^"]*)"')
        
class StringDelimMatcher(AbstractMatcher):
    def __init__(self):
        AbstractMatcher.__init__(self,(lambda s:s),"'([^']*)'")

class Generic(AbstractMatcher):
    def __init__(self,kind,pattern):
        AbstractMatcher.__init__(self,kind,pattern)
