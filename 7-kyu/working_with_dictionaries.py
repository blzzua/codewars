# https://www.codewars.com/kata/5639302a802494696d000077

import operator

def inf_database(range_, str_, val):
    global A001055     # global it's not necessary but to remember you the name of the database
    comparator = { 'higher than' : operator.gt, 'higher and equals to': operator.ge, 'equals to': operator.eq, 'lower than': operator.lt, 'lower and equals to' : operator.le}
    if str_ in comparator:
        ret = [i for i in range(range_[0], range_[1]+1) if comparator[str_](A001055[i],val)]
        return (len(ret), ret)
    else:
        return 'wrong constraint'

