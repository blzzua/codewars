# https://www.codewars.com/kata/569d488d61b812a0f7000015

def data_reverse(data):
    data = data[:] 
    buffer = []
    res = []
    while data:
        buffer.append(data.pop())
        if len(buffer) == 8:
            res.extend(buffer[::-1])
            buffer = []
    return res

# clever
# np.array(np.array_split(data, len(data) // 8)[::-1]).reshape(len(data)).tolist()
