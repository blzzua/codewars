# https://www.codewars.com/kata/52ea928a1ef5cfec800003ee

def ip_to_int32(ip):
    return sum([a*256**(3-i) for i, a in enumerate(map(int,ip.split('.')))])
