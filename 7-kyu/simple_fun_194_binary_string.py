# https://www.codewars.com/kata/58c218efd8d3cad11c0000ef

def bin_str(s):
    ss = '0' * len(s)
    index = s.find('1')
    for i in range(len(s) * 2):
        if ss == s:
            return i
        s = s[:index] + s[index:].translate(str.maketrans({'0': '1', '1': '0'}))
        index = s.find('1')
    return 0
