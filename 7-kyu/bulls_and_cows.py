# https://www.codewars.com/kata/5be1a950d2055d589500005b
class BullsAndCows:
    def __init__(self, n):
        if not isinstance(n, int) or n < 0 or len(str(n)) != 4 or len(set(str(n))) != 4:
            raise ValueError(f'ValueError {n=}')
        self.n = n
        self.turns_left = 8
        self.won = False
    
    def compare_with(self, n):
        if self.won:
            return 'You already won!'
        if self.turns_left <=0:
            return "Sorry, you're out of turns!"
        if not isinstance(n, int) or n < 0 or len(str(n)) != 4 or len(set(str(n))) != 4:
            raise ValueError(f'ValueError {n=}')
        self.turns_left -= 1

        bulls = [a == b for a,b, in zip(str(self.n), str(n))]
        cows  = [ b     for a,b, in zip(str(self.n), str(n)) if a != b and b in str(self.n)]
        if all(bulls):
            self.won = True
            return "You win!"
        else:
            bulls = sum(bulls)
            cows = len(cows)
            plural_bulls = 's' if bulls != 1 else ''
            plural_cows = 's' if cows != 1 else ''
            return f'{bulls} bull{plural_bulls} and {cows} cow{plural_cows}'

        
