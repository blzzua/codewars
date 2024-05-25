# https://www.codewars.com/kata/58e09234ca6895c7b300008c

def palindrome(num, s):
    if not(isinstance(num, int) and isinstance(s, int)):
        return 'Not valid'
    if not(num > 0 and s >= 0):
        return 'Not valid'
    if num < 10: num = 11
    res = []
    while len(res) < s:
        if str(num) == str(num)[::-1]:
            res.append(num)
        num+=1
    return res
