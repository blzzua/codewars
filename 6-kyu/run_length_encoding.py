# https://www.codewars.com/kata/546dba39fa8da224e8000467

def run_length_encoding(s):
    res = []
    for ch in s:
        if not res:
            res.append([1, ch])
        else:
            if res[-1][1] == ch:
                res[-1][0] += 1
            else:
                res.append([1, ch])
    return res
