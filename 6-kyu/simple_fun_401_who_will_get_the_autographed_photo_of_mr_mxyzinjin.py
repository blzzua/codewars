# https://www.codewars.com/kata/5be539ccb062f9a90e0000ac

def who(init_weights, spec_weights, n):
    res = [{'id1':i, 'weight':w} for i, w in enumerate(init_weights, 1)]
    res.sort(key=lambda e: (-e['weight'], e['id1']))
    for i, e in enumerate(res, 1):
        e['weight'] += spec_weights[i % 10 - 1] 
    res.sort(key=lambda e: (-e['weight'], e['id1']))
    return [e['id1'] for e in res[:n]]
