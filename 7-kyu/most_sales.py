# https://www.codewars.com/kata/5e16ffb7297fe00001114824

def top3(products, amounts, prices):
    res = {n: (a*p,-i) for i, (n,a,p) in enumerate(zip(products, amounts, prices))}
    return sorted(res, key=lambda x: res[x], reverse=True)[0:3]
