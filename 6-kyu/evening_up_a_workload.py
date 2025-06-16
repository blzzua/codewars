# https://www.codewars.com/kata/56431c04ed1454a35d00003b

def split_workload(workload):
    if workload == []:
        return (None, None)
    s = sum(workload)
    min_diff = float('inf')
    min_diff_i = 0
    for i in range(len(workload)):
        cur_diff = abs(sum(workload[0:i]) - sum(workload[i:]))
        if cur_diff < min_diff:
            min_diff = cur_diff
            min_diff_i = i
    i  = min_diff_i
    diff = abs(sum(workload[0:i]) - sum(workload[i:]))
    return (i, diff)

