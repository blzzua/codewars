# https://www.codewars.com/kata/59be8c08bf10a49a240000b1

import re
# reuse functions from prev katas
def to_camel(identifier):
    words = re.findall(r'([A-Za-z]+)',identifier)
    res = [words.pop(0)]
    res += list(map(str.capitalize, words))
    return ''.join(res)

def to_kebab(identifier):
    words = re.sub('\d','', identifier)
    return '-'.join(map(str.lower, re.findall(r'([A-Z]?(?:[a-z]+)|[A-Z])', words)))

def camel_to_snake(identifier):
    words = re.findall(r'[A-Z][a-z0-9]*|[a-z0-9]+', identifier)
    return "_".join(map(str.lower,words))

def kebab_to_snake(identifier):
    return identifier.replace('-', '_')

def change_case(identifier, target_case):
    if target_case not in ('camel','kebab', 'snake'):
        return None
    if identifier == '':
        return identifier
    
    source_case = 'none'
    if re.match(r'^[a-z]+([A-Z]+[a-z]+)+$', identifier):
        source_case = 'camel'
    if re.match(r'^[a-z]+(-([a-z]+))+$', identifier):
        source_case = 'kebab'
    if re.match(r'^[a-z]+(_([a-z]+))+$', identifier):
        source_case = 'snake'
    print('debug ', f'{source_case=} {identifier}', )
    if source_case == 'none':
        return None

    match (source_case, target_case):
        case (src, tgt) if src == tgt:
            return identifier
        case (_, 'camel'):
            return to_camel(identifier)
        case (_, 'kebab'):
            return to_kebab(identifier)
        case ('camel', 'snake'):
            return camel_to_snake(identifier)
        case ('kebab', 'snake'):
            return kebab_to_snake(identifier)
        case _: # debug wtf branch
            return ':'.join([identifier, 'from', source_case, 'to', target_case])
