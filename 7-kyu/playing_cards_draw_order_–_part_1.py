# https://www.codewars.com/kata/630647be37f67000363dff04

def draw(deck):
    print_deck(deck, True)   # Using unicode characters
    print_deck(deck, False)  # Using regular characters

    drawn_cards = []
    while len(deck) > 1:
        drawn_cards.append(deck.pop(0))
        if deck:
            deck.append(deck.pop(0))
    return drawn_cards + deck
