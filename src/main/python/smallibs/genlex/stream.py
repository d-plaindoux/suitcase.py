''' Stream class / Simple and naive implementation for the moment '''

class Stream:
    def __init__(self,value):
        self._offset = 0;
        self._value = value

    def offset(self,value):
        self._value = self._value[value:]
        return self._value

    def value(self):
        return self._value

    def isEmpty(self):
        return len(self._value) == 0
