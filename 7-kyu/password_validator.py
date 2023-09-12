# https://www.codewars.com/kata/56a921fa8c5167d8e7000053

import string
def password(password):
    return all((len(password) >= 8,
                any(map(string.ascii_lowercase.count, password)),
                any(map(string.ascii_uppercase.count, password)),
                any(map(string.digits.count, password))))
