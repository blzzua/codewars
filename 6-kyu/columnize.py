# https://www.codewars.com/kata/6087bb6050a6230049a068f1

from itertools import zip_longest 
def columnize(items, columns_count):
    separator = ' | '
    arranged = list(zip_longest(*[iter(items)] * columns_count))
    wides = [max([len(item) for item in col if not (item is None)], default=0)  for col in zip(*arranged)]
    res = []
    for line in arranged:
        res.append(separator.join((str(item) + (' ' *  wide))[:wide] for wide, item in zip(wides, line) if not (item is None)))
    return '\n'.join(res)
