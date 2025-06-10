# https://www.codewars.com/kata/59dbab4d7997cb350000007f
# Check if two words are isomorphic to each other


def tokenize(a):
    a_dict = dict()
    res = []
    for c in a:
        if c in a_dict:
            res.append(a_dict[c])
        else:
            res.append(num_val:=max(a_dict.values(), default=0) + 1)
            a_dict[c] = num_val
    return res

def isomorph(a, b):
    return tokenize(a) == tokenize(b)
