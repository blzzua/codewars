# https://www.codewars.com/kata/541a354c39c5efa5fa001372

from ipaddress import ip_address 

def ip_to_num(ip):
    return int(ip_address(ip))

def num_to_ip(num):
    return str(ip_address(num))
