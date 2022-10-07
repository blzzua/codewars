# https://www.codewars.com/kata/55cd4ce59382498cbd000080

class List:
    def __init__(self,type):
        self.type=type
        self.items=[]
        self.count=0
    
    def add(self, item):
        if type(item) != self.type:
            return f"This item is not of type: {self.type.__name__}"
        self.items.append(item)
        self.count += 1
        return self

