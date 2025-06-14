# https://www.codewars.com/kata/59f44c7bd4b36946fd000052

def hist(s):
    res = []
    for c in ['u','w','x','z']:
        sc = s.count(c)
        if sc > 0:
            sc_jsf = str(sc).ljust(6)
            sc_hst = '*' * s.count(c)
            res.append(f"{c}  {sc_jsf}{sc_hst}")
    return '\r'.join(res)

