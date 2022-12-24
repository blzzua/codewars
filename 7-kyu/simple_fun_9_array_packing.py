# https://www.codewars.com/kata/588453ea56daa4af920000ca

def array_packing(arr):
    return int(''.join([f'{i:08b}' for i in arr[::-1]]),2)
