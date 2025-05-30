# https://www.codewars.com/kata/5b06c990908b7eea73000069

def f_orig(n, z):
    #(1 - z)(z + z**2 + z**3 + ... + z**n)
    return (1-z) * sum(z**i for i in range(1,n+1))

def f(z, eps):
    if abs(z) >=1:
        return -1
    res = 1
    nz = 0
    while abs(nz - z) > eps:
        nz = f_orig(res, z)
        #print(abs(nz - z))
        res += 1
    return res-1

# math solution (math.log(eps) / math.log(abs(z))
