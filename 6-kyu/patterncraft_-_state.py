# https://www.codewars.com/kata/5682e72eb7354b2f39000021

class SiegeState:
    def __init__(self):
        self._can_move = False
        self.damage = 20

class TankState:
    def __init__(self):
        self._can_move = True
        self.damage = 5

class Tank:
    def __init__(self):
        self.state = TankState()

    def can_move(self):
        return self.state._can_move
    
    def damage(self):
        return self.state.damage
