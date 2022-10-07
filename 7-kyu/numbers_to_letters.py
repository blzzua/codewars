# https://www.codewars.com/kata/57ebaa8f7b45ef590c00000c

from string import ascii_lowercase 
def switcher(arr):
    alphabet = ['zero placeholder'] + list(reversed(ascii_lowercase))+['!','?',' ']
    return ''.join(alphabet[int(c)] for c in arr)
                           
                           


