# https://www.codewars.com/kata/58f174ed7e9b1f32b40000ec

def max_profit(prices):
    max_ = prices[1] - prices[0]
    mm =  prices[1] - prices[0]
    for price in reversed(prices):
        max_ = max(max_, mm-price)
        mm = max(mm,price)
    return max_ 
