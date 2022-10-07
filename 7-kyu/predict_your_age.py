# https://www.codewars.com/kata/5aff237c578a14752d0035ae

def predict_age(*ages):
    return int(sum(age**2 for age in ages)**0.5/2)

