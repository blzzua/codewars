# https://www.codewars.com/kata/590148d79097384be600001e

def sort_by_guide(arr, guide):
    sorted_pairs = sorted([(a,b) for a,b in zip(guide, arr) if a != -1])
    res = []
    for i, val in enumerate(arr):
        if guide[i] == -1:
            res.append(val)
        else:
            res.append(sorted_pairs.pop(0)[1])
    return res
  
