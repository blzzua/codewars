# https://www.codewars.com/kata/597ab747d1ba5b843f0000ca

def buy_or_sell(pairs, harvested_fruit):
    cur = harvested_fruit
    res = []
    for f1, f2 in pairs:
        if f1 == cur:
            cur = f2
            res.append('buy')
        elif f2 == cur:
            res.append('sell')
            cur = f1
        else:
            return 'ERROR'
    return res
  
