# https://www.codewars.com/kata/580a4001d6df740d61000301

def complete_series(seq): 
    if len(seq) != len(set(seq)):
        return [0]
    else:
        return [*(range(0, -~max(seq)))]


