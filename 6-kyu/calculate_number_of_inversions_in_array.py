# https://www.codewars.com/kata/537529f42993de0e0b00181f
# actually count swap operations for bubble-sort

def count_inversions(array):
    res = 0
    for i, must_bigger in enumerate(array):
        for must_smaller in array[:i]:
             if must_smaller > must_bigger:
                res += 1
    return res

