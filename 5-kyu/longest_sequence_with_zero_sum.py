# https://www.codewars.com/kata/52b4d1be990d6a2dac0002ab

def max_zero_sequence(arr):
    result = []
    for start, _ in enumerate(arr):
        for end in range(len(arr[start:]), 0, -1):
            if len(arr[start:end]) > 0 and sum(arr[start:end]) == 0 and len(arr[start:end]) > len(result):
                result = arr[start:end]
                break
    return result

