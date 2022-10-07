# https://www.codewars.com/kata/57d1f36705c186d018000813

def gordon(a):
    a = a.upper()
    for vowel in "EIOU":
        a = a.replace(vowel,"*")
    return a.replace("A","@").replace(" ","!!!! ")+"!!!!"

