# https://www.codewars.com/kata/553e8b195b853c6db4000048

def has_unique_chars(string):
    return sorted(set(string)) == sorted(string)

