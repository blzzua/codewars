# https://www.codewars.com/kata/59b06d83cf33953dbb000010

def is_centered(arr,n):
    if (n == 0 and len(arr) % 2 == 0): return True # wierd zero-len cetral subseq workaround
    if sum(arr) == n: return True  # wierd zero-len edge subseq workaround

    while len(arr) > 1:
        arr.pop(0), arr.pop()
        if sum(arr) == n:
            return True
    return False
