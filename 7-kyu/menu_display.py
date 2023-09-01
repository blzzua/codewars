# https://www.codewars.com/kata/64c766dd16982000173d5ba1

class Menu:
    def __init__(self, values):
        self.values = values
        self.active = 0
    
    def to_the_right(self):
        self.active = (self.active + 1) % len(self.values)
        
    def to_the_left(self):
        self.active = (self.active + len(self.values) - 1) % len(self.values)
        
    def display(self):
        return str([ [str(v)] if i == self.active else str(v) for i, v in enumerate(self.values)])
