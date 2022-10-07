# https://www.codewars.com/kata/60a94f1443f8730025d1744b

from string import ascii_lowercase
def grid(N):
    print(N)
    if N > 0:
        return '\n'.join(' '.join(ascii_lowercase[(i + j) % 26] for j in range(N)) for i in range(N))
    elif N == 0:
        return ''


