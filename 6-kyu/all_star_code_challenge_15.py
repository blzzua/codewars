# https://www.codewars.com/kata/586560a639c5ab3a260000f3

def rotate(str_):
    l = len(str_)
    s = str_ + str_
    return [ (s[i:]+s[:i])[:l] for i in range(1, l+1)]
