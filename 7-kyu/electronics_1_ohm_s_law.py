# https://www.codewars.com/kata/614dfc4ce78d31004a9c1276

def ohms_law(s):
    input = { val[-1]: float(val[:-1])  for val in s.split(' ')}
    if 'V' not in input:
        return str(round(input['A']*input['R'],6)) + 'V'
    elif 'R' not in input:
        return str(round(input['V']/input['A'],6)) + 'R'
    elif 'A' not in input:
        return str(round(input['V']/input['R'],6)) + 'A'

