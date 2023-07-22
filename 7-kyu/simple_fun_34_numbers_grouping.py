# https://www.codewars.com/kata/588711735ea0b4649e000001

def numbers_grouping(a):
    res_dict = {}
    for i in a:
        mod = (i-1)//10000+1
        if mod not in res_dict:
            res_dict[mod] = 1
        else:
            res_dict[mod] += 1
    print(res_dict)
    num_lines = sum(res_dict.values())+ len(res_dict.keys())
    return num_lines
