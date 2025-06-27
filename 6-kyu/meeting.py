# https://www.codewars.com/kata/59df2f8f08c6cec835000012

def meeting(s):
    names = []
    for name in s.split(';'):
        fn, ln = name.split(':') 
        names.append((ln.upper(), fn.upper()))
    return ''.join([f'({fn}, {ln})' for fn, ln in sorted(names)])
  
