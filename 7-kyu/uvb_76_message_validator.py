# https://www.codewars.com/kata/56445cc2e5747d513c000033

import re
def validate(message):
    print(message)
    return bool(re.fullmatch(r'MDZHB(?: \d{2}){2}\d [A-Z]+(?: \d\d){4}', message))
