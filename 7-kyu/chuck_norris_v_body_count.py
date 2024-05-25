# https://www.codewars.com/kata/57066ad6cb72934c8400149e

import re
def body_count(code):
    return bool(re.search(r'([A-Z]\d){5}\.-[A-Z]%\d\.\d{2}\.', code))

