# https://www.codewars.com/kata/594979a364becbc1ab00003a

class LCG(object):
    a = 2
    c = 3
    m = 10
    x = 0

    def __init__(self, seed):
        self.seed = seed
        self.x = seed

    def random(self):
        self.x = (self.a * self.x + self.c) % self.m 
        return self.x / self.m 
