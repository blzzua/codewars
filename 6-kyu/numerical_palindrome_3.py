# https://www.codewars.com/kata/58df62fe95923f7a7f0000cc

def palindrome(num):
    if not (type(num) == int and num >= 0):
        return 'Not valid'
    s = str(num)
    res = 0
    for i in range(2, len(s) + 1):
        for j in range(len(s) - i + 1):
            c = s[j:j+i]
            if c == c[::-1]:
                res += 1
    return res

