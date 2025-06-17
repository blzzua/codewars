# https://www.codewars.com/kata/52d3b68215be7c2d5300022f

class Event():
    def __init__(self):
        self._list = []
    
    def subscribe(self, f):
        self._list.append(f)
    
    def unsubscribe(self, f):
        self._list.remove(f)
    
    def emit(self, *arg):
        for func in self._list:
            func(*arg)
