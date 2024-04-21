# https://www.codewars.com/kata/5825792ada030e9601000782

def zip_with(fn,a1,a2):
    return [fn(a,b) for a,b in zip(a1, a2)]

# clever shrt solution
return list(map(fn, a1, a2))
