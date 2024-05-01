# https://www.codewars.com/kata/54c2fc0552791928c9000517

def f(n, m):
    return (m*(m-1)//2)*(n//m) + (1 + n%m) * (n%m) // 2
    # re, c = divmod(n,m) ; m*(m-1)//2*re + (1+c)*c/2    
