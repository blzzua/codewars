# https://www.codewars.com/kata/58856a06760b85c4e6000055

def bits_battle(numbers):
    chet   = ''.join([format(n, 'b') for n in numbers if n % 2 == 0 and n != 0])
    nechet = ''.join([format(n, 'b') for n in numbers if n % 2 != 0 and n != 0])

    chet_score = sum(1 for char in chet if char == '0')
    nechet_score = sum(1 for char in nechet if char == '1')

    if chet_score > nechet_score:
        return 'evens win'
    elif chet_score < nechet_score:
        return 'odds win'
    else:
        return 'tie'

