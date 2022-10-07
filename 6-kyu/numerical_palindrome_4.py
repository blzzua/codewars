# https://www.codewars.com/kata/58df8b4d010a9456140000c7

def is_palindrome(num):
    return str(num)[::-1] == str(num)

def palindrome(num):
    if not (type(num) == int and num >= 0):
        return 'Not valid'
    if num <= 16:
        return 11
    if is_palindrome(num):
        return num
    for step in range(num):
        if is_palindrome(num+step):
            return num+step
        if is_palindrome(num-step):
            return num-step


