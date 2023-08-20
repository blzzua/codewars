# https://www.codewars.com/kata/56917304360b39073f00003b

import ast
def calc_pol(pol_str, x = None):
    print(pol_str, x)
    if x is None:
        return "There is no value for x"
    node = ast.parse(pol_str, mode='eval')
    code_object = compile(node, filename='<string>', mode='eval')
    result = eval(code_object)
    if result == 0:
        return f'Result = {result}, so {x} is a root of {pol_str}'
    return f'Result = {result}'
