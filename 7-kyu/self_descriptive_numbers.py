# https://www.codewars.com/kata/56a628758f8d06b59800000f 

def self_descriptive(num):
    return all(int(s) == list(str(num)).count(str(i)) for i, s in enumerate(str(num)))
