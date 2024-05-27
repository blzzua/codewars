# https://www.codewars.com/kata/54b80308488cb6cd31000161

def group_check(s):
    wait = []
    l = list(s)
    while l:
        char = l.pop(0)
        if char == '(':
            wait.append(')')
            continue
        elif char == '{':
            wait.append('}')
            continue
        elif char == '[':
            wait.append(']')
            continue
        elif wait and char == wait[-1]:
            wait.pop()
            continue
        if wait and l != wait[-1] and l in wait:
            return False
        if len(wait) == 0 and char in ')}]':
            return False
    if wait:
        return False
    else:
        return True

# see also https://www.codewars.com/kata/5277c8a221e209d3f6000b56
