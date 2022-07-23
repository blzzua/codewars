# https://www.codewars.com/kata/5601c5f6ba804403c7000004

def bar_triang(a, b, c):
    return [round(sum(x)/3, 4) for x in zip(a, b, c)]
