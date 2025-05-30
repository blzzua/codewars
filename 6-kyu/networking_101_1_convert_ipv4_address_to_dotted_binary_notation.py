# https://www.codewars.com/kata/6288de23ab7ede0031602521

def ipv4_to_binary(ipv4_addr: str) -> str:
    res = []
    for octet in ipv4_addr.split('.'):
        digit = int(octet)
        bin_oct = (bin(digit)[2:]).zfill(8)
        res.append(bin_oct)
    return '.'.join(res)

