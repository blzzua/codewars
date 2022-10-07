# https://www.codewars.com/kata/58ba6fece3614ba7c200017f

def palindrome(num):
    if type(num) == int and num >= 0:
        return num == int(str(num)[::-1])
    else:
        return 'Not valid'

