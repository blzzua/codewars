# https://www.codewars.com/kata/556d120c7c58dacb9100008b

# Write a function that takes two string parameters, an IP (v4) address and
# a subnet mask, and returns two strings: the network block,
# and the host identifier.

# For example:
# >>> print ipv4__parser('192.168.50.1', '255.255.255.0')
# ('192.168.50.0', '0.0.0.1')

def ipv4__parser(ip_addr, mask):
    ip_digits = list(map(int, ip_addr.split('.')))
    mask_digits = list(map(int, mask.split('.')))
    net_digits = [i & m for i, m in zip(ip_digits, mask_digits)]
    host_digits = [i & ~n for i, n in zip(ip_digits, net_digits)]

    net_addr = '.'.join(map(str, net_digits))
    host_addr = '.'.join(map(str, host_digits))
    return (net_addr, host_addr)


