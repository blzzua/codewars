# https://www.codewars.com/kata/586ee462d0982081bf001f07

def fillable(stock, merch, n):
    if merch in stock and stock[merch] >= n:
        return True
    return False

