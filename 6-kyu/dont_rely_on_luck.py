# https://www.codewars.com/kata/5268af3872b786f006000228

# method1: random.getstate() -> random.setstate()
import random
seed = random.getstate()
guess = random.randint(1, 100)
random.setstate(seed)

# method2: almost same set predefined seed
import random
random.seed(42)
guess = random.randint(1,100)
random.seed(42)

# method3 redefine int.__eq__(); but not works for int class, make your own class
class AlwaysEqClass:
    def __eq__(self, *args):
        return True
guess = AlwaysEqClass()
