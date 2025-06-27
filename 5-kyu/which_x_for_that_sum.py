# https://www.codewars.com/kata/5b1cd19fcd206af728000056

# f(x, n)  = x + 2x**2 + 3x**3 + .. + nx**n when n -> inf; so 
# very similar to some Tailor-Maclaurin series. task is find that function
# some math from 1/(1-x) = sum(i * x**i for i in range(0..inf )) 
# diff[1/(1-x)] = diff[ sum(i * x**i for i in range(0..inf )) ] ## diff both sides
# 1/((1-x)**2) = 0 + 1 + 2x + 3**x2 ...  - we need just multiply on x
# f(x) = x/((1-x)**2)

def solve(m):
    # solve for x:   m = x/((1-x)**2) on known m
    a = m
    b = -(1 + 2 * m)
    c = m
    d = b**2 - 4*a*c
    x1 = (-b+(d**0.5))/(2*a)
    x2 = (-b-(d**0.5))/(2*a)
    if 0 < x1 < 1:
        return x1
    elif 0 < x2 < 1:
        return x2
