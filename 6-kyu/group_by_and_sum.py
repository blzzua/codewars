# https://www.codewars.com/kata/5ed056c9263d2f001738b791

def group_key(line, idx):
    return tuple(line[ind] for ind in idx)
def group_values(line, idx):
    return [value for ind, value in enumerate(line) if ind not in idx]

def group(arr, idx):
    res = {}
    for line in arr:
        key = group_key(line, idx)
        values = group_values(line, idx)
        if key not in res:
            res[key] = values
        else:
            res[key] = [a+b for a,b in zip(res[key], values)]
    return res
  
