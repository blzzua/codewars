# https://www.codewars.com/kata/5704bf9b38428f1446000a9d

def histogram(values, bin_width):
    if len(values) * bin_width == 0:
        return []
    res = [0 for _ in range((max(values)//bin_width + 1))]
    for v in values: 
        res[v//bin_width] += 1
    return res

