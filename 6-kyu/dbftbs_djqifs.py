# https://www.codewars.com/kata/546937989c0b6ab3c5000183

import string
def encryptor(key, message):
    key = (key + 26) % 26
    tr_map_lower = str.maketrans(string.ascii_lowercase, (string.ascii_lowercase + string.ascii_lowercase)[key:key+26])
    tr_map_upper = str.maketrans(string.ascii_uppercase, (string.ascii_uppercase + string.ascii_uppercase)[key:key+26])
    return message.translate(tr_map_upper).translate(tr_map_lower)
