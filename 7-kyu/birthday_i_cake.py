# https://www.codewars.com/kata/5805ed25c2799821cb000005

from  string import ascii_lowercase as al
def cake(candles, debris):
    total_sum = 0
    for i, char in enumerate(debris):
        if i % 2 == 0:
            total_sum += ord(char)
        else:
            total_sum += al.index(char) + 1
    threshold = 0.7 * candles
    if candles == 0 or total_sum <= threshold:
        return 'That was close!'
    else:
        return 'Fire!'
