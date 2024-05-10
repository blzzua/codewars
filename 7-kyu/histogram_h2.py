# https://www.codewars.com/kata/5d5f5ea8e3d37b001dfd630a

def histogram(results):
    h = u'█'; width = 50
    sum_ = sum(results) or 9223372036854775807
    res = []
    for i, val in zip(range(1,6+1), results):
        bar = h * ((width * val) // sum_)  
        pct = (str(int(100*val/sum_)) + '%') 
        bar_pct = f'{bar} {pct}' if val else ''
        res.append(f'{i}|{bar_pct}\n')
    return ''.join(res[::-1])
