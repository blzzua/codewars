# https://www.codewars.com/kata/5858326b994864753d0000d1

class SimTime:
    def __init__(self, speed=1):
        self.speed = 1
        self.real = 0
        self.sim = 0
    
    def get(self):
        return self.sim
    
    def set_speed(self, speed):
        self.speed = speed
        
    def update(self, value):
        diff = (value - self.real)
        if diff >= 0:
            self.real += diff
            self.sim += diff * self.speed
        else:
            raise ValueError("You shouldn't be able to travel back in time")
