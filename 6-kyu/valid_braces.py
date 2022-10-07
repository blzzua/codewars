# https://www.codewars.com/kata/5277c8a221e209d3f6000b56

def valid_braces(string):
    bc = {"(": ")", "[": "]", "{": "}"}
    stack = []
    for c in string:
        if c in bc:
            stack.append(c)
        else:
            if len(stack) == 0 or bc[stack.pop()] != c:
                return False
    return not bool(stack)


