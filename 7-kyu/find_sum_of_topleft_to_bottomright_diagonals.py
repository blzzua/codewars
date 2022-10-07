# https://www.codewars.com/kata/5497a3c181dd7291ce000700

def diagonal_sum(a):
    return sum(a[i][i] for i in range(len(a)))


