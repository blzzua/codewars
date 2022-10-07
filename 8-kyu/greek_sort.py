# https://www.codewars.com/kata/56bc1acf66a2abc891000561

def greek_comparator(lhs, rhs):
    n = greek_alphabet.index(lhs) - greek_alphabet.index(rhs)
    if n:
        return n // abs(n)
    else:
        return n

