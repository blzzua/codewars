# https://www.codewars.com/kata/56d55dcdc87df58c81000605

def valid_card(card):
    checksum = 0
    for i, digit in enumerate(map(int, card.replace(' ', '')[::-1])):
        if i % 2:
            digit *= 2
            if digit > 8:
                checksum += digit - 9  
            else:
                checksum += digit
        else:
            checksum += digit
    return checksum % 10 == 0
