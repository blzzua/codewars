# https://www.codewars.com/kata/55eea63119278d571d00006a

def next_id(arr):
    for i in range(0,len(arr)):
        if i not in arr:
            return i
    else:
        return len(arr)

