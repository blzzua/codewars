# https://www.codewars.com/kata/58a3a735cebc0630830000c0

def string_constructing(a, s):
    res = 0
    start = list(a) 
    finish = list(s)
    while finish:
        res = res + len(start) + 1 
        for start_letter in start:
            if start_letter  == finish[0]:
                finish.pop(0)
                res = res - 1
                if finish == []:
                    break 
    return res
