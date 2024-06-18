# https://www.codewars.com/kata/57f548337763f20e02000114/solutions/python

import re
import operator
condition_map = {'==': operator.eq, '<': operator.lt, '>': operator.gt, '<=': operator.le, '>=': operator.ge, '!=': operator.ne}

def string_evaluation(strng, conditions):
    res = []
    for cond in conditions:
        a, cond, b = re.split(r'([!<>=]=?)', cond)
        res.append(condition_map[cond](*map(lambda x: int(x) if x.isnumeric() else strng.count(x), (a,b))))
    return res


# same but not compact:
import re
def string_evaluation(strng, conditions):
    res = []
    for cond in conditions:
        a, cond, b = re.split(r'([!<>=]=?)', cond)
        ac = int(a) if a.isnumeric() else strng.count(a)
        bc = int(b) if b.isnumeric() else strng.count(b)
        match cond:
            case '==':
                res.append(ac == bc)
            case '<':
                res.append(ac < bc)
            case '>':
                res.append(ac > bc)
            case '<=':
                res.append(ac <= bc)
            case '>=':
                res.append(ac >= bc)
            case '!=':
                res.append(ac != bc)
    return res
