# https://www.codewars.com/kata/643a47fadad36407bf3e97ea

def encode_cd(n):
    bitmask = f'{n:b}'.zfill(8)[::-1]
    res = 'P'
    prev = res
    for x in bitmask:
        if x == '0':
            res+=prev
        else:
            if prev == 'P':
                res+='L' 
            else:
                res+='P'
        prev = res[-1]
    return res
