# https://www.codewars.com/kata/5c511d8877c0070e2c195faf

def validate(username, password):
    short, long = sorted((username, password), key=len)
    n = (len(short)+1)//2
    ln = len(long) - n + 1
    is_subs = [long[i:n+i] in short for i in range(ln)]
    return not any(is_subs)
