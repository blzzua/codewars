# https://www.codewars.com/kata/604517d65b464d000d51381f

def strange_math(n, k):
    return sorted(list(map(str,range(-~n)))).index(str(k))

