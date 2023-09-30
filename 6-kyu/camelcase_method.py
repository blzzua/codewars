# https://www.codewars.com/kata/587731fda577b3d1b0001196

def camel_case(s):
    return ''.join(map(str.capitalize,s.strip().split()))
  
