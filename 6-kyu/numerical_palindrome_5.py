# https://www.codewars.com/kata/58e26b5d92d04c7a4f00020a

# if number is palindrome, then Counter(str(num)) can consist only 1 odd count of numbers in center.
# other numbers-counts must be doubled and even

from collections import Counter
def palindrome(num):
    if not (type(num) == int and num >= 0):
        return 'Not valid'
    c = Counter(str(num))
    return sum(1 for k,v in c.items() if v % 2) <= 1 and num > 10 
    
