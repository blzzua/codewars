# https://www.codewars.com/kata/57ce0c634001a5f3c7000006

import re
def date_checker(date):
    return bool(re.match(r'\d{2}-\d{2}-\d{4} \d{2}:\d{2}', date))
