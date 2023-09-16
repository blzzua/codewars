# https://www.codewars.com/kata/587f1e1f39d444cee6000ad4

class Vector(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self, other):
        return Vector(other.x + self.x, other.y + self.y)
        
