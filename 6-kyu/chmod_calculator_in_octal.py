# https://www.codewars.com/kata/57f4ccf0ab9a91c3d5000054

def chmod_calculator(perm):
    res = ''
    for o in 'user', 'group', 'other':
        p = perm.get(o,'---')
        res += str(sum((2**i) * p.count(b) for i, b  in enumerate('xwr')))
    return res

