# https://www.codewars.com/kata/5b6db1acb118141f6b000060

def recycle(a):
    res = {'paper': [], 'glass': [], 'organic': [], 'plastic': []}
    for item in a:
        res[item['material']].append(item['type'])
        if 'secondMaterial' in item:
            res[item['secondMaterial']].append(item['type'])
    return tuple(res.values())
