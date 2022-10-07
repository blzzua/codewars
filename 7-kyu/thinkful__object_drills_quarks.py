# https://www.codewars.com/kata/5882b052bdeafec15e0000e6

class Quark(object):
    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor
        self.baryon_number = 1/3
    
    def interact(self, q2):
        self.color, q2.color = q2.color, self.color

