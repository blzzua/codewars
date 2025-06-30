# https://www.codewars.com/kata/5888145122fe8620950000f0

# naive model: works but not pass tests. too slow
def switch_lights(arr):
    for i, candle in enumerate(arr):
        if candle == 1:
            for j in range(i+1):
                arr[j] = 1 - arr[j]
    return arr

