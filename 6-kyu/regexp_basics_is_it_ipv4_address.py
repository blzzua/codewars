# https://www.codewars.com/kata/567fe8b50c201947bc000056

import re
def ipv4_address(address):
    if address.strip() != address: # \n workaround
        return False
    return bool(re.match(r'^((25[0-5]|(2[0-4]|1\d|[1-9]|)\d)\.?\b){4}$', address))
