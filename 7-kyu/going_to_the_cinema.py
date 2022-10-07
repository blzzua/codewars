# https://www.codewars.com/kata/562f91ff6a8b77dfe900006e

def movie(card, ticket, perc):
    total_card = card 
    total_tickets = 0
    i = 0
    while round(total_card + 0.5) >= total_tickets:
        i += 1
        total_card += ticket * (perc**i)
        total_tickets += ticket
    return i 
    

