# https://www.codewars.com/kata/5704aea738428f4d30000914

def triple_trouble(*args):
    return ''.join([''.join(v) for v in zip(*args)])

