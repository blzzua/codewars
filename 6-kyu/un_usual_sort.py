# https://www.codewars.com/kata/5443b8857fc4473cb90008e4

from string import ascii_uppercase, ascii_lowercase, digits

def unusual_sort(array):
    sortlist = list(ascii_uppercase + ascii_lowercase)
    for a,b in zip(range(10), digits):
        sortlist.extend((a,b))
    return sorted(array, key=sortlist.index)
