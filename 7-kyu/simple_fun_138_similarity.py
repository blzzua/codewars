# https://www.codewars.com/kata/58a6841442fd72aeb4000080

def similarity(a, b):
    return len(set(a).intersection(set(b))) / len(set(a+b))
