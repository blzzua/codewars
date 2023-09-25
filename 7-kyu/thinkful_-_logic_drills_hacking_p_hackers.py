# https://www.codewars.com/kata/5864af6739c5ab26e80000bf

def categorize_study(p_value, requirements):
    product = p_value * (2 ** (6-requirements))
    if product < 0.05 and requirements > 0:
        return 'Fine'
    elif product < 0.05 and requirements == 0:
        return 'Needs review'
    elif product >= 0.15:
        return 'Pants on fire'
    else:
        return 'Needs review'
