# https://www.codewars.com/kata/5cb99d1a1e00460024827738

def f1(n, k):
    i = n
    while True:
        if all((int(c) < k for c in str(i))):
            return i
        i = i + n


def f2(n, k):
    i = n
    while True:
        if set(str(i)) == set((str(d) for d in range(k))):
            return i
        i = i + n
        
def find_f1_eq_f2(n,k):
    i = n + 1
    while f1(i, k) != f2(i, k):
        i += 1
    return i

