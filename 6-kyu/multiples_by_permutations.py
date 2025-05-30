# https://www.codewars.com/kata/55f1a53d9c77b0ed4100004e

def search_perm_mult(n_max, k):
    res = 0
    for i in range(1, n_max // k +1):
        if sorted(str(i*k)) == sorted(str(i)):
            print(i,i*k)
            res += 1
    return res

