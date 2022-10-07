# https://www.codewars.com/kata/56f253dd75e340ff670002ac

def compose(s1, s2):
    s1 = s1.split('\n')
    s2 = s2.split('\n')[::-1]
    t = [a + b for a, b in zip(s1,s2)]
    return '\n'.join([c[:i+1] + c[len(t):len(c)- i] for i, c in enumerate(t)])

