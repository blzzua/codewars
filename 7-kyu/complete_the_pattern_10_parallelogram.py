# https://www.codewars.com/kata/5581a7651185fe13190000ee

def pattern(n):
    step = ''.join([str(i%10) for i in range(1,n+1)])
    return '\n'.join([' '*(n-i) +step + ' '*(i-1)  for i in range(1,n+1)])

