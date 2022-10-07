# https://www.codewars.com/kata/5e07b5c55654a900230f0229

def reverse_in_parentheses(string):
    res = ''
    stack = []
    for c in string:
        stack.append(c)
        if c == ')':
            cursor = len(stack) - stack[::-1].index('(') - 1
            reversed_internal = ''.join([i[::-1].translate(str.maketrans('()',')(')) for i in stack[cursor:][::-1]])
            stack.append(reversed_internal)
            del stack[cursor:-1]
    res = ''.join(stack)
    return res


