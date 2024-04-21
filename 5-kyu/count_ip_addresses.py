# https://www.codewars.com/kata/526989a41034285187000de4

import ipaddress
def ips_between(start, end):
    return int(ipaddress.IPv4Address(end)) - int(ipaddress.IPv4Address(start))

# singleline
def ips_between(start, end):
    return sum([(b-a)*256**(3-i) for i, (a,b) in enumerate(zip(map(int,start.split('.')), map(int,end.split('.'))) )])
