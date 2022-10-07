# https://www.codewars.com/kata/57e2dd0bec7d247e5600013a

def unflatten(flat_array):
    inp=flat_array[:] 
    res = []
    while inp:
        i = inp.pop(0)
        if i < 3:
            res.append(i)
        else:
            subarray = [i]
            for _ in range(i-1):
                try:
                    subarray.append(inp.pop(0))
                except IndexError:
                    pass
            res.append(subarray)
    return res


