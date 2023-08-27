import re
def case_id(c_str):
    print(c_str)
    if re.match(r'^[a-z]+([A-Z]+[a-z]+)+$', c_str):
        return 'camel'
    if re.match(r'^[a-z]+(-([a-z]+))+$', c_str):
        return 'kebab'
    if re.match(r'^[a-z]+(_([a-z]+))+$', c_str):
        return 'snake'
    return 'none'
