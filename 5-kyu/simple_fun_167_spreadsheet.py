# https://www.codewars.com/kata/58b38f24c723bf6b660000d8

import re
import string
alphabet = ' '+ string.ascii_uppercase # indexed from 1

def rowcol2alphabet(s):
    colstr, rowstr = re.findall(r'^([A-Z]+)(\d+)$',s)[0]
    colnum = sum([26**position * charnum  for position, charnum in enumerate(list(map(alphabet.index, colstr))[::-1])])
    return f'R{rowstr}C{colnum}'

def alphabet2rowcol(s):
    row, col = re.findall('^R(\d+)C(\d+)$', s)[0]
    colarr = []
    colnum = int(col)
    while colnum > 0:
        colnum, d = divmod(colnum, 26)
        if d == 0:
            colnum = colnum - 1
            d = d + 26
        colarr.append(alphabet[d])
    colstr = ''.join(colarr[::-1])
    return f'{colstr}{row}'

def spreadsheet(s):
    if re.match('^[A-Z]+\d+$', s):
        return rowcol2alphabet(s)
    else:
        return alphabet2rowcol(s)
    

