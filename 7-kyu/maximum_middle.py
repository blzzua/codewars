# https://www.codewars.com/kata/60e238105b0327001434dfd8

def maximum_median(arr, min_length):
    return max(arr[i:i+min_length][min_length//2] for i in range(len(arr)-min_length+1))

