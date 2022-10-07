# https://www.codewars.com/kata/58de819eb76cf778fe00005c

def palindrome(num):
    if not (type(num) == int and num >= 0):
        return 'Not valid'
    s = str(num)
    for i in range(2, len(s) + 1):
        for j in range(len(s) - i + 1):
            c = s[j:j+i]
            if c == c[::-1]:
                return True
    return False

