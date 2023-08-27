#  https://www.codewars.com/kata/64c7bbad0a2a00198657013d

def rev_sub(arr):
    rev_sub_arr = []
    res = []
    for i in arr:
        if i % 2 == 1:
            if rev_sub_arr != []:
                res.extend(rev_sub_arr[::-1])
                rev_sub_arr = []
            res.append(i)
        else: # if i % 2 == 0:
            rev_sub_arr.append(i)
    res.extend(rev_sub_arr[::-1])
    return res
