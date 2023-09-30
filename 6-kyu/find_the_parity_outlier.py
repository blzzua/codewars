# https://www.codewars.com/kata/5526fc09a1bbd946250002dc

def find_outlier(a):
    even = odd = se = so = ss = 0
    for i in a:
        if i % 2 == 1:
            odd, so, ss = odd + 1, so + i, ss + i
        else:
            even, se, ss = even + 1, se + i, ss + i

    return [se, so][even > odd]
