# https://www.codewars.com/kata/58de77a2c19f096a5a00013f

def find_added(st1, st2):
    l1, l2  = list(st1), list(st2)
    for i in l1:
        if i in l2:
            l2.remove(i)
    return ''.join(sorted(l2))

# actual is Counter diff
# return ''.join(sorted((Counter(st2) - Counter(st1)).elements()))
