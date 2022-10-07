# https://www.codewars.com/kata/56853c44b295170b73000007

def is_square(arr):
    if arr:
        return all(int(a**0.5)**2 == a for a in arr)

