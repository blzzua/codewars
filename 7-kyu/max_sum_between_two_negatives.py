# https://www.codewars.com/kata/6066ae080168ff0032c4107a

def max_sum_between_two_negatives(arr):
    narr = [i for i,j in enumerate(arr) if j<0]
    if len(narr) <= 1:
        return -1
    else:
        return max(sum(arr[narr[i-1]:narr[i]+1])-arr[narr[i-1]]-arr[narr[i]] for i in range(1, len(narr)))

