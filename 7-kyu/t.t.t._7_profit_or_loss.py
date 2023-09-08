# https://www.codewars.com/kata/5768b775b8ed4a360f000b20

def profit_loss(records):
    return round(sum((val - val * 100 / (100 + pct)) for val, pct in records),2)
