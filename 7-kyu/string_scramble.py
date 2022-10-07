# https://www.codewars.com/kata/5822d89270ca28c85c0000f3

def scramble(string, array):
    return ''.join(c[0] for c in sorted(zip(string, array), key=lambda i: i[1]))

