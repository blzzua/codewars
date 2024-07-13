# https://www.codewars.com/kata/5936371109ca68fe6900000c

# library solution:
from ipaddress import ip_address 
def number_and_IP_address(s):
    if '.' in s:
        return str(int(ip_address(s)))
    else:
        return str(ip_address(int(s)))


# algo solution:
def number_and_IP_address(s):
    if '.' in s:
        res = sum(256**p * int(i) for p, i in enumerate(s.split(".")[::-1]))
        return str(res)
    else:
        n = int(s)
        res = []
        for p in range(4):
            n, digit = divmod(n, 256)
            res.append(digit)
        return '.'.join(map(str,res[::-1]))
