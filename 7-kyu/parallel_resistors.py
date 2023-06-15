# https://www.codewars.com/kata/5723b111101f5f905f0000a5

def resistor_parallel(*args):
    return 1 / sum( 1 / x for x in args)
