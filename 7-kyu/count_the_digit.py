# https://www.codewars.com/kata/566fc12495810954b1000030

def nb_dig(n, d):
    return ''.join(str(a ** 2) for a in range(n + 1)).count(str(d))

