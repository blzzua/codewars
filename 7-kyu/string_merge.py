# https://www.codewars.com/kata/597bb84522bc93b71e00007e

def string_merge(string1, string2, letter):
    i1 = string1.find(letter)
    i2 = string2.find(letter)
    return string1[:i1] + string2[i2:]


