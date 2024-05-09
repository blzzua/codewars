# https://www.codewars.com/kata/590c4c342ad5cd6a8700005c

def prefix_sums_to_suffix_sums(prefix_sums):
    arr = [prefix_sums[0]] + [y - x for x, y in zip(prefix_sums, prefix_sums[1:])]
    res = [sum(arr)]
    for x in arr[:-1]:
        res.append(res[-1] - x)
    return res

