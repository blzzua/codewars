# https://www.codewars.com/kata/551e51155ed5ab41450006e1

from itertools import product

def sum_times_tables(table,a,b):
    return sum(x*y for x,y in product(table, range(a,b+1)))
