# https://www.codewars.com/kata/5a3357ae8058425bde002674

import re

def rotate(n, arr, left=False):
    if not arr:
        return arr
    n = n % len(arr)
    if left:
        return arr[n:] + arr[:n]
    else:
        return arr[-n:] + arr[:-n]

def encode(n, string):
    for _ in range(n):
        sp_pos = [i for i, c in enumerate(string) if c == ' ']
        string = string.replace(' ', '')
        chars = rotate(n, list(string))

        for pos in sp_pos:
            if pos <= len(chars):
                chars.insert(pos, ' ')
            else:
                chars.append(' ')

        words = ''.join(chars).split(' ')
        rotated_words = [''.join(rotate(n, list(word))) for word in words]
        string =  ' '.join(rotated_words)
    return f"{n} {string}"

def decode(string):
    match = re.match(r'^(\d+)\s+', string)
    n = int(match.group(1))
    string = string[match.end():]

    for _ in range(n):
        words = string.split(' ')
        rotated_words = [''.join(rotate(n, list(word), True)) for word in words]
        string = ' '.join(rotated_words)

        sp_pos = [i for i, c in enumerate(string) if c == ' ']
        string = string.replace(' ', '')
        chars = rotate(n, list(string), True)

        for pos in sp_pos:
            if pos <= len(chars):
                chars.insert(pos, ' ')
            else:
                chars.append(' ')
        string = ''.join(chars)
    return string
