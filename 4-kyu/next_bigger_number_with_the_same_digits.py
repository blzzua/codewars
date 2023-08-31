# https://www.codewars.com/kata/55983863da40caa2c900004e

def next_bigger(n):
    # some workarounds for edge cases:
    if n < 10:
        return -1
    l = tuple(str(n))
    if len(l) < 3:
        print('len < 3 case')
        res = int(''.join(reversed(l)))
        if res == n or res < n:
            return -1
        else:
            return res
    if list(l) == list(sorted(l, reverse=True)):
        print('sorted case')
        return -1

    # partitioning number
    for pc in range(2, len(l)+1):
        if l[-pc:] == tuple(sorted(l[-pc:], reverse=True)):
            print('continue: ', pc ,l[-pc:])
            continue
        else:
            print('permutate: ', pc ,l[-pc:])
            break
    p1, p2 = list(l[:-pc]), list(l[-pc:])

    f0 = p1[:]                     # first, untouched part of n
                                   # p2 - variable part
    # p2[0] max digit in variable part.
    # find second digit in variable part f1_value:
    f1_value = next(filter(lambda x: x > p2[0], sorted(p2[1:])))  
    f1_index = p2.index(f1_value)                                     
    f1 = [p2.pop(f1_index)]   # remove second digit from variable part
    f2 = sorted(p2)
    return int(''.join(f0 + f1 + f2))
  
