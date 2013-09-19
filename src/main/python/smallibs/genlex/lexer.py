''' Dedicated lexer based on specific recognizer '''

from smallibs.utils.infix import Infix

class TokenStream:
    def __init__(self,genlex,stream):
        self.genlex = genlex
        self.stream = stream

    def __skip(self):
        if self.stream.isEmpty():
           return None 
       
        for recognizer in self.genlex.skipped:
            result = recognizer(self.stream).join()
            if result != None:
                return result

        return None
            
    def isFinish():
        return self.stream.isEmpty()
            
    def next(self):
        while self.__skip():
            pass
        
        if self.stream.isEmpty():
           return None 

        for recognizer in self.genlex.recognizers:
            result = recognizer(self.stream).join()
            if result != None:
                return result

        return None
        
class Genlex:
    def __init__(self):
        self.recognizers = []
        self.skipped = []

    def skip(self,skip):
        self.skipped.extend([skip])
        return self

    def accept(self,recognizer):
        self.recognizers.extend([recognizer])
        return self
    
    def parse(self,stream):
        return TokenStream(self,stream)

skip = Infix(lambda g,s: g.skip(s))
accept= Infix(lambda g,r: g.accept(r))
