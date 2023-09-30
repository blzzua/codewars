# https://www.codewars.com/kata/5679aa472b8f57fb8c000047

def find_even_index(arr):
    for i in range(len(arr)):
        l = sum(arr[:i])
        r = sum(arr[i+1:])
        if l == r:
            return i
    else:
        return -1
