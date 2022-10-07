# https://www.codewars.com/kata/54eea36b7f914221eb000e2f

def sort_it(list_, n):
    return ', '.join(sorted(list_.split(', '), key=lambda w: w[n-1]))

