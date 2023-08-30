# https://www.codewars.com/kata/57c6c2e1f8392d982a0000f2

def h_histogram(results):
    res = []
    max_h = max(results)
    for i, j in zip(range(1,6+1), results):
        line1 =  f'{i}-' + '#' * j
        if 0 < j < 10:
            line1 += f'{j}' 
        elif j == 0 :
            line1 +=' '
        elif j>=10:
            l1_index = len(line1)
            line1 += f'{j // 10}'
        line1  += ' ' * (max_h - j)
        line2 = ' ' * len(line1)
        if j>=10:
            line2 = ''.join([f'{j % 10}' if i2 == l1_index else c for i2, c in enumerate(line2)][::-1])
        line2 = ''.join(['-' if i3 == len(line1)-2 and i < 6 else c for i3, c in enumerate(line2)])
        res.append(line1[::-1])
        res.append(line2)
    return res

def histogram(rolls):
    hs = h_histogram(rolls)
    return ''.join([''.join(c).rstrip(' ')+'\n' for c in zip(*hs)])
    
