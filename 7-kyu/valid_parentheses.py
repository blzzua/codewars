# https://www.codewars.com/kata/6411b91a5e71b915d237332d

def valid_parentheses(paren_str):
    s = paren_str[:]
    while True:
        ns = s.replace('()','')
        if ns == '':
            return True
        elif ns == s:
            return False
        s = ns
