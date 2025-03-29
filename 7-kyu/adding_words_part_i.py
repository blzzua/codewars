# https://www.codewars.com/kata/592eaf848c91f248ca000012

class Arith():
    def __init__(self, value):
        self._S2N = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 
        'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10, 'eleven': 11, 
        'twelve': 12, 'thirteen': 13, 'fourteen': 14, 'fifteen': 15, 'sixteen': 16, 
        'seventeen': 17, 'eighteen': 18, 'nineteen': 19, 'twenty': 20}
        self._N2S= {v:k for k,v in self._S2N.items()}
        self.value = self._S2N.get(value)

    def add(self, othervalue):
        return str(self._N2S.get(self.value + self._S2N.get(othervalue)))

