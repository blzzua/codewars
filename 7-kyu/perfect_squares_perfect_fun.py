# https://www.codewars.com/kata/5705ca6a41e5be67720012c0

def square_it(d):
    s = str(d)
    root = len(s) ** 0.5
    if root == int(root) :
        root = int(root)
        return '\n'.join((s[i * root:i * root + root] for i in range(int(root))))
    return 'Not a perfect square!'

