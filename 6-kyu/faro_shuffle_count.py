# https://www.codewars.com/kata/57bc802c615f0ba1e3000029

def faro_cycles(deck_size):
    prev = [i for i in range(deck_size)]
    order = prev[:]
    cycle = 1
    while True:
        deck = []
        for i in range(deck_size // 2):
            deck.extend([order[i], order[i + deck_size // 2]])
        if deck == prev:
            return cycle
        cycle += 1
        order = deck
      
