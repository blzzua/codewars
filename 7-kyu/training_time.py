# https://www.codewars.com/kata/572ab0cfa3af384df7000ff8

def shuffle_it(arr, *swaps):
    for s1, s2 in swaps:
        arr[s1], arr[s2] = arr[s2], arr[s1]
    return arr
