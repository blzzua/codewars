# https://www.codewars.com/kata/59590976838112bfea0000fa


def beggars(values, n):
    if n == 0:
        return []
    l = len(values)
    values = values + [0] *(n - l % n)
    return [sum(values[i::n]) for i in range(n)]
    
