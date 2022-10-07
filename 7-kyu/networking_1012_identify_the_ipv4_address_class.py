# https://www.codewars.com/kata/628ba76a85a2d500649da696

def ipv4_address_class(ipv4_addr):
    n = int(ipv4_addr.split(".")[0])
    return ['E','D','C','B','A'][(n<128) + (n<192) + (n<224) + (n<240)]


