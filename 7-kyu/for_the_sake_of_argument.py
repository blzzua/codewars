# https://www.codewars.com/kata/5258b272e6925db09900386a

def numbers(*args):
    return all(type(i) in (int, float)  for i in args)

