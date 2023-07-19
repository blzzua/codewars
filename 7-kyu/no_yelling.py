# https://www.codewars.com/kata/587a75dbcaf9670c32000292

import re
def filter_words(st):
    return re.sub('\s+',' ', st.capitalize()).strip()
