# https://www.codewars.com/kata/541629460b198da04e000bb9

def last(*args):
    if len(args) > 1:
        return args[-1]
    if hasattr(args[0], '__iter__'):
        return args[0][-1]
    return args[0]
  
