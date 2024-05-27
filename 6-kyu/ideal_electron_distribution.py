# https://www.codewars.com/kata/59175441e76dc9f9bc00000f

def saturate(n):
    while True:
        yield 2 * (n**2)
        n += 1
    
def atomic_number(electrons):
    orbit_gen = saturate(1)       # saturate = [2, 8, 18, 32, 50, 72, 98]
    res = []
    while electrons > 0:
        orbits = next(orbit_gen)  # orbits = saturate.pop(0)
        if electrons <= orbits:
            res.append(electrons)
            electrons = max(electrons - orbits,0)
        else:
            electrons -= orbits
            res.append(orbits)
    return  res
