# https://www.codewars.com/kata/5945f0c207693bc53100006b

from collections import Counter
def count_contiguous_distinct(k, arr):
    res = []
    test = Counter(arr[0:k])
    res.append(len(test))
    for i in range(len(arr) - k):
        if arr[i] != arr[i+k]:
            test.update({arr[i]: -1, arr[i+k]:1})
            if test[arr[i]] == 0:
                del test[arr[i]]
        res.append(len(test))
    return res
