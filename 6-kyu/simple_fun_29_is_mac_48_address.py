# https://www.codewars.com/kata/5886faac54a7111c21000072

def is_mac_48_address(address):
    if len(address) != len('00-00-00-00-00-00'):
        return False
    if any(address[i] != '-' for i in [2,5,8,11,14]) or address.count('-') != 5:
        return False 
    return set(address).issubset(set('0123456789ABCDEF-'))

