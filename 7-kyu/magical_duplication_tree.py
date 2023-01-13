# https://www.codewars.com/kata/6339de328a3b8f0016cc5b8d

def magic_plant(p_field,split,n):
    h0 = p_field.count('|')
    h1 = (h0 - n)
    w = split**n
    heads = 'o' * w
    if h1:
        downs = '\n' + '\n'.join('|' * w for _ in range(h1))
        return heads + downs
    return heads
