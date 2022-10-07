# https://www.codewars.com/kata/5a005f4fba2a14897f000086

def int2b(arg):
    return int(*arg)
def sum_it_up(numbers_with_bases):
    return sum(map(int2b,numbers_with_bases))

