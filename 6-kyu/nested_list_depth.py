# https://www.codewars.com/kata/56b3b9c7a6df24cf8c00000e

def list_depth(l):
    if type(l) != list:
        return 0
    res = 1
    for item in l:
        if type(item) == list:
            res = max(res, list_depth(item) + 1)
    return res     


# funny method based on repr(nested_list):
def list_depth(l):
    cur_cnt, max_cnt = 0, 0
    for char in str(l):
        if char == '[': 
            cur_cnt += 1
        elif char == ']': 
            cur_cnt -= 1
        else: 
            continue
        max_cnt = max(cur_cnt, max_cnt)
    return max_count
