# https://www.codewars.com/kata/58b8c94b7df3f116eb00005b

def reverse_letter(string):
    return ''.join(a for a in string[::-1] if a.isalpha())

