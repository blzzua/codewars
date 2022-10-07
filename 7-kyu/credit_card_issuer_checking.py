# https://www.codewars.com/kata/5701e43f86306a615c001868

import re
def get_issuer(number):
    s = str(number)
    if re.match(r'^(34|37)\d{13}$', s):
        return 'AMEX'
    elif re.match(r'^6011\d{12}$', s):
        return 'Discover'
    elif re.match(r'^(51|52|53|54|55)\d{14}$', s):
        return 'Mastercard'
    elif re.match(r'^4(\d{12}|\d{15})$', s):
        return 'VISA'
    else:
        return 'Unknown'

