# https://www.codewars.com/kata/54f9c37106098647f400080a

def drop_while(arr, pred):
    for i, v in enumerate(arr):
        if pred(v):
            continue
        else:
            return arr[i:]
    else:
        return []

