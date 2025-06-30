# https://www.codewars.com/kata/590adadea658017d90000039

def fruit(reels, spins):
    res = sorted([reels[i][j] for i,j in enumerate(spins)])

    if res.count('Wild') == 3:
        return 100
    if res.count('Wild') == 2:
        return 10
    wild_multiplicator = 2 if res.count('Wild') == 1 else 1

    if res.count('Star') == 3:
        return 90
    if res.count('Star') == 2:
        return 9 * wild_multiplicator

    if res.count('Bell') == 3:
        return 80
    if res.count('Bell') == 2:
        return 8 * wild_multiplicator

    if res.count('Shell') == 3:
        return 70
    if res.count('Shell') == 2:
        return 7 * wild_multiplicator

    if res.count('Seven') == 3:
        return 60
    if res.count('Seven') == 2:
        return 6 * wild_multiplicator

    if res.count('Cherry') == 3:
        return 50
    if res.count('Cherry') == 2:
        return 5 * wild_multiplicator

    if res.count('Bar') == 3:
        return 40
    if res.count('Bar') == 2:
        return 4 * wild_multiplicator

    if res.count('King') == 3:
        return 30
    if res.count('King') == 2:
        return 3 * wild_multiplicator

    if res.count('Queen') == 3:
        return 20
    if res.count('Queen') == 2:
        return 2 * wild_multiplicator

    if res.count('Jack') == 3:
        return 10
    if res.count('Jack') == 2:
        return 1 * wild_multiplicator
    
    return 0

