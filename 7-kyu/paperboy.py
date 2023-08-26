# https://www.codewars.com/kata/56ed5f13c4e5d6c5b3000745

price_map = {40: 3.85, 20: 1.93,  10: 0.97, 5: 0.49, 1: 0.1}

def cheapest_quote(n):
    s = 0
    prices_sorted = sorted(price_map.keys(), reverse = True)
    for p in prices_sorted:
        cur_p, rest = divmod(n, p)
        n -= cur_p * p
        s += cur_p * price_map[p] 
    return round(s,2)
