# https://www.codewars.com/kata/563f037412e5ada593000114

def calculate_years(principal, interest, tax, desired):
    y = 0
    while principal < desired:
        principal += (principal * interest) * (1-tax)
        y += 1
    return y

