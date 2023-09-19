# https://www.codewars.com/kata/573b216f5328ffcd710013b3

LWM = {'M': 1.5, 'F': 1.2}
def lose_weight(gender, weight, duration):
    if gender not in 'MF':
        return 'Invalid gender'
    if weight <= 0:
        return 'Invalid weight'
    if duration <= 0:
        return 'Invalid duration'
    coef = round(1/(1+LWM[gender]/100),3)
    return round(weight * (coef ** duration),1)
