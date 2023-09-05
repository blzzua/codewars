# https://www.codewars.com/kata/5a05fe8a06d5b6208e00010b

def seq_to_one(n):
    inc = 1 if n < 1 else -1
    return [i for i in range(n, 1 + inc, inc)]

