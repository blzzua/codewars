# https://www.codewars.com/kata/59e1b9ce7997cbecb9000014

from math import prod
def cog_RPM(cogs):
    return  prod(-c1/c2 for c1, c2 in zip(cogs,cogs[1:]))
