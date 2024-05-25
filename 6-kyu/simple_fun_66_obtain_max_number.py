# https://www.codewars.com/kata/5893f03c779ce5faab0000f6

from collections import Counter
def obtain_max_number(lst):
    while True:
        doubles = [k for k,v in Counter(lst).items() if v >= 2]
        if doubles:
            for k in doubles:
                a = lst.pop(lst.index(k))
                b = lst.pop(lst.index(k))
                lst.append(a+b)
        else:
            break
    return max(lst)
