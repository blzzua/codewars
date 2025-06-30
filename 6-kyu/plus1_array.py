# https://www.codewars.com/kata/5514e5b77e6b2f38e0000ca9
def up_array(arr):
    if arr == []:
        return None
    for digit in arr:
        if not (0 <= digit <=9):
            return None
    n = int(''.join(map(str,arr)))
    n += 1
    res = list(map(int, str(n)))
    if len(res) < len(arr):
        res = [0] * (len(arr) - len(res))  + res
    return res
  
