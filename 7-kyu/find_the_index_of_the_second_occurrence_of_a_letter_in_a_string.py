# https://www.codewars.com/kata/63f96036b15a210058300ca9

def second_symbol(s, symbol):
    return s.find(symbol, s.find(symbol)+1)
    
