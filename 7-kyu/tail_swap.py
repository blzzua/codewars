# https://www.codewars.com/kata/5868812b15f0057e05000001
def tail_swap(strings):
    t = [s.split(':') for s in strings]
    return [':'.join((a[0],b[1]))  for a,b in zip(t, t[::-1])]
  
