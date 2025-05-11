# https://www.codewars.com/kata/59aac10dd0a5ff951100002a
# not published translation yet

def find_index_of_sub_array(arr):
    res1 = []
    res2 = []
    sa = sorted(arr)
    for i,(x,y,z) in enumerate(zip(arr, sa, sa[::-1])):
        if x != y:
            res1.append(i)
        if x != z:
            res2.append(i)
    if res1 == [] or res2 == []:
        # already sorted
        return [0, 0]

    if len(res1) < len(res2):
        return [res1[0],res1[-1]]
    elif len(res1) > len(res2):
        return [res2[0],res2[-1]]
    else: 
        if res1[-1] <= res2[-1]:
            return [res1[0], res1[-1]]
        else:
            return [res2[0], res2[-1]]

