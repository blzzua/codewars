# https://www.codewars.com/kata/5acbc3b3481ebb23a400007d

def is_flush(cards):
    return all(card[-1] == cards[0][-1:] for card in cards)

