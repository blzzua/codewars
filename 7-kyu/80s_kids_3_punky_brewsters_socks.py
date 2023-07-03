# https://www.codewars.com/kata/5662292ee7e2da24e900012f

def get_socks(name, socks):
    if name == 'Henry':
        for s in socks:
            if socks.count(s) > 1:
                return [s] * 2 
        return []
    elif name == 'Punky':
        for s1, s2 in zip(socks,socks[1:]):
            if s1 != s2:
                return [s1, s2]
        return []
