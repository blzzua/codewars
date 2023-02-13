# https://www.codewars.com/kata/5a34f087c5e28462d9000082

def swap_head_tail(arr):
    half = len(arr) // 2 
    return arr[-half:] + arr[half:-half] + arr[:half]
