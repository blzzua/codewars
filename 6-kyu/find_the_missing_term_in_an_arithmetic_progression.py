# https://www.codewars.com/kata/52de553ebb55d1fca3000371

def find_missing(seq):
    return (len(seq) + 1) * (seq[-1] + seq[0]) / 2 - sum(seq)
