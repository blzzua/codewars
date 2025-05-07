# https://www.codewars.com/kata/6584b7cac29ca91dd9124009

def convert_lojban(lojban):
    literals = ['no','pa','re','ci','vo','mu','xa','ze','bi','so']
    numbers = [literals.index(a+b) for a,b in zip(lojban[::2],lojban[1::2])]
    res = 0 
    power = 0
    while numbers:
        res += 10**(power) * numbers.pop()
        power += 1
    return res

