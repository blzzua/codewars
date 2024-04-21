# https://www.codewars.com/kata/58ac59d21c9e1d7dc5000150

def make_parts(arr, chunk_size):
    #return [*map(list,zip(*[iter(arr)] * chunk_size))]
    res = []
    while arr:
        res.append(arr[:chunk_size])
        arr = arr[chunk_size:]
    return res
