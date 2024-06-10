# https://www.codewars.com/kata/58afa8185eb02ea2a7000094

def pairwise(arr, n):
    added_indices = set()
    res = 0
    for i, val1 in enumerate(arr):
        for j, val2 in enumerate(arr[i+1:], i+1):
            if val1 + val2 == n:
                if i not in added_indices and j not in added_indices:
                    added_indices.add(i)
                    added_indices.add(j)
                    res += (i+j)
    return res
