# https://www.codewars.com/kata/568dc69683322417eb00002c

def triple_x(s):
    try:
        i = s.find('x')
        return i >= 0 and s[i] == s[i+1] == s[i+2]
    except IndexError:
        return False


